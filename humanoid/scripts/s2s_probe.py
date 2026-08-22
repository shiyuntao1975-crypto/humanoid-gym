import os, math, sys
import numpy as np
import mujoco
from collections import deque
from scipy.spatial.transform import Rotation as R
from humanoid.envs import XBotLCfg
import torch

MODEL = sys.argv[1] if len(sys.argv) > 1 else '/home/robot/humanoid-gym/logs/XBot_ppo/exported/policies/policy_1.pt'
print('PROBE MODEL =', MODEL)

class cmd:
    vx = 0.4; vy = 0.0; dyaw = 0.0

def quat2euler(quat):
    x, y, z, w = quat
    t0 = +2.0*(w*x+y*z); t1 = +1.0-2.0*(x*x+y*y); roll = np.arctan2(t0, t1)
    t2 = +2.0*(w*y-z*x); t2 = np.clip(t2, -1, 1); pitch = np.arcsin(t2)
    t3 = +2.0*(w*z+x*y); t4 = +1.0-2.0*(y*y+z*z); yaw = np.arctan2(t3, t4)
    return np.array([roll, pitch, yaw])

cfg = XBotLCfg()
model = mujoco.MjModel.from_xml_path('/home/robot/humanoid-gym/resources/robots/XBot/mjcf/XBot-L.xml')
model.opt.timestep = 0.001
data = mujoco.MjData(model)
mujoco.mj_step(model, data)
try:
    bid = model.body('pelvis').id
except Exception:
    bid = 1
print('PROBE pelvis body id =', bid, 'ref_z =', model.body(bid).pos[2])
policy = torch.jit.load(MODEL)

kps = np.array([200,200,350,350,15,15]*2, dtype=np.double)
kds = np.array(12*[10.], dtype=np.double)
tau_limit = 200.*np.ones(12, dtype=np.double)
dt, decimation = 0.001, 10
num_actions = cfg.env.num_actions

target_q = np.zeros(num_actions, dtype=np.double)
action = np.zeros(num_actions, dtype=np.double)
hist_obs = deque()
for _ in range(cfg.env.frame_stack):
    hist_obs.append(np.zeros([1, cfg.env.num_single_obs], dtype=np.double))

T, AZ, PIT, XY = [], [], [], []
count = 0
for _ in range(int(60.0/dt)):
    q = data.qpos.astype(np.double); dq = data.qvel.astype(np.double)
    quat = data.sensor('orientation').data[[1,2,3,0]].astype(np.double)
    r = R.from_quat(quat)
    omega = data.sensor('angular-velocity').data.astype(np.double)
    q12 = q[-12:]; dq12 = dq[-12:]
    if count % decimation == 0:
        obs = np.zeros([1, cfg.env.num_single_obs], dtype=np.float32)
        eu = quat2euler(quat); eu[eu > math.pi] -= 2*math.pi
        obs[0,0] = math.sin(2*math.pi*count*dt/0.64)
        obs[0,1] = math.cos(2*math.pi*count*dt/0.64)
        obs[0,2] = cmd.vx*cfg.normalization.obs_scales.lin_vel
        obs[0,3] = 0.0
        obs[0,4] = 0.0
        obs[0,5:17] = q12*cfg.normalization.obs_scales.dof_pos
        obs[0,17:29] = dq12*cfg.normalization.obs_scales.dof_vel
        obs[0,29:41] = action
        obs[0,41:44] = omega
        obs[0,44:47] = eu
        obs = np.clip(obs, -cfg.normalization.clip_observations, cfg.normalization.clip_observations)
        hist_obs.append(obs); hist_obs.popleft()
        pin = np.zeros([1, cfg.env.num_observations], dtype=np.float32)
        for i in range(cfg.env.frame_stack):
            pin[0, i*cfg.env.num_single_obs:(i+1)*cfg.env.num_single_obs] = hist_obs[i][0,:]
        action[:] = policy(torch.tensor(pin))[0].detach().numpy()
        action = np.clip(action, -cfg.normalization.clip_actions, cfg.normalization.clip_actions)
        target_q = action*cfg.control.action_scale
    tau = (target_q-q12)*kps + (0.0-dq12)*kds
    tau = np.clip(tau, -tau_limit, tau_limit)
    data.ctrl = tau
    mujoco.mj_step(model, data)
    if count % 100 == 0:
        az = data.xpos[bid][2]
        pit = quat2euler(data.sensor('orientation').data[[1,2,3,0]].astype(np.double))[1]
        T.append(count*dt); AZ.append(az); PIT.append(pit); XY.append((data.qpos[0], data.qpos[1]))
    count += 1

T=np.array(T); AZ=np.array(AZ); PIT=np.array(PIT); XY=np.array(XY)
fall = np.where((AZ < 0.45) | (np.abs(PIT) > 0.6))[0]
print(f'PROBE abs pelvis z: start={AZ[0]:.3f} min={AZ.min():.3f}@{T[AZ.argmin()]:.1f}s final={AZ[-1]:.3f}')
print(f'PROBE upright-time (z>=0.45 & |pitch|<=0.6): {(len(T)-len(fall))*0.1:.1f}s of 60s')
if len(fall):
    print(f'PROBE FIRST_FALL t={T[fall[0]]:.1f}s')
    rec = np.where((AZ >= 0.45) & (np.abs(PIT) <= 0.6))[0]
    print(f'PROBE recovered-after-fall: {"YES" if len(rec) and rec[-1] > fall[0]+50 else "NO (stays down)"}')
for i in range(30, 170, 5):  # t=3..17s every 0.5s
    if i < len(T): print(f'PROBE t={T[i]:4.1f}s absz={AZ[i]:.3f} pitch={PIT[i]:+.2f}')
v5 = np.linalg.norm(np.array(XY[50])-np.array(XY[5]))/4.5
print(f'PROBE avg speed t=0.5-5s: {v5:.2f} m/s (cmd 0.4)')
print('PROBE DONE', MODEL)
