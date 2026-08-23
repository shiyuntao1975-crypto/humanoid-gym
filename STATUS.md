# 4090 训练状态（自动推送）

- 更新时间: 2026-08-23 10:53:01

## GPU
0, NVIDIA GeForce RTX 4090, 84 %, 8024 MiB
1, NVIDIA GeForce RTX 4090, 79 %, 6788 MiB

## humanoid-gym 训练进程
3955573 python scripts/train.py --task=humanoid_ppo --run_name v2_long --headless
3955574 python scripts/train.py --task=humanoid_ppo --run_name v2_dr --headless

## 训练摘要（hg_train_v2_long.log）
                    [1m Learning iteration 3442/10000 [0m                     
                       Mean reward: 179.57
               Mean episode length: 2401.00
                   Total timesteps: 846151680
                               ETA: 22476.3s
                    [1m Learning iteration 3443/10000 [0m                     
                       Mean reward: 179.65
               Mean episode length: 2401.00
                   Total timesteps: 846397440
                               ETA: 22472.9s

## 最新 checkpoint
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_dr/model_3400.pt
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_long/model_3400.pt
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_dr/model_3300.pt

## HOVER 最近产物
总计 8
drwxrwxr-x 4 robot robot 4096  8月 21 09:54 student
drwxrwxr-x 4 robot robot 4096  8月 20 12:16 teacher
