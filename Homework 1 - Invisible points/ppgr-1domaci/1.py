#Funkcija afine koja homogene koordinate pretvara u afine 
def afine(t):
    print("T4(" + str(round((t[0])/(t[2]))) +", " + str(round(t[1]/t[2])) + ")")
       
#Funkcija vektorski_proizvod koja racuna vektorski proizvod na osnovu formule ako su nam dati vektori sa svojim koordinatama
def vektorski_proizvod(p1, p2):
    x=p1[1]*p2[2]-p1[2]*p2[1]
    y=p1[2]*p2[0]-p1[0]*p2[2]
    z=p1[0]*p2[1]-p1[1]*p2[0]
    
    return (x, y, z)
    
#Funkcija nevidljivo koja nalazi koordinate T4 nevidljivog temena
def nevidljivo(T1, T2, T3, T5, T6, T7, T8): 
    t1=(T1[0], T1[1], 1)
    t2=(T2[0], T2[1], 1)
    t3=(T3[0], T3[1], 1)
    t5=(T5[0], T5[1], 1)
    t6=(T6[0], T6[1], 1)
    t7=(T7[0], T7[1], 1)
    t8=(T8[0], T8[1], 1)
   
    x_beskonacno=vektorski_proizvod(vektorski_proizvod(t2,t6),
        vektorski_proizvod(t1,t5))
   
    y_beskonacno=vektorski_proizvod(vektorski_proizvod(t5,t6),
        vektorski_proizvod(t7,t8))
   
    return vektorski_proizvod(vektorski_proizvod(t8, x_beskonacno), vektorski_proizvod(t3,y_beskonacno))
   
 
T1=(162, 404)
T2=(678, 765)
T3=(894, 466)
T5=(92, 198)
T6=(705, 520)
T7=(958, 248)
T8=(392, 88)   

T4=nevidljivo(T1, T2, T3, T5, T6, T7, T8)
afine(T4)

