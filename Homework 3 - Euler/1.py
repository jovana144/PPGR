import numpy as np
import numpy.linalg as LA
import math
import sys

def Euler2A(phi, theta, psi):
    Rx=np.array([[1, 0, 0],
                [0, math.cos(phi), -math.sin(phi)],
                [0, math.sin(phi), math.cos(phi)]])
        
    Ry=np.array([[math.cos(theta), 0, math.sin(theta)],
                [0, 1, 0],
                [-math.sin(theta), 0, math.cos(theta)]])
        
    Rz=np.array([[math.cos(psi), -math.sin(psi), 0],
                [math.sin(psi), math.cos(psi), 0],
                [0, 0, 1]])
        
    return Rz.dot(Ry).dot(Rx)    
       
def AxisAngle(A):
    if (A == np.eye(3)).all() or round(LA.det(A))!=1:
        sys.exit("Matrica A je jedinicna ili joj je determinanta razlicita od 1!")
        
    #Racunanje sopstvenih vrednosti i vektora
    lambdaa,vector=LA.eig(A, );
    for i in range(len(lambdaa)):
        if round(lambdaa[i], 6)==1.0:
            p=np.real(vector[:, i])
            
    p1=p[0]
    p2=p[1]
    p3=p[2]  
    
    u=np.cross(p, np.array([p1, p2, -p3]))
    u = u/math.sqrt(u[0]**2 + u[1]**2+u[2]**2)
    
    up=A.dot(u)
    
    fi=round(math.acos(np.sum(u*up)), 5)
    if round(np.sum(np.cross(u, up)*p), 5) < 0:
        p=(-1)*p
        
    return [p, fi]
    
def Rodrigez(p, fi):
    if round(LA.norm(p))!=1:
        norm_p=LA.norm(p)
        if norm_p != 0:
            p= p / norm_p    
     
    p1 = p[0]
    p2 = p[1]
    p3 = p[2]
     
    # Formula Rodrigeza:
    # Rp(fi) = p*p_t + cos(fi)*(E - p*p_t) + sin(fi)*px
    
    pp_t=np.reshape(p, (3,1)).dot(np.reshape(p, (1,3)))
    px = np.array([
        [0, -p3, p2],
        [p3, 0, -p1],
        [-p2, p1, 0]
        ])
    
    Rp=pp_t + math.cos(fi)*(np.eye(3)-pp_t)+math.sin(fi)*px
    return Rp

def A2Euler(A):
    if round(LA.det(A))!=1: 
        sys.exit("Matrica A nije ortogonalna!")

    A=np.array(A)
    fi, teta, psi=0,0,0
    if A[2,0]<1:
        if A[2,0]>-1:
            psi=math.atan2(A[1,0], A[0,0]) 
            teta=math.asin((-1)*A[2,0])
            fi=math.atan2(A[2,1], A[2,2])
        else:   
            psi=math.atan2((-1)*A[0,1], A[1,1])
            teta=math.pi/2.0
            fi=0.0
    else:
        psi=math.atan2((-1)*A[0,1], A[1,1])
        teta=(-1.0)*math.pi/2.0
        fi=0
        print(A)

    return fi, teta, psi           
          
def AxisAngleQ2(p, phi):
    if phi==0:
        return 1;
        
    w = math.cos(phi/2.0)
    norm = LA.norm(p)
    if norm !=0:
        p =p/norm
    [x, y, z]=math.sin(phi/2.0)*p
    return [x, y, z, w]
            
            
def Q2AxisAngle(q):
    norm = LA.norm(q)
    if norm !=0:    
        q=q/norm
        
    fi = 2*math.acos(q[3])
    if abs(q[3])==1:
        p=[1, 0, 0]   
    else:
        norm = LA.norm(np.array([q[0], q[1], q[2]]))
        p=np.array([q[0], q[1], q[2]])
        if norm != 0:
            p = p / norm
            
    return [p, fi]

#phi=-math.atan(1/4)
#teta=-math.asin(8/9)
#psi=math.atan(4)

phi=-math.pi / 3
teta=-math.pi / 3
psi=math.pi /4


print()
print("Polazni Ojlerovi uglovi fi, teta, psi:") 
print(phi, teta, psi)
print("Polazni Ojlerovi uglovi u stepenima:")
print(round(phi/math.pi*180), round(teta/math.pi*180), round(psi/math.pi*180))
                      
print()          
print("--------Euler2A----------")
print("Matrica A = Rz(psi)Ry(teta)Rx(fi):")
A = Euler2A(phi, teta, psi)
print(A.round(decimals=5))

print()
print("--------AxisAngle---------")
p, fi =AxisAngle(A)
print("Vektor p: ", p)
print("Ugao fi: ", fi)
print("Ugao fi u stepenima: ", round(fi / math.pi*180))
       
        
print()
print("--------Rodrigez---------")  
print("Matrica rotacije:") 
Rp = Rodrigez(p, fi)
print(Rp.round(decimals=5))

print()
print("--------A2Euler------------")
print("Ojlerovi uglovi phi, teta, psi:")
phi, teta, psi=A2Euler(A)
print(phi, teta, psi)
print("Ojlerovi uglovi phi, teta, psi u stepenima:")
print(round(phi/math.pi*180), round(teta/math.pi*180), round(psi/math.pi*180))

print()
print("--------AxisAngleQ2---------")
q=AxisAngleQ2(p, fi)
print("Kvaternion: ", q)

print()
print("--------Q2AxisAngle----------")
p, fi=Q2AxisAngle(q)
print("Vektor p: ", p)
print("Ugap fi: ", fi)
print("Ugap fi u stepenima: ", round(fi/math.pi*180))
print()
