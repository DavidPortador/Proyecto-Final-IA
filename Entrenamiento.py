from tkinter import messagebox
import cv2
import os
import numpy as np

# Crea un modelo entrenado con los rostros agregados
def entrenar():
	dataPath = 'Personas'
	peopleList = os.listdir(dataPath)
	print('Lista de personas: ', peopleList)
	labels = []
	facesData = []
	label = 0
	for nameDir in peopleList:
		personPath = dataPath + '/' + nameDir
		print('Leyendo las imágenes')

		for fileName in os.listdir(personPath):
			print('Rostros: ', nameDir + '/' + fileName)
			labels.append(label)
			facesData.append(cv2.imread(personPath+'/'+fileName,0))
		label = label + 1
	face_recognizer = cv2.face.LBPHFaceRecognizer_create()
	# Entrenando el reconocedor de rostros
	print("Entrenando...")
	face_recognizer.train(facesData, np.array(labels))
	# Almacenando el modelo obtenido
	face_recognizer.write('Modelos/modeloLBPHFace.xml')
	print("Modelo almacenado...")
	messagebox.showinfo(message="La creación del modelo de entrenamiento se creo exitosamente!", title="Entrenamiento")