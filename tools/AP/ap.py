import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import auc
import os

attack_type = "lidar_creating_car_fpnet"
class_type = "car_detection_3d"
file_path = "/home/usslab/Desktop/data/" + attack_type +"/plot_val/" + class_type + ".txt"

data = np.loadtxt(file_path)

print(data.shape)

plt.plot(data[:,0], data[:,1])
plt.plot(data[:,0], data[:,2])
plt.plot(data[:,0], data[:,3])
plt.show()

ap1 = auc(data[:,0], data[:,1])
ap2 = auc(data[:,0], data[:,2])
ap3 = auc(data[:,0], data[:,3])


d1, d2, d3 = np.zeros((41, 3)), np.zeros((41, 3)), np.zeros((41, 3))
for i in range(3):
    d1[:, i] = data[:, (i+1)*3+1]
    d2[:, i] = data[:, (i+1)*3+2]
    d3[:, i] = data[:, (i+1)*3+3]
d1 = d1[~(d1==0).all(axis=1)].astype(int)
d2 = d2[~(d2==0).all(axis=1)].astype(int)
d3 = d3[~(d3==0).all(axis=1)].astype(int)
print(ap1,ap2,ap3)
print(d1[-1])
print(d2[-1])
print(d3[-1])

# print(d1[:,0]/(d1[:,0]+d1[:,1]))
# print(d1[:,0]/(d1[:,0]+d1[:,2]))
# recall = d1[:,0]/(2906)
# print(recall.shape,data[:,1].shape)
# print(auc([0,0.5],[1,1]))
# pre = np.sort(d1[:,0]/(d1[:,0]+d1[:,1]))[::-1]
# # print(d1)
# print(d2)?
# # print(d3)
# plt.plot(recall, pre,'*')
# plt.show()
# ap1_my = auc(recall,pre)
# ap1_both = auc(recall,data[:len(recall),1])
# print(ap1, ap1_my, ap1_both) # (ap1_both-ap1_my)/ap1_both*100, ap1_both-ap1_my)
# recall = d2[:,0]/(7874)
# pre = np.sort(d2[:,0]/(d2[:,0]+d2[:,1]))[::-1]
# ap2_my = auc(recall,pre)
# ap2_both = auc(recall,data[:len(recall),2])
# print(ap2, ap2_my, ap2_both)#, (ap2_both-ap2_my)/ap2_both*100)
# recall = d3[:,0]/(10960)
# pre = np.sort(d3[:,0]/(d3[:,0]+d3[:,1]))[::-1]
# print(ap3, auc(recall,pre), auc(recall,data[:len(recall),3]))


# recall = d1[:,0]/(2906)
# test = d1[:,0]/(d1[:,0]+d1[:,1])
# for i in range(len(test)):
#     print(np.max(test[i:]))
#     test[i] = np.max(test[i:])
# print(auc(recall,test))




