import numpy as np
import numpy.linalg as LA

n=3
print(n)

T=[[5, -1-2*n, 3, 18-3*n],
   [0, -1, 5, 21],
   [0, -1, 0, 1]];
'''
T=[[1,5,7,-2],
   [3,0,2,3],
   [4,-1,0,1]]
'''   
def ParametriKamere(T):
    T=np.array(T)
    print("Matrica kamere T(3x4):")
    print(T)
    print()
    T0=T[:, 0:3]
    print("Matrica T0:")
    print(T0)
    print()
  #  print("Determinanta matrice T0:")
    det_T0=LA.det(T0)
   # print(det_T0)
    if det_T0<0:
   #     print("Posto je determinata manja od 0, mnozimo matricu T sa -1.")
        T=T*(-1)
        T0=T0[:, 0:3]
    #    print("Sada je matirca T")
    #    print(T)
    #    print("Matrica T0 je sada:")
    #    print(T0)
        
    T0_inv=LA.inv(T0);
  #  print("Inverz matrice T0 je:")
  #  print(T0_inv)
    Q, R= LA.qr(T0_inv)
    print("Primenjena je QR dekompozicija:")
    print()
    print("Matrica Q:")
    print(Q)
    print()
    print("Matrica R:")
    print(R)
    print()
    if R[0,0]<0:
        R[0, :]=R[0, :]*(-1)
        Q[:, 0]=Q[:, 0]*(-1)
    if R[1,1]<0:
        R[1, :]=R[1, :]*(-1)
        Q[:, 1]=Q[:, 1]*(-1)
    if R[2,2]<0:      
        R[2, :]=R[2, :]*(-1)
        Q[:, 2]=Q[:, 2]*(-1)  
  #  print("Izmenjeni Q I R u slucaju da je neki dijagonalni element negativan")
  #  print(Q)
  #  print(R)
    
    K=LA.inv(R)
  #  print("Matrica K: (Matirca kalibracije):")
  #  print(K)
    A=np.transpose(Q)
    if K[2,2]!=1:
        K=K/K[2,2]
    print("Resenje: (K,A,C)")    
    print("Matrica K:")
    print(K)
    print()
    print("Matrica A:")
    print(A)
    print()
    print("C (tacka kamere):")
    T=np.array(T)
    T=T/K[2,2]
  #  print(T)
    l=T[:, 3]
    c1, c2, c3 =(-1)*LA.solve(T0, l)
    print([c1, c2, c3])
    
ParametriKamere(T)
