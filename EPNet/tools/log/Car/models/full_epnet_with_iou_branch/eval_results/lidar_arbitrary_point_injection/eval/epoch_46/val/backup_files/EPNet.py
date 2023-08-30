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
DATASET_PATH = ROOT_PATH + "sensorfusion/EPNet/"+dataset_name+"/KITTI"

# if ("kitti" in dataset_name):
#     # 配置原始数据集
#     os.makedirs(DATASET_PATH + "/object", exist_ok=True)
#     os.symlink(ROOT_PATH + "kitti/ImageSets", DATASET_PATH + "/ImageSets")
#     os.symlink(ROOT_PATH + "kitti/training", DATASET_PATH + "/object/training")
#     os.symlink(ROOT_PATH + "kitti/testing", DATASET_PATH + "/object/testing")

    # 配置攻击数据集
# if ("lidar" in dataset_name):
#     os.makedirs(DATASET_PATH+"/object/training", exist_ok=True)
#     os.symlink(ROOT_PATH + "kitti/ImageSets", DATASET_PATH + "/ImageSets")
#     os.symlink(ROOT_PATH + "kitti/training/calib", DATASET_PATH + "/object/training/calib")
#     os.symlink(ROOT_PATH + "kitti/training/image_2", DATASET_PATH + "/object/training/image_2")
#     os.symlink(ROOT_PATH + "kitti/training/image_3", DATASET_PATH + "/object/training/image_3")
#     os.symlink(ROOT_PATH + "kitti/training/label_2", DATASET_PATH + "/object/training/label_2")
#     os.symlink(ROOT_PATH + f"kitti_attack/{dataset_name}", DATASET_PATH + "/object/training/velodyne")

# if ("camera" in dataset_name):
#     os.makedirs(DATASET_PATH+"/training", exist_ok=True)
#     os.symlink(ROOT_PATH + "kitti/training/calib", DATASET_PATH + "training/calib")
#     os.symlink(ROOT_PATH + f"kitti/{dataset_name}", DATASET_PATH + "training/image_2")
#     os.symlink(ROOT_PATH + "kitti/training/label_2", DATASET_PATH + "training/label_2")
#     os.symlink(ROOT_PATH + "kitti_attack/training/velodyne", DATASET_PATH + "training/velodyne")


# # 生成中间数据集文件
# file = open("/home/usslab/SensorFusion/sensorfusion/PointPainting/painting/painting.py", "r+")
# lines = file.readlines()
# lines[17] = f"TRAINING_PATH = '/home/usslab/SensorFusion/sensorfusion/PointPainting/detector/data/{dataset_name}/training/'\n"
# file.seek(0)
# file.writelines(lines)
# file.close()

# os.system("python /home/usslab/SensorFusion/sensorfusion/PointPainting/painting/painting.py")



file = open("/home/usslab/SensorFusion/sensorfusion/EPNet/tools/eval_rcnn.py", "r+")
lines = file.readlines()
lines[926] = f"    DATA_PATH = os.path.join('/home/usslab/SensorFusion/sensorfusion/EPNet/{dataset_name}')\n"
file.seek(0)
file.writelines(lines)
file.close()





os.system(f"CUDA_VISIBLE_DEVICES=0,1,2,3 python /home/usslab/SensorFusion/sensorfusion/EPNet/tools/eval_rcnn.py \
          --cfg_file /home/usslab/SensorFusion/sensorfusion/EPNet/tools/cfgs/LI_Fusion_with_attention_use_ce_loss.yaml \
          --eval_mode rcnn_online \
          --output_dir /home/usslab/SensorFusion/sensorfusion/EPNet/tools/log/Car/models/full_epnet_with_iou_branch/eval_results/{dataset_name}  \
          --ckpt /home/usslab/SensorFusion/sensorfusion/EPNet/tools/log/Car/models/full_epnet_with_iou_branch/ckpt/checkpoint_epoch_46.pth \
          --set LI_FUSION.ENABLED True LI_FUSION.ADD_Image_Attention True RCNN.POOL_EXTRA_WIDTH 0.2  RPN.SCORE_THRESH 0.2 RCNN.SCORE_THRESH 0.2  USE_IOU_BRANCH True")

