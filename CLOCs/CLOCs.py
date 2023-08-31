import os
import argparse

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_name', default='kitti', type=str, help='攻击数据集')
    parser.add_argument('--attack_target', default='none', type=str, help='攻击传感器种类')
    args = parser.parse_args()

dataset_name = args.dataset_name

# original dataset
dataset_name = "kitti"
# # attack lidar
dataset_name = "lidar_arbitrary_point_injection"
# dataset_name = "lidar_gaussian_noise"
# dataset_name = "lidar_creating_car"
# dataset_name = "lidar_hiding"
# # attack camera
# dataset_name = "camera_blur"
# dataset_name = "camera_color_strip"
# dataset_name = "camera_hiding"
# dataset_name = "camera_truncation"

ROOT_PATH = "/home/usslab/SensorFusion/"
DATASET_PATH = ROOT_PATH + "sensorfusion/CLOCs/datasets/"+dataset_name

# if ("kitti" in dataset_name):
#     # 配置原始数据集
#     os.makedirs(DATASET_PATH, exist_ok=True)
#     os.symlink(ROOT_PATH + "kitti/training", DATASET_PATH + "/training")
#     os.makedirs(DATASET_PATH + "/training/velodyne_reduced", exist_ok=True)
#     os.symlink(ROOT_PATH + "kitti/testing", DATASET_PATH + "/testing")
#     os.makedirs(DATASET_PATH + "/testing/velodyne_reduced", exist_ok=True)

# #配置攻击数据集
# if ("lidar" in dataset_name):
#     os.makedirs(DATASET_PATH+"/training", exist_ok=True)
#     os.symlink(ROOT_PATH + "kitti/training/calib", DATASET_PATH + "/training/calib")
#     os.symlink(ROOT_PATH + "kitti/training/image_2", DATASET_PATH + "/training/image_2")
#     os.symlink(ROOT_PATH + "kitti/training/image_3", DATASET_PATH + "/training/image_3")
#     os.symlink(ROOT_PATH + "kitti/training/label_2", DATASET_PATH + "/training/label_2")
#     os.symlink(ROOT_PATH + f"kitti_attack/{dataset_name}", DATASET_PATH + "/training/velodyne")
#     os.makedirs(DATASET_PATH + "/training/velodyne_reduced", exist_ok=True)

# # if ("camera" in dataset_name):
# #     os.makedirs(DATASET_PATH+"/training", exist_ok=True)
# #     os.symlink(ROOT_PATH + "kitti/training/calib", DATASET_PATH + "training/calib")
# #     os.symlink(ROOT_PATH + f"kitti/{dataset_name}", DATASET_PATH + "training/image_2")
# #     os.symlink(ROOT_PATH + "kitti/training/label_2", DATASET_PATH + "training/label_2")
# #     os.symlink(ROOT_PATH + "kitti_attack/training/velodyne", DATASET_PATH + "training/velodyne")


# # 生成中间数据集文件
# os.chdir("/home/usslab/SensorFusion/sensorfusion/CLOCs/second/")
# os.system(f"python /home/usslab/SensorFusion/sensorfusion/CLOCs/second/create_data.py create_kitti_info_file \
# --data_path=/home/usslab/SensorFusion/sensorfusion/CLOCs/datasets/{dataset_name}")
# os.system(f"python /home/usslab/SensorFusion/sensorfusion/CLOCs/second/create_data.py create_groundtruth_database \
# --data_path=/home/usslab/SensorFusion/sensorfusion/CLOCs/datasets/{dataset_name}")
# os.system(f"python /home/usslab/SensorFusion/sensorfusion/CLOCs/second/create_data.py create_reduced_point_cloud \
# --data_path=/home/usslab/SensorFusion/sensorfusion/CLOCs/datasets/{dataset_name}")




# file = open("/home/usslab/SensorFusion/sensorfusion/CLOCs/second/configs/car.fhd.config", "r+")
# lines = file.readlines()
# lines[122] = f"    database_info_path: '/home/usslab/SensorFusion/sensorfusion/CLOCs/datasets/{dataset_name}/kitti_dbinfos_train.pkl'\n"
# lines[148] = f"  kitti_info_path: '/home/usslab/SensorFusion/sensorfusion/CLOCs/datasets/{dataset_name}/kitti_infos_train.pkl'\n"
# lines[149] = f"  kitti_root_path: '/home/usslab/SensorFusion/sensorfusion/CLOCs/datasets/{dataset_name}'\n"
# lines[175] = f"  detection_2d_path: '/home/usslab/SensorFusion/sensorfusion/CLOCs/d2_detection_data/{dataset_name}/data'\n"
# lines[187] = f"  kitti_info_path: '/home/usslab/SensorFusion/sensorfusion/CLOCs/datasets/{dataset_name}/kitti_infos_val.pkl'\n"
# lines[188] = f"  #kitti_info_path: '/home/usslab/SensorFusion/sensorfusion/CLOCs/datasets/{dataset_name}/kitti_infos_test.pkl'\n"
# lines[189] = f"  kitti_root_path: '/home/usslab/SensorFusion/sensorfusion/CLOCs/datasets/{dataset_name}'\n"
# file.seek(0)
# file.writelines(lines)
# file.close()

os.makedirs(f"/home/usslab/SensorFusion/sensorfusion/CLOCs/second/results/{dataset_name}",exist_ok=True)
os.chdir("/home/usslab/SensorFusion/sensorfusion/CLOCs/second")
os.system(f"python /home/usslab/SensorFusion/sensorfusion/CLOCs/second/pytorch/train.py evaluate \
--config_path=/home/usslab/SensorFusion/sensorfusion/CLOCs/second/configs/car.fhd.config \
--model_dir=/home/usslab/SensorFusion/sensorfusion/CLOCs/CLOCs_SecCas_pretrained \
--result_path=/home/usslab/SensorFusion/sensorfusion/CLOCs/second/results/{dataset_name} \
--pickle_result=False \
--measure_time=True --batch_size=1")

