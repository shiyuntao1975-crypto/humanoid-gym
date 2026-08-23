# 4090 训练状态（自动推送）

- 更新时间: 2026-08-23 11:23:01

## GPU
0, NVIDIA GeForce RTX 4090, 79 %, 8024 MiB
1, NVIDIA GeForce RTX 4090, 83 %, 6788 MiB

## humanoid-gym 训练进程
3955573 python scripts/train.py --task=humanoid_ppo --run_name v2_long --headless
3955574 python scripts/train.py --task=humanoid_ppo --run_name v2_dr --headless

## 训练摘要（hg_train_v2_dr.log）
                    [1m Learning iteration 3962/10000 [0m                     
                       Mean reward: 180.05
               Mean episode length: 2401.00
                   Total timesteps: 973946880
                               ETA: 20712.2s
                    [1m Learning iteration 3963/10000 [0m                     
                       Mean reward: 179.88
               Mean episode length: 2401.00
                   Total timesteps: 974192640
                               ETA: 20708.7s

## 最新 checkpoint
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_dr/model_3900.pt
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_long/model_3900.pt
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_dr/model_3800.pt

## HOVER 最近产物
总计 8
drwxrwxr-x 4 robot robot 4096  8月 21 09:54 student
drwxrwxr-x 4 robot robot 4096  8月 20 12:16 teacher
