#Pri pokretanju programa ispisuju se rezultati za vec unesene
#tacke, ako zelite da testirane na nekim drugim koordinatama
#mozete odkomentarisati deo za unos tacaka sa standardnog ulaza i
# tu uneti zeljene koordinate
# zatim se unosi slika, vrsi se otklanjanje projektivne distorzije
from tkinter import *
from tkinter import filedialog
import PIL.Image
import sys
import numpy as np
import numpy.linalg as LA
from algoritmi import dlt_normalizacija
import math

HEIGHT=500
WIDTH =500

root = Tk()
root.title("Otklanjane distorzije!")


def ucitaj():
    #odabir i prikaz slike
    filename = filedialog.askopenfilename()

    global image 

    image = PIL.Image.open(filename)
    image.show()
    
    global dimensions
    dimensions=image.size
    
    print('Dimenzije ucitane slike:')
    print(dimensions)
    
    frame1=Frame(root, bg='pink')
    frame1.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.35)
    
    labelUnesi = Label(frame1, bg='pink',text="Unesite 4 piksela sa slike\n koji ce da se slikaju u pravougaonik:", font=40)
    labelUnesi.grid(row=1)
    
    tackeE = []

    for i in range(4):
        e = Entry(frame1, bg='pink')
        tackeE.append(e)
        tackeE[i].grid(row=i+2)
    
    def otkloniDistorziju():
        tacke = []
   
        #odabrane tacke na slici
        for i in range(4):
            x = float(tackeE[i].get().strip().split(' ')[0])
            y = float(tackeE[i].get().strip().split(' ')[1])

            tacke.append([x, y, 1])

        #izracunavanje koordinata pravougaonika u cija temena treba da se preslikaju odabrane tacke na slici
        slike = []
        
        #AD i BC predstavljaju duzinu ili sirinu odabranog cetvorougla
        A=tacke[0]
        B=tacke[1]
        C=tacke[2]
        D=tacke[3]
        
        AD = math.sqrt((A[0]-D[0])**2 + (A[1]-D[1])**2)
        BC = math.sqrt((B[0] - C[0])**2 + (B[1] - C[1])**2)

        #sirina pravougaonika je aritmeticka sredina sirina stranica originalnog cetvorougla
        sirina = round((AD+BC)/2)

        AB = math.sqrt((A[0]-B[0])**2 + (A[1]+B[1])**2)
        DC = math.sqrt((D[0]-C[0])**2 + (D[1] - C[1])**2)

        #duzina pravougaonika je aritmeticka sredina duzina stranica originalnog cetvorougla
        duzina = round((AB+DC)/2)

        s1 = dimensions[1] - sirina
        s1 = round(s1/2)

        s2 = dimensions[0] - duzina
        s2 = round(s2/2)

        slike.append([s2, s1, 1])
        slike.append([dimensions[0]-s2, s1, 1])
        slike.append([dimensions[0]-s2, dimensions[1]-s1, 1])
        slike.append([s2, dimensions[1]-s1, 1])

        #matrica preslikavanja uz pomoc modifikovanog DLT algoritma
        P = dlt_normalizacija(tacke, slike)

        #racunanje inverza dobijenog preslikavanja
        P_inv = LA.inv(P)

        #izdvajanje piksela ucitane slike
        old_pixels = image.load()

        #otvaranje nove slike koja je na pocetku crna
        image_new = PIL.Image.new("RGB", dimensions, "#000000")
        new_pixels = image_new.load()

        #prolazenje kroz sve piksele 
        #za svaki piksel (i, j) se racuna piksel koji se sa originalne slike preslikava u njega
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                coordinates = np.dot(P_inv, [i, j, 1])

                x = round(coordinates[0]/coordinates[2])
                y = round(coordinates[1]/coordinates[2])
                
                #ako su koordinate piksela van originalne slike on ostaje crn,inace se piksel postavlja na vrednost dobijenog piksela
                if (x < 0 or x >= dimensions[0]):
                    continue
                elif (y < 0 or y >= dimensions[1]):
                    continue
                else:
                    new_pixels[i, j] = old_pixels[x, y]
                    

        #cuvanje i prikazivanje slike sa otklonjenom disperzijom
        image_new.save("ispravljena_slika.bmp")
        image_new.show()

    buttonOk = Button(frame1, text="OK", command=otkloniDistorziju)
    buttonOk.grid(row=6)

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#Uklonjena slika za pozadinu, zbog velicine i problema pri slanju na rcub
background_label=Label(root, bg='purple')
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame=Frame(root, bg='black', bd=5)
frame.place(relx=0.33, rely=0.2, relwidth=0.3, relheight=0.1)

buttonUcitaj=Button(frame, bg='pink', text="Ucitaj sliku", font=40, command=ucitaj)
buttonUcitaj.place(relx=0.02, rely=0.06, relwidth=0.95, relheight=0.9)

root.mainloop()
