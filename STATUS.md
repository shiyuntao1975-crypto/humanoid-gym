# 4090 训练状态（自动推送）

- 更新时间: 2026-08-23 07:53:01

## GPU
0, NVIDIA GeForce RTX 4090, 78 %, 8032 MiB
1, NVIDIA GeForce RTX 4090, 80 %, 6788 MiB

## humanoid-gym 训练进程
3955573 python scripts/train.py --task=humanoid_ppo --run_name v2_long --headless
3955574 python scripts/train.py --task=humanoid_ppo --run_name v2_dr --headless

## 训练摘要（hg_train_v2_long.log）
                     [1m Learning iteration 290/10000 [0m                     
                       Mean reward: 134.13
               Mean episode length: 2298.23
                   Total timesteps: 71516160
                               ETA: 34173.0s
                     [1m Learning iteration 291/10000 [0m                     
                       Mean reward: 137.80
               Mean episode length: 2352.85
                   Total timesteps: 71761920
                               ETA: 34167.9s

## 最新 checkpoint
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_long/model_200.pt
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_dr/model_200.pt
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_long/model_100.pt

## HOVER 最近产物
总计 8
drwxrwxr-x 4 robot robot 4096  8月 21 09:54 student
drwxrwxr-x 4 robot robot 4096  8月 20 12:16 teacher
