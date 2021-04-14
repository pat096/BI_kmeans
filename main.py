#Wais Patrick Assignment 3

import pandas as pd
import numpy as np

df = pd.read_csv('input.csv',delimiter=';',header=None, decimal=",")

number_cluster = df.loc[0,0]
elements = df.loc[1,0]

array = df.to_numpy()
array = array[2:20,:]
#Append column for cluster number
output = np.insert(array, 0, values=0, axis=1) # Insert column at position 0

w, h = 2, int(number_cluster)
k_means_array = [[0 for x in range(w)] for y in range(h)]
iteration = 0

#Define random means
for i in range(0,3):
    k_means_array[i][0] = np.random.uniform(min(array[:,1]), max(array[:,0]))#X-coor
    k_means_array[i][1] = np.random.uniform(min(array[:,1]), max(array[:,1]))#Y-coor

#Calculate manhattan distance
#print('Array')
#print(array[0,:])
#print("KMEans 1")
#print(k_means_array[0][:])
#print("KMEans 2")
#print(k_means_array[1][:])
#print("KMEans 3")
#print(k_means_array[2][:])
mean_array_k1X = []
mean_array_k2X = []
mean_array_k3X = []
mean_array_k1Y = []
mean_array_k2Y = []
mean_array_k3Y = []


flag = 0 #check if kmeans changes in new iteration

while(flag == 0):

    iteration = iteration + 1
    mean_array_k1X.clear()
    mean_array_k1Y.clear()
    mean_array_k2X.clear()
    mean_array_k2Y.clear()
    mean_array_k3X.clear()
    mean_array_k3Y.clear()

    for i in range(0,18):
        #mean_array_k1X_old = k_means_array[0][0]
        sum1 = abs(array[i,0] - k_means_array[0][0]) + abs(array[i,1] - k_means_array[0][1])
        sum2 = abs(array[i,0] - k_means_array[1][0]) + abs(array[i,1] - k_means_array[1][1])
        sum3 = abs(array[i,0] - k_means_array[2][0]) + abs(array[i,1] - k_means_array[2][1])
        if(sum1<sum2 and sum1<sum3):
            output[i,0] = 1
            mean_array_k1X.append(array[i,0])
            mean_array_k1Y.append(array[i,1])
        elif(sum2<sum3 and sum2<sum1):
            output[i,0] = 2
            mean_array_k2X.append(array[i,0])
            mean_array_k2Y.append(array[i,1])
        elif(sum3<sum1 and sum3<sum2):
            output[i,0] = 3
            mean_array_k3X.append(array[i,0])
            mean_array_k3Y.append(array[i,1])

    if(k_means_array[0][0] == np.mean(mean_array_k1X)):
        flag = 1
    else:
        k_means_array[0][0] = np.mean(mean_array_k1X)#X-coor
        k_means_array[0][1] = np.mean(mean_array_k1Y)#Y-coor
        k_means_array[1][0] = np.mean(mean_array_k2X)
        k_means_array[1][1] = np.mean(mean_array_k2Y)
        k_means_array[2][0] = np.mean(mean_array_k3X)
        k_means_array[2][1] = np.mean(mean_array_k3Y)


df2 = pd.DataFrame(np.array([[number_cluster,'' ,'' ], [k_means_array[0][0], k_means_array[0][1], ''], [k_means_array[1][0], k_means_array[1][1],''],[k_means_array[2][0],k_means_array[2][1],''],
                             [iteration,'',''],[18,2,'']]))

#print(df2)
#print(output)
output = pd.DataFrame(data=output)
result = df2.append(output)

print(result)





























