import numpy as np
from sklearn.metrics import auc
import os
import time
import csv

mode = "val"
if mode == "train":
    n_groundtruth = [3062, 7832, 10750]
elif mode == "val":
    n_groundtruth = [2906, 7874, 10960]
else:
    n_groundtruth = [5968, 15706, 21710]
# class_type = ["car", "pedestrian", "cyclist"]
class_type = ["car"]
# detection_type = ["_detection", "_detection_3d", "_detection_ground"]
detection_type = ["_detection_3d"]
model_type = ["point", "fpnet", "virconv_l", "virconv_t", "epnet", "avod", "clocs"]
attack_type = ["benign", "lidar_creating_car", "camera_creating", "lidar_hiding", "camera_hiding"]
folders_path = "/home/usslab/Desktop/data/"


result_file = open("AP_result.txt", 'a')
result_csv = open("AP_val.csv",'w')
writer = csv.writer(result_csv)
header = ['model', 'attack', 'ap_easy', 'ap_easy_delta', 'ap_moderate', 'ap_moderate_delta', 'ap_hard', 'ap_hard_delta',\
          'tp_easy', 'tp_easy_delta', 'tp_moderate', 'tp_moderate_delta', 'tp_hard', 'tp_hard_delta',\
            'fp_easy', 'fp_easy_delta', 'fp_moderate', 'fp_moderate_delta', 'fp_hard', 'fp_hard_delta',\
                'fn_easy', 'fn_easy_delta', 'fn_moderate', 'fn_moderate_delta', 'fn_hard', 'fn_hard_delta']
# writer.writerow(header)
count = 0
str0 = str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
str0 = str0.center(61,'*')
result_file.write(str0+'\n')
str1 = "mode==%s" % mode
str1 = str1.center(61,'*')
result_file.write(str1)
result_file.write("\n\n")

benign_data = []

for model in model_type:
    for attack in attack_type:
        plot_dir = folders_path + attack + "_" + model + "/plot_" + mode
        if os.path.exists(plot_dir):
            str1 = attack + "_" + model
            str1 = str1.center(61,'-')
            result_file.write(str1+"\n")
            for c in class_type:
                for d in detection_type:
                    RP_file = plot_dir + "/" + c + d + ".txt"
                    if os.path.exists(RP_file):
                        RP_data = np.loadtxt(RP_file)
                        d1, d2, d3 = np.zeros((41, 3)), np.zeros((41, 3)), np.zeros((41, 3))
                        for i in range(3):
                            d1[:, i] = RP_data[:, (i+1)*3+1]  # 4
                            d2[:, i] = RP_data[:, (i+1)*3+2]  # 8
                            d3[:, i] = RP_data[:, (i+1)*3+3]  # 12
                        d1 = d1[~(d1==0).all(axis=1)].astype(int)
                        d2 = d2[~(d2==0).all(axis=1)].astype(int)
                        d3 = d3[~(d3==0).all(axis=1)].astype(int)
                        # pre1 = np.sort(d1[:,0]/(d1[:,0]+d1[:,1]))[::-1]
                        # pre2 = np.sort(d2[:,0]/(d2[:,0]+d2[:,1]))[::-1]
                        # pre3 = np.sort(d3[:,0]/(d3[:,0]+d3[:,1]))[::-1]
                        # AP_easy = auc(np.insert(d1[:,0]/n_groundtruth[0],0,0), np.insert(RP_data[:len(d1[:,0]),1],0,0))
                        # AP_moderate = auc(np.insert(d2[:,0]/n_groundtruth[1],0,0), np.insert(RP_data[:len(d2[:,0]),2],0,0))
                        # AP_hard = auc(np.insert(d3[:,0]/n_groundtruth[2],0,0), np.insert(RP_data[:len(d3[:,0]),3],0,0))
                        # result_file.write("|%s:   %f  %f  %f (ours)    |\n" % (c+d, AP_easy, AP_moderate, AP_hard))
                        AP_easy = auc(RP_data[:,0], RP_data[:,1])
                        AP_moderate = auc(RP_data[:,0], RP_data[:,2])
                        AP_hard = auc(RP_data[:,0], RP_data[:,3])
                        result_file.write("|%s:   %f  %f  %f (official)|\n" % (c+d, AP_easy, AP_moderate, AP_hard))
                        result_file.write("|tp_fp_fn_easy:      %-6d    %-6d    %-6d             |\n" % (d1[-1][0], d1[-1][1], d1[-1][2]))
                        result_file.write("|tp_fp_fn_moderate:  %-6d    %-6d    %-6d             |\n" % (d2[-1][0], d2[-1][1], d2[-1][2]))
                        result_file.write("|tp_fp_fn_hard:      %-6d    %-6d    %-6d             |\n" % (d3[-1][0], d3[-1][1], d3[-1][2]))
                        result_file.write("-------------------------------------------------------------\n")
                        count = count + 1
            result_file.write("\n")
        if attack == 'benign':
            benign_data = [AP_easy, AP_moderate, AP_hard, d1[-1][0], d1[-1][1], d1[-1][2], d2[-1][0], d2[-1][1], d2[-1][2], d3[-1][0], d3[-1][1], d3[-1][2]]
            content1 = [model, attack, 'car_detection_3d', AP_easy, 0,0, AP_moderate, 0,0,AP_hard,0, 0]
            content2 = [model, attack, 'tp_fp_fn_easy', d1[-1][0], 0,0, d1[-1][1], 0,0, d1[-1][2],0, 0]
            content3 = [model, attack, 'tp_fp_fn_moderate', d2[-1][0], 0,0, d2[-1][1], 0, d2[-1][2],0, 0]            
            content4 = [model, attack, 'tp_fp_fn_hard', d3[-1][0], 0,0, d3[-1][1], 0,0, d3[-1][2],0, 0]
        else:
            content1 = [model, attack, 'car_detection_3d', AP_easy, AP_easy-benign_data[0],AP_easy/benign_data[0]-1, AP_moderate, AP_moderate-benign_data[1],AP_moderate/benign_data[1]-1, AP_hard, AP_hard-benign_data[2],AP_hard/benign_data[2]-1]
            content2 = [model, attack, 'tp_fp_fn_easy', d1[-1][0], d1[-1][0]-benign_data[3],d1[-1][0]/benign_data[3]-1, d1[-1][1], d1[-1][1]-benign_data[4],d1[-1][1]/benign_data[4]-1, d1[-1][2], d1[-1][2]-benign_data[5],d1[-1][2]/benign_data[5]-1]
            content3 = [model, attack, 'tp_fp_fn_moderate', d2[-1][0], d2[-1][0]-benign_data[6],d2[-1][0]/benign_data[6]-1, d2[-1][1], d2[-1][1]-benign_data[7],d2[-1][1]/benign_data[7]-1, d2[-1][2], d2[-1][2]-benign_data[8],d2[-1][2]/benign_data[8]-1]            
            content4 = [model, attack, 'tp_fp_fn_hard', d3[-1][0], d3[-1][0]-benign_data[9],d3[-1][0]/benign_data[9]-1, d3[-1][1], d3[-1][1]-benign_data[10],d3[-1][1]/benign_data[10]-1, d3[-1][2], d3[-1][2]-benign_data[11],d3[-1][2]/benign_data[11]-1]
        writer.writerow(content1)
        writer.writerow(content2)
        writer.writerow(content3)
        writer.writerow(content4)
                   
result_file.write("*************************************************************\n")               
result_file.write("\n")
result_csv.close()
result_file.close()
print(count)