from tkinter import *
from PIL import ImageTk
from PIL import Image
import imutils
import cv2
import os
import ReconocimientoFacial
import AgregarPersona
import entrenamiento

def iniciar():
    global cap
    cap = cv2.VideoCapture(0)
    visualizar()
    
def visualizar():
    global cap
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width=912)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Dibujando un rectángulo por cada rostro detectado
            faces = face_cascade.detectMultiScale(frame, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.putText(frame, 'Persona', (x,y-20), 2,0.8, (0,255,0), 2, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, visualizar)
        else:
            lblVideo.image = ""
            cap.release()

def finalizar():
    global cap
    cap.release()

def viewReconocimiento():
    ReconocimientoFacial.reconocimeinto(ventana)

def addPersona():
    #mb.showinfo("Información", "texto uwu")
    emergente = Tk()
    emergente.title("Nombre completo")
    lbl = Label(emergente,text='Nombre completo de la persona')
    caja = Text(emergente, height = 5, width = 52)
    accept_button = Button(emergente,text='Aceptar', command=lambda: agregar(caja, emergente))
    lbl.pack(ipadx=5,ipady=5,expand=True)
    caja.pack(ipadx=5,ipady=5,expand=True)
    accept_button.pack()
    emergente.mainloop()

def verPersonas():
    per = Tk()
    per.title("Nombre completo")
    msj = Label(per,text='Nombre completo de la personas registradas')
    msj.pack(ipadx=5,ipady=5,expand=True)
    dataPath = 'Personas'
    imagePaths=os.listdir(dataPath)
    print('Personas Registradas=',imagePaths)
    nombres = Label(per,text=imagePaths)
    nombres.pack(ipadx=5,ipady=5,expand=True)
    per.mainloop()

def agregar(caja, emergente):
    nombre = caja.get("1.0","end-1c")
    nombre = nombre.strip()
    print(nombre)
    AgregarPersona.newPersona(nombre, emergente)

def entrenar():
    entrenamiento.entrenar()

def initGUI():
    menubar = Menu(ventana)
    width = 910
    height = ventana.winfo_screenheight() 
    ventana.geometry("%dx%d" % (width, height))
    ventana.title("Proycto Final IA")
    ventana.config(menu=menubar)

    # Menú Interfaz
    intmenu = Menu(menubar, tearoff=0)
    intmenu.add_command(label="Iniciar Interfaz Principal", command=iniciar)
    intmenu.add_command(label="Detener Interfaz Principal", command=finalizar)
    intmenu.add_separator()
    intmenu.add_command(label="Iniciar Interfaz de Reconocimiento Entrenada", command=viewReconocimiento)
    intmenu.add_separator()
    intmenu.add_command(label="Salir", command=ventana.destroy)

    # Menú Personas
    personmenu = Menu(menubar, tearoff=0)
    personmenu.add_command(label="Agregar Persona", command=addPersona)
    personmenu.add_command(label="Ver personas", command=verPersonas)
    personmenu.add_separator()
    personmenu.add_command(label="Eliminar Persona")

    # Menú Entrenamiento
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Entrenar", command=entrenar)
    editmenu.add_separator()
    editmenu.add_command(label="Reiniciar entrenamiento!")

    # Menú Ayuda
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Ayuda")
    helpmenu.add_separator()
    helpmenu.add_command(label="Acerca de...")

    # Todos los menús
    menubar.add_cascade(label="Interfaz", menu=intmenu)
    menubar.add_cascade(label="Personas", menu=personmenu)
    menubar.add_cascade(label="Entrenamiento", menu=editmenu)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)
    menubar.add_command(label="Salir", command=ventana.destroy)

# CODE
global cap
ventana = Tk()
initGUI()

# Label con transmision de la camara en tiempo real
lblVideo = Label(ventana)
lblVideo.grid(column=0, row=1, columnspan=2)
#iniciar()

# Bucle de la aplicación
ventana.mainloop()