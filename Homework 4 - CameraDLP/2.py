import numpy as np
import numpy.linalg as LA
import math

n=3
print(n)    

M1=np.array([460, 280, 250, 1])
M2=np.array([50, 380, 350, 1])
M3=np.array([470, 500, 100, 1])
M4=np.array([380, 630, 50*n, 1])
M5=np.array([30*n, 290, 0, 1])
M6=np.array([580, 0, 130, 1])

M1p=np.array([288, 251, 1])
M2p=np.array([79, 510, 1])
M3p=np.array([470, 440, 1])
M4p=np.array([520, 590, 1])
M5p=np.array([365, 388, 1])
M6p=np.array([365, 20, 1])

originali=np.array([M1, M2, M3, M4, M5, M6])
projekcije=np.array([M1p, M2p, M3p, M4p, M5p, M6p])
print()
print("Originali:")
print(originali)
print()
print("Projekcije:")
print(projekcije)
print()

def CameraDLP(originali, projekcije):   
    matrica = []
    n = len(originali)
    for i in range(n):
        matrica.append([0, 0, 0, 0, 
         -projekcije[i][2]*originali[i][0],-projekcije[i][2]*originali[i][1], -projekcije[i][2]*originali[i][2],-projekcije[i][2]*originali[i][3], 
         projekcije[i][1]*originali[i][0],projekcije[i][1]*originali[i][1],projekcije[i][1]*originali[i][2],projekcije[i][1]*originali[i][3]])     
         
        matrica.append([ 
         projekcije[i][2]*originali[i][0], projekcije[i][2]*originali[i][1], projekcije[i][2]*originali[i][2],projekcije[i][2]*originali[i][3],
         0,0,0,0, 
         -projekcije[i][0]*originali[i][0], -projekcije[i][0]*originali[i][1], -projekcije[i][0]*originali[i][2], -projekcije[i][0]*originali[i][3]])     
         
    #print("Matrica:")
    #print(matrica)
    
    #svd, A=UDV^T
    
    _, _, V = LA.svd(matrica)
    T = V[-1]*(-1)
    return T
   
T=CameraDLP(originali, projekcije)
T=T.reshape((3,4))
T=T/T[0,0]
print("Matrica kamere T, posto je cuvana kao niz nije lepo zaokruzeno")
print(T)
print()
print("Matrica kamere T")
M1=[T[0,0].round(decimals=0), T[0,1].round(decimals=2), T[0,2].round(decimals=3), T[0,3].round(decimals=2)]
M2=[T[1,0].round(decimals=4), T[1,1].round(decimals=4), T[1,2].round(decimals=4), T[1,3].round(decimals=1)]
M3=[T[2,0].round(decimals=7), T[2,1].round(decimals=8), T[2,2].round(decimals=7), T[2,3].round(decimals=4)]
print("[", M1)
print(" ", M2)
print(" ",M3,"]")
