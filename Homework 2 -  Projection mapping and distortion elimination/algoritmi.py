import numpy as np
import copy
import numpy.linalg as LA
import matplotlib.pyplot as plt 
import math


#ulaz u algoritam homogene koordinate 4 originalne tacke i
#4 njihove slike ->naivni algoritam daje matricu preslikavanja 
#a.b,c, d u ap, bp, cp, dp
'''
tacke=[[-3, 2, 1],
       [-2, 5, 2],
       [1, 0, 3],
       [-7, 3, 1]]

tacke_projekcije=[[11, -12, 7],
                  [25, -8, 9],
                  [15, 4, 17],
                  [14, -28, 10]]

'''
tacke=[[2, 1, 1],
       [1, 2, 1],
       [3, 4, 1],
       [-1, -3, 1]]

tacke_projekcije=[[0, 0, 1],
                  [5, 0, 1],
                  [2, -5, 1],
                  [-1, -1, 1]]
'''
print("Unesite broj tacaka:")
n=int(input())
print("Unesite koordinate originalnih tacaka:")

tacke=[]
for i in range(n):
    t=list(map(int, input().split()))
    tacke.append(t)

print("Koordinate originalnih tacaka su:")
tacke=np.array(tacke).reshape(n,3)
print(tacke)

print("Unesite koordinate tacaka slike:")
tacke_projekcije=[]
for i in range(n):
    t=list(map(int, input().split()))
    tacke_projekcije.append(t)


print("Koordinate tacaka slike su:")
tacke_projekcije=np.array(tacke_projekcije).reshape(n,3)
print(tacke_projekcije)
'''
print("Koordinate originalnih tacaka su:")
print(tacke)

print("Koordinate tacaka slike su:")
print(tacke_projekcije)

tacke = [[a/c, b/c, 1] for [a,b,c] in tacke]
tacke_projekcije = [[a/c, b/c, 1] for [a,b,c] in tacke_projekcije]

#Ao, Bo, Co, Do                 
bazne_tacke=[[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]]
#f: Ao, Bo, Co, Do -> A, B,C, D
#D=Aalfa+Bbeta+Cgama, alfa, beta, gama su razliciti od nule
def resavanje_sistema(tacke):
    D= np.array([[tacke[0][0], tacke[1][0], tacke[2][0]],
                 [tacke[0][1], tacke[1][1], tacke[2][1]],
                 [tacke[0][2], tacke[1][2], tacke[2][2]]])
    
    D1=np.array([tacke[3][0], tacke[3][1], tacke[3][2]])
    
    alfa, beta, gama =np.linalg.solve(D, D1)
    
    return (alfa, beta, gama)

def matrica_P(tacke, tacke_projekcije):
    (alfa, beta, gama) = resavanje_sistema(tacke)
    
    p1 = np.array([[x*alfa for x in tacke[0]],
                   [x*beta for x in tacke[1]],
                   [x*gama for x in tacke[2]]])
    
    p1 = np.transpose(p1)
    
    (alfap, betap, gamap) = resavanje_sistema(tacke_projekcije)
    p2 = np.array([[x*alfap for x in tacke_projekcije[0]],
                   [x*betap for x in tacke_projekcije[1]],
                   [x*gamap for x in tacke_projekcije[2]]])
 
    p2 = np.transpose(p2)
    
    P =p2.dot(LA.inv(p1))
    
    return (P, alfa, beta, gama)

def naivni_algoritam(tacke, tacke_projekcije):
    P_matrica, alfa, beta, gama = matrica_P(tacke, tacke_projekcije)
    return (P_matrica, alfa, beta, gama)

P_matrica, alfa, beta, gama = naivni_algoritam(tacke, tacke_projekcije)

print()
print('********** NAIVNI ALGORITAM ************')
print('Matrica naivnog algoritma')
print (P_matrica.round(decimals=5))
print()
print("Koeficijenti su:")
print(alfa.round(decimals=2), beta.round(decimals=1), gama.round(decimals=1))
print()

print('Provera za tacku D: ')
D=np.array(tacke[0])*alfa + np.array(tacke[1])*beta + np.array(tacke[2])*gama
print(D)
print()
print()

#DLT algoritam za projektivno preslikavanje
def dlt(tacke, tacke_slike):    
    
    matrica = []
    n = len(tacke)
    for i in range(n):
        matrica.append( [0, 0, 0, 
         -tacke_slike[i][2]*tacke[i][0], -tacke_slike[i][2]*tacke[i][1], -tacke_slike[i][2]*tacke[i][2], 
         tacke_slike[i][1]*tacke[i][0], tacke_slike[i][1]*tacke[i][1], tacke_slike[i][1]*tacke[i][2]])     

        matrica.append([tacke_slike[i][2]*tacke[i][0], tacke_slike[i][2]*tacke[i][1], tacke_slike[i][2]*tacke[i][2],
         0, 0, 0,
         -tacke_slike[i][0]*tacke[i][0], -tacke_slike[i][0]*tacke[i][1], -tacke_slike[i][0]*tacke[i][2]])

#svd, A=UDV^T, bitna nam je jedino matrica V i to njene kolone, jer je tu rezultat
    _, _, V = LA.svd(matrica)
    P_matrica_DLT = V[-1]*(-1)
    return P_matrica_DLT
   
print("******** DLT *******")
P_matrica_DLT = dlt(tacke, tacke_projekcije)
print("Matrica preslikavanja za DLT algoritam sa 4 tacke:")
print(P_matrica_DLT.reshape((3,3)).round(decimals=5))
print()

#Poredjenje sa naivnim, stavljamo u if uslov za slucaj da nam je vrednost 0 
#i da ne bi dobili deljenje 0, posto ne znamo unapred vrednosti, 
#inace treba da se odabere vrednost koja nije 0 pri deljenju i tako za svako poredjenje

P=P_matrica
PM=P_matrica_DLT
if ((PM[0]*P[0][0])!=0):
    print("Poredjenje matrice naivnog i skalirane matrice za DLT algoritam, na 5 decimala")
    M=[(x / PM[0] * P[0][0]) for x in PM]   
    M=np.array(M).reshape(3,3).round(decimals=5)
    print("Zakljucak:")
    print(M)
    print(M.round(decimals=5)==P.round(decimals=5))
    print()

originali=[[2, 1, 1],
           [1, 2, 1],
           [3, 4, 1],
           [-1, -3, 1],
           [-2, 5, 1]]

slike=[[0, 1, 1],
       [5, 0, 1],
       [2, -5, 1],
       [-1, -1, 1],
       [4, 1, 2]]
'''

originali=[[-3, -1, 1],
           [3, -1, 1],
           [1, 1, 1],
           [-1, 1, 1],
           [1, 2, 3],
           [-8, -2, 1]]

slike=[[-2, -1, 1],
       [2, -1, 1],
       [2, 1, 1],
       [-2, 1, 1],
       [2, 1, 4],
       [-16, -5, 4]]

print("Algoritmi primenjeni na vise korespodencija")
print("Unesite broj tacaka:")
m=int(input())
print("Unesite koordinate originalnih tacaka:")

originali=[]
for i in range(m):
    t=list(map(int, input().split()))
    originali.append(t)

print("Koordinate originalnih tacaka su:")
originali=np.array(originali).reshape(m,3)
print(originali)

print("Unesite koordinate tacaka slike:")
slike=[]
for i in range(m):
    t=list(map(int, input().split()))
    slike.append(t)

print("Koordinate tacaka slike su:")
slike=np.array(slike).reshape(m,3)
print(slike)
print()
'''
print("Koordinate originalnih tacaka su:")
print(originali)

print("Koordinate tacaka slike su:")
print(slike)
print()

originali = [[a/c, b/c, 1] for [a,b,c] in originali]
slike = [[a/c, b/c, 1] for [a,b,c] in slike]

P_DLT = dlt(originali, slike)
print("Matrica preslikavanja za DLT algoritam sa vise tacaka:")
print(P_DLT.reshape((3,3)).round(decimals=5))
print()

M1=P_matrica_DLT.reshape((3,3)).round(decimals=6)
M2=P_DLT.reshape((3,3)).round(decimals=6)
print("!!!!!!!!!!!!!!!!")
print("Poredjenje matrica dlt sa 4 i vise korespodencija")
print(M1)
print()
print(M2)
print("Zakljucak:")
print("Dobijeno projektivno preslikavanje nije isto kao ono sa 4 tacke, ali je priblizno!")
print("!!!!!!!!!!!!!!!!")
print()
P_matrica,_,_,_=naivni_algoritam(originali,slike)
P=P_matrica
PM=P_DLT
if (PM[0]*P[0][0]!=0):
    print("Poredjenje matrica naivnog i skaliranog DLT algoritma, na 5 decimala")
    M=[(x / PM[0] * P[0][0]) for x in PM]
    M=np.array(M).reshape(3,3).round(decimals=5)    
    print("Zakljucak:")
    print(M)
    print(M.round(decimals=5)==P.round(decimals=5))
    print()

#normalizacija tacaka
def normalizacija(tacke):
    x = 0.0
    y = 0.0

    udaljenost = 0.0

    for i in range(len(tacke)):
        x = x + float(tacke[i][0]) / float(tacke[i][2])
        y = y + float(tacke[i][1]) / float(tacke[i][2])

    #x i y su afine koordinate tezista tacaka
    x = x / float(len(tacke))
    y = y / float(len(tacke))

    for i in range(len(tacke)):
       
        tmp1 = tacke[i][0]/tacke[i][2] - x
        tmp2 = tacke[i][1]/tacke[i][2] - y

        udaljenost = udaljenost + math.sqrt(tmp1**2 + tmp2**2)

    udaljenost = udaljenost / float(len(tacke))

    k = math.sqrt(2) / udaljenost 

    S = np.array([[k, 0, -k*x], [0, k, -k*y], [0, 0, 1]])

    return S

def dlt_normalizacija(originali, slike):

    #matrice T i Tp su matrice normalizacije originalnih tacaka i njihovih slika
    T = normalizacija(originali)
    Tp = normalizacija(slike)

    #kopije originalnih tacaka i njihovih slika
    originali_copy = copy.deepcopy(originali)
    slike_copy = copy.deepcopy(slike)

    for i in range(len(originali)):
        #normalizacija originalnih tacaka
        [x, y, z] = np.dot(T, [originali[i][0], originali[i][1], originali[i][2]])

        originali_copy[i][0] = float(x) 
        originali_copy[i][1] = float(y)
        originali_copy[i][2] = float(z)

    for i in range(len(slike)):
        #normalizacija slika
        [x, y, z] = np.dot(Tp, [float(slike[i][0]), float(slike[i][1]), float(slike[i][2])])

        slike_copy[i][0] = float(x) 
        slike_copy[i][1] = float(y)
        slike_copy[i][2] = float(z)

    #primena DLT algoritma na normalizovane originalne tacke i njihove slike
    Pp = dlt(originali_copy, slike_copy)
    Pp=Pp.reshape((3,3))

    #odgovarajuca matrica preslikavanja
    P = np.dot(LA.inv(Tp), Pp)
    P = np.dot(P, T)

    return P
     
rezultat= dlt_normalizacija(originali, slike)
print("******* DLT NORMALIZOVANI ******")
print()
print("Za vise korespodencija:")
print()
print("Matrica dobijena DLT normalizovanim algoritmom za vise tacaka: ")
print(rezultat.round(decimals=5))
print()

#Reskaliramo i uporedimo sa matricom dobijenom pre promene koordinata
Pndlt=rezultat.flatten()
P,_,_,_ =naivni_algoritam(originali, slike)
if ((Pndlt[0] * P[0][0])!=0):
    print("Poredjenje matrica naivnog i normalizovanog DLT, na 5 decimala")
    M=[(x / Pndlt[0] * P[0][0]) for x in Pndlt]
    M=np.array(M).reshape((3,3)).round(decimals=5)
    print("Zakljucak:")
    print(M)
    print(M.round(decimals=5)==P.round(decimals=5))

print()
print("!!!!!!!!!!!!!!!")
Pndlt=rezultat.flatten()
P=dlt(originali, slike).reshape((3,3))
if ((Pndlt[0] * P[0][0])!=0):
    print("Poredjenje matrica dlt i normalizovanog DLT, na 6 decimala")
    M=[(x / Pndlt[0] * P[0][0]) for x in Pndlt]
    M=np.array(M).reshape((3,3)).round(decimals=6)
    print(M)
    print()
    print(P.round(decimals=6))
    print("Zakljucak:")
    print("Vidimo da se matrice razlikuju vec na drugoj decimali.")
print("!!!!!!!!!!!!!!!!")
   
def test_dlt(tacke, tacke_slike):
   #matrice T i Tp su matrice normalizacije originalnih tacaka i njihovih slika
    T=np.array([[0,1,2],[-1,0,3],[0,0,1]]).reshape((3,3))
    Tp=np.array([[1,-1,5],[1,1,-2],[0,0,1]]).reshape((3,3))
    
    #Normalizacija tacaka i njihovih slika
    tacke=np.transpose(tacke)
    tacke_slike=np.transpose(tacke_slike)
    
    tackeN=np.transpose(T.dot(tacke))
    tacke_slikeN=np.transpose(Tp.dot(tacke_slike))
    
    #Primena dlt algoritma na normalizovane tacke i slike
    dlt_mat=dlt(tackeN, tacke_slikeN)
    dlt_mat=np.array(dlt_mat).reshape((3,3))
    
    #return dlt_mat
    #4. P=T'^-1P^-T
    rezultat=  (LA.inv(Tp)).dot(dlt_mat).dot(T)
    return (rezultat, dlt_mat)

print()
print("!!!!!!!!!!!!!!!!!!!!!!!!")
print("Proveravamo da li je rezultat DLT algoritma primenjenog\n na nove koordinate, isti kao rezultat starog u novim koordinatama ")
novi, stari=test_dlt(originali, slike)
print(novi)
print()
print(stari)
R=[(x / novi[0] * stari[0][0]) for x in novi]
R=np.array(M).reshape((3,3)).round(decimals=6)
print()
print("DLT")
print(M2)
print()
print("Reskalirana, na novim koordinatama")
print(R)
print()
print("Zakljucak: Vidimo da se na drugoj decimali pojavljuje razlika.\nDLT algoritam nije invarijantan u odnosu na promenu koordinata, \ntj. nije geometrijski!")
print("!!!!!!!!!!!!!!!!!!!!!!!!")
print()

def test_dlt_norm(tacke, tacke_slike):
   #matrice T i Tp su matrice normalizacije originalnih tacaka i njihovih slika
    T=np.array([[0,1,2],[-1,0,3],[0,0,1]]).reshape((3,3))
    Tp=np.array([[1,-1,5],[1,1,-2],[0,0,1]]).reshape((3,3))
    
    #Normalizacija tacaka i njihovih slika
    tacke=np.transpose(tacke)
    tacke_slike=np.transpose(tacke_slike)
    
    tackeN=np.transpose(T.dot(tacke))
    tacke_slikeN=np.transpose(Tp.dot(tacke_slike))
    
    #Primena dlt algoritma na normalizovane tacke i slike
    dlt_mat=dlt_normalizacija(tackeN, tacke_slikeN)
    dlt_mat=np.array(dlt_mat).reshape((3,3))
    
    #return dlt_mat
    #4. P=T'^-1P^-T
    rezultat=  (LA.inv(Tp)).dot(dlt_mat).dot(T)
    return (rezultat, dlt_mat)
print("!!!!!!!!!!!!!!!!!!!!!!!!")
print("Modifikovani DLT algoritam - poredjenje sa DLT algoritmom\n i invarijantnost u odnosu na transformaciju koordinata!")

rez, d=test_dlt_norm(originali, slike)
mdlt=dlt_normalizacija(originali, slike)
#Proveravamo da li je rezultat modifkovanog DLP algoritma primenjenog na nove koordinate, isti kao rezultat starog u novim koordinatama
print(rez.round(decimals=6))
print()
print(mdlt.round(decimals=6))
print()
print(rez.round(decimals=6)==mdlt.round(decimals=6))
print()
print("Zakljucak: Matrice su iste, tj. modifikovani DLT ne zavisi od izbora koordinata!")
print("!!!!!!!!!!!!!!!!!!!!!!!!")
print()

