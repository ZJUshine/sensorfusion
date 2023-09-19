import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
import argparse


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_name', default='kitti', type=str, help='攻击数据集')
    parser.add_argument('--attack_target', default='none', type=str, help='攻击传感器种类')
    args = parser.parse_args()

dataset_name = args.dataset_name

# original dataset
# dataset_name = "kitti"
# # attack lidar
dataset_name = "lidar_emi_gaussian_noise"
# dataset_name = "lidar_laser_arbitrary_point_injection"
# dataset_name = "lidar_laser_background_noise_injection"
# dataset_name = "lidar_laser_creating_car"
# dataset_name = "lidar_laser_hiding"
# # attack camera
# dataset_name = "camera_acoustic_blur_linear"
# dataset_name = "camera_emi_strip_loss"
# dataset_name = "camera_emi_truncation"
# dataset_name = "camera_laser_hiding"
# dataset_name = "camera_laser_strip_injection"
# dataset_name = "camera_projection_creating"

ROOT_PATH = "/home/usslab/SensorFusion/"
DATASET_PATH = ROOT_PATH + "sensorfusion/PointPainting/detector/data/"+dataset_name

# if ("kitti" in dataset_name):
    # # 配置原始数据集
    # os.makedirs(DATASET_PATH, exist_ok=True)
    # os.symlink(ROOT_PATH + "kitti/training", DATASET_PATH + "/training")
    # os.symlink(ROOT_PATH + "kitti/kitti_infos_train.pkl", DATASET_PATH + "/kitti_infos_train.pkl")
    # os.symlink(ROOT_PATH + "kitti/kitti_infos_val.pkl", DATASET_PATH + "/kitti_infos_val.pkl")

# if ("lidar" in dataset_name):
#     os.makedirs(DATASET_PATH+"/training", exist_ok=True)
#     os.symlink(ROOT_PATH + "kitti/training/calib", DATASET_PATH + "/training/calib")
#     os.symlink(ROOT_PATH + "kitti/training/image_2", DATASET_PATH + "/training/image_2")
#     os.symlink(ROOT_PATH + "kitti/training/image_3", DATASET_PATH + "/training/image_3")
#     os.symlink(ROOT_PATH + "kitti/training/label_2", DATASET_PATH + "/training/label_2")
#     os.symlink(ROOT_PATH + f"kitti_attack/{dataset_name}", DATASET_PATH + "/training/velodyne")
#     os.symlink(ROOT_PATH + "kitti/kitti_infos_train.pkl", DATASET_PATH + "/kitti_infos_train.pkl")
#     os.symlink(ROOT_PATH + "kitti/kitti_infos_val.pkl", DATASET_PATH + "/kitti_infos_val.pkl")

# if ("camera" in dataset_name):
#     os.makedirs(DATASET_PATH+"/training", exist_ok=True)
#     os.symlink(ROOT_PATH + "kitti/training/calib", DATASET_PATH + "training/calib")
#     os.symlink(ROOT_PATH + f"kitti/{dataset_name}", DATASET_PATH + "training/image_2")
#     os.symlink(ROOT_PATH + "kitti/training/label_2", DATASET_PATH + "training/label_2")
#     os.symlink(ROOT_PATH + "kitti_attack/training/velodyne", DATASET_PATH + "training/velodyne")


# 生成中间数据集文件
file = open("/home/usslab/SensorFusion/sensorfusion/PointPainting/painting/painting.py", "r+")
lines = file.readlines()
lines[17] = f"TRAINING_PATH = '/home/usslab/SensorFusion/sensorfusion/PointPainting/detector/data/{dataset_name}/training/'\n"
file.seek(0)
file.writelines(lines)
file.close()

os.system("python /home/usslab/SensorFusion/sensorfusion/PointPainting/painting/painting.py")



file = open("/home/usslab/SensorFusion/sensorfusion/PointPainting/detector/tools/cfgs/dataset_configs/painted_kitti_dataset.yaml", "r+")
lines = file.readlines()
lines[1] = f"DATA_PATH: '/home/usslab/SensorFusion/sensorfusion/PointPainting/detector/data/{dataset_name}'\n"
file.seek(0)
file.writelines(lines)
file.close()



os.system(f"python /home/usslab/SensorFusion/sensorfusion/PointPainting/detector/tools/test.py \
          --cfg_file '/home/usslab/SensorFusion/sensorfusion/PointPainting/detector/tools/cfgs/kitti_models/pointpillar_painted.yaml' \
          --ckpt_dir '/home/usslab/SensorFusion/sensorfusion/PointPainting/detector/output/kitti_models/pointpillar_painted/default/ckpt' \
          --ckpt '/home/usslab/SensorFusion/sensorfusion/PointPainting/detector/output/kitti_models/pointpillar_painted/default/ckpt/checkpoint_epoch_80.pth' \
          --eval_tag '{dataset_name}' \
          --save_to_file")





# 弃用 只能生成3d box

# 测试攻击数据集

# file = open("/home/usslab/SensorFusion/sensorfusion/PointPainting/detector/tools/demo.py", "r+")
# lines = file.readlines()
# lines[99] = f"            os.makedirs('/home/usslab/SensorFusion/sensorfusion/PointPainting/detector/data/{dataset_name}/kitti_inference/data/', exist_ok=True)\n"
# lines[100] = f"            file = open('/home/usslab/SensorFusion/sensorfusion/PointPainting/detector/data/{dataset_name}/kitti_inference/data/' + filename + '.txt','w')\n"
# file.seek(0)
# file.writelines(lines)
# file.close()

# painted_path = f"/home/usslab/SensorFusion/sensorfusion/PointPainting/detector/data/{dataset_name}/training/painted_lidar"

# os.system(f"python /home/usslab/SensorFusion/sensorfusion/PointPainting/detector/tools/demo.py \
#             --cfg_file /home/usslab/SensorFusion/sensorfusion/PointPainting/detector/tools/cfgs/kitti_models/pointpillar_painted.yaml \
#             --ckpt /home/usslab/SensorFusion/sensorfusion/PointPainting/detector/output/kitti_models/pointpillar_painted/default/ckpt/checkpoint_epoch_80.pth \
#             --data_path {painted_path} --ext .npy")
