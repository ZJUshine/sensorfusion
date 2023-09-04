import os
import argparse
os.environ["CUDA_VISIBLE_DEVICES"] = "2"
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_name', default='kitti', type=str, help='攻击数据集')
    parser.add_argument('--attack_target', default='none', type=str, help='攻击传感器种类')
    args = parser.parse_args()

dataset_name = args.dataset_name

# original dataset
# dataset_name = "kitti"
# # attack lidar
# dataset_name = "lidar_laser_arbitrary_point_injection"
# dataset_name = "lidar_laser_background_noise_injection"
dataset_name = "lidar_laser_creating_car"
# dataset_name = "lidar_laser_hiding"
# # attack camera
# dataset_name = "camera_acoustic_blur"
# dataset_name = "camera_emi_strip_loss"
# dataset_name = "camera_emi_truncation"
# dataset_name = "camera_laser_hiding"
# dataset_name = "camera_laser_strip_injection"
# dataset_name = "camera_projection_creating"

ROOT_PATH = "/home/usslab/SensorFusion/"
DATASET_PATH = ROOT_PATH + "sensorfusion/VirConv/data/"+dataset_name

# if ("kitti" in dataset_name):
#     # 配置原始数据集
#     os.makedirs(DATASET_PATH, exist_ok=True)
#     os.symlink(ROOT_PATH + "kitti/training", DATASET_PATH + "/training")
#     os.symlink(ROOT_PATH + "kitti/testing", DATASET_PATH + "/testing")

# #配置攻击数据集
# if ("lidar" in dataset_name):
#     os.makedirs(DATASET_PATH+"/training", exist_ok=True)
#     os.symlink(ROOT_PATH + "kitti/training/calib", DATASET_PATH + "/training/calib")
#     os.symlink(ROOT_PATH + "kitti/training/image_2", DATASET_PATH + "/training/image_2")
#     os.symlink(ROOT_PATH + "kitti/training/label_2", DATASET_PATH + "/training/label_2")
#     os.symlink(ROOT_PATH + f"kitti_attack/{dataset_name}", DATASET_PATH + "/training/velodyne")
#     os.symlink(ROOT_PATH + "kitti/training/planes", DATASET_PATH + "/training/planes")
#     os.symlink("/home/usslab/SensorFusion/sensorfusion/VirConv/data/kitti/ImageSets", DATASET_PATH + "/ImageSets")


# # if ("camera" in dataset_name):
# #     os.makedirs(DATASET_PATH+"/training", exist_ok=True)
# #     os.symlink(ROOT_PATH + "kitti/training/calib", DATASET_PATH + "training/calib")
# #     os.symlink(ROOT_PATH + f"kitti/{dataset_name}", DATASET_PATH + "training/image_2")
# #     os.symlink(ROOT_PATH + "kitti/training/label_2", DATASET_PATH + "training/label_2")
# #     os.symlink(ROOT_PATH + "kitti_attack/training/velodyne", DATASET_PATH + "training/velodyne")


# # 生成中间数据集文件
# file = open("/home/usslab/SensorFusion/sensorfusion/VirConv/tools/PENet/main.py", "r+")
# lines = file.readlines()
# lines[154] = f"args.result = os.path.join('..', 'results_{dataset_name}')\n"
# file.seek(0)
# file.writelines(lines)
# file.close()

os.chdir("/home/usslab/SensorFusion/sensorfusion/VirConv/tools/PENet")
os.system(f"python /home/usslab/SensorFusion/sensorfusion/VirConv/tools/PENet/main.py \
          --evaluate '/home/usslab/SensorFusion/sensorfusion/VirConv/tools/PENet/pe.pth.tar' \
          --test \
          --detpath /home/usslab/SensorFusion/sensorfusion/VirConv/data/{dataset_name}/training")

# os.chdir("/home/usslab/SensorFusion/sensorfusion/VirConv")
# file = open("/home/usslab/SensorFusion/sensorfusion/VirConv/tools/cfgs/dataset_configs/kitti_dataset.yaml", "r+")
# lines = file.readlines()
# lines[0] = f"DATA_PATH: '/home/usslab/SensorFusion/sensorfusion/VirConv/data/{dataset_name}'\n"
# file.seek(0)
# file.writelines(lines)
# file.close()

# os.system(f"python -m pcdet.datasets.kitti.kitti_dataset_mm create_kitti_infos tools/cfgs/dataset_configs/kitti_dataset.yaml")

# os.chdir("/home/usslab/SensorFusion/sensorfusion/VirConv/tools")
# os.system(f"python /home/usslab/SensorFusion/sensorfusion/VirConv/tools/test.py \
# --cfg_file='/home/usslab/SensorFusion/sensorfusion/VirConv/tools/cfgs/models/kitti/VirConv-L.yaml' \
# --ckpt='/home/usslab/SensorFusion/sensorfusion/VirConv/tools/ckpt/VirConv-L2.pth' \
# --save_to_file")