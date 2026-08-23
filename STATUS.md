# 4090 训练状态（自动推送）

- 更新时间: 2026-08-23 14:53:01

## GPU
0, NVIDIA GeForce RTX 4090, 78 %, 8024 MiB
1, NVIDIA GeForce RTX 4090, 76 %, 6788 MiB

## humanoid-gym 训练进程
3955573 python scripts/train.py --task=humanoid_ppo --run_name v2_long --headless
3955574 python scripts/train.py --task=humanoid_ppo --run_name v2_dr --headless

## 训练摘要（hg_train_v2_long.log）
                    [1m Learning iteration 7654/10000 [0m                     
                       Mean reward: 183.02
               Mean episode length: 2386.71
                   Total timesteps: 1881292800
                               ETA: 8017.1s
                    [1m Learning iteration 7655/10000 [0m                     
                       Mean reward: 183.45
               Mean episode length: 2390.91
                   Total timesteps: 1881538560
                               ETA: 8013.7s

## 最新 checkpoint
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_dr/model_7600.pt
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_long/model_7600.pt
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_dr/model_7500.pt

## HOVER 最近产物
总计 8
drwxrwxr-x 4 robot robot 4096  8月 21 09:54 student
drwxrwxr-x 4 robot robot 4096  8月 20 12:16 teacher
