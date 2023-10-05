import os

# 读取txt文件中的新文件名
with open('/home/usslab/SensorFusion/kitti/ImageSets/val.txt', 'r', encoding='utf-8') as f:
    new_names = [line.strip() for line in f.readlines()]

# 定义目标文件夹路径
# folder_path1 = '/home/usslab/SensorFusion/sensorfusion/mmdetection3d/second_kitti_results/pred_instances_3d'
folder_path2 = '/home/usslab/SensorFusion/sensorfusion/mmdetection3d/second_lidar_emi_gaussian_noise_results/pred_instances_3d'
folder_path3 = '/home/usslab/SensorFusion/sensorfusion/mmdetection3d/second_lidar_laser_arbitrary_point_injection_results/pred_instances_3d'
folder_path4 = '/home/usslab/SensorFusion/sensorfusion/mmdetection3d/second_lidar_laser_background_noise_injection_results/pred_instances_3d'
folder_path5 = '/home/usslab/SensorFusion/sensorfusion/mmdetection3d/second_lidar_laser_creating_car_results/pred_instances_3d'
folder_path6 = '/home/usslab/SensorFusion/sensorfusion/mmdetection3d/second_lidar_laser_hiding_results/pred_instances_3d'
new_folder_path = '/home/usslab/SensorFusion/sensorfusion/mmdetection3d/results/'
os.makedirs(new_folder_path, exist_ok=True)
for folder_path in [folder_path2, folder_path3, folder_path4, folder_path5, folder_path6]:  
    # 获取文件夹中的所有文件
    files = sorted(os.listdir(folder_path))
    # 将原来的文件拷贝到新的文件夹中并根据txt文件中的文件名重命名
    save_folder_path = os.path.join(new_folder_path, folder_path.split('/')[-2],"data")
    os.makedirs(save_folder_path, exist_ok=True)
    for i in range(len(files)):
        old_name = os.path.join(folder_path, files[i])
        new_name = os.path.join(save_folder_path, new_names[i]+'.txt')
        os.rename(old_name, new_name)

        