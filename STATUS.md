# 4090 训练状态（自动推送）

- 更新时间: 2026-08-23 15:23:01

## GPU
0, NVIDIA GeForce RTX 4090, 74 %, 8024 MiB
1, NVIDIA GeForce RTX 4090, 76 %, 6788 MiB

## humanoid-gym 训练进程
3955573 python scripts/train.py --task=humanoid_ppo --run_name v2_long --headless
3955574 python scripts/train.py --task=humanoid_ppo --run_name v2_dr --headless

## 训练摘要（hg_train_v2_long.log）
                    [1m Learning iteration 8182/10000 [0m                     
                       Mean reward: 183.52
               Mean episode length: 2401.00
                   Total timesteps: 2011054080
                               ETA: 6212.0s
                    [1m Learning iteration 8183/10000 [0m                     
                       Mean reward: 183.36
               Mean episode length: 2401.00
                   Total timesteps: 2011299840
                               ETA: 6208.6s

## 最新 checkpoint
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_dr/model_8100.pt
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_long/model_8100.pt
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_dr/model_8000.pt

## HOVER 最近产物
总计 8
drwxrwxr-x 4 robot robot 4096  8月 21 09:54 student
drwxrwxr-x 4 robot robot 4096  8月 20 12:16 teacher
