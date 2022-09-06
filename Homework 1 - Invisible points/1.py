def afina_tacka(tacka):
    print("T4(" + str(round(tacka[0]/tacka[2])) + ", " + str(round(tacka[1]/tacka[2])) + ")")
 
def vektorski_proizvod(t1, t2):
    x = t1[1] * t2[2] - t1[2] * t2[1];
    y = t1[2] * t2[0] - t1[0] * t2[2];
    z = t1[0] * t2[1] - t1[1] * t2[0];
    return (x, y, z)

def nevidljiva_tacka(T1, T2, T3, T5, T6, T7, T8):
    t1=(T1[0], T1[1], 1)
    t2=(T2[0], T2[1], 1)
    t3=(T3[0], T3[1], 1)
    t5=(T5[0], T5[1], 1)
    t6=(T6[0], T6[1], 1)
    t7=(T7[0], T7[1], 1)
    t8=(T8[0], T8[1], 1)
    
    x_beskonacno=vektorski_proizvod(vektorski_proizvod(t1, t5), vektorski_proizvod(t2, t6))
    y_beskonacno=vektorski_proizvod(vektorski_proizvod(t5, t8), vektorski_proizvod(t6, t7))
    return vektorski_proizvod(vektorski_proizvod(x_beskonacno, t8), vektorski_proizvod(y_beskonacno, t1))

T1=(515, 330);
T2=(661, 461);
T3=(887, 245);
T5=(471, 188);
T6=(644, 311);
T7=(905, 108);
T8=(740, 59);   
T4=nevidljiva_tacka(T1, T2, T3, T5, T6, T7, T8)
afina_tacka(T4)


    
