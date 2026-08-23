# 4090 训练状态（自动推送）

- 更新时间: 2026-08-23 16:23:01

## GPU
0, NVIDIA GeForce RTX 4090, 83 %, 8030 MiB
1, NVIDIA GeForce RTX 4090, 76 %, 6788 MiB

## humanoid-gym 训练进程
3955573 python scripts/train.py --task=humanoid_ppo --run_name v2_long --headless
3955574 python scripts/train.py --task=humanoid_ppo --run_name v2_dr --headless

## 训练摘要（hg_train_v2_long.log）
                    [1m Learning iteration 9234/10000 [0m                     
                       Mean reward: 184.88
               Mean episode length: 2401.00
                   Total timesteps: 2269593600
                               ETA: 2617.2s
                    [1m Learning iteration 9235/10000 [0m                     
                       Mean reward: 184.76
               Mean episode length: 2401.00
                   Total timesteps: 2269839360
                               ETA: 2613.8s

## 最新 checkpoint
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_dr/model_9200.pt
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_long/model_9200.pt
/home/robot/humanoid-gym/logs/XBot_ppo/Aug23_07-35-40_v2_dr/model_9100.pt

## HOVER 最近产物
总计 8
drwxrwxr-x 4 robot robot 4096  8月 21 09:54 student
drwxrwxr-x 4 robot robot 4096  8月 20 12:16 teacher
