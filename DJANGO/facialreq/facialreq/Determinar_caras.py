import pandas
import pickle
from sklearn.decomposition import PCA
import numpy
import os
from .settings import *


from .facialReqNS import *

def Similiarity(a,b):
  return numpy.linalg.norm(a-b)

Similiarity(numpy.asarray([1,2,3]),numpy.asarray([1,2,3]))

def conestojala():
  img_path = os.path.join(PROJECT_ROOT, "..\images\image.jpg")
  #print(img_path)
  I = cv2.imread(img_path)
   # Leer la imagen de la foto
  AR = 480 / I.shape[1] # Aspect Ratio
  width = int(I.shape[1] * AR)
  height = int(I.shape[0] * AR)
  # Reescalamiento
  I = cv2.resize(I, (width,height), interpolation = cv2.INTER_AREA)
  cv2.imwrite("temp.jpg", I)
  # Guardar archivo temporal de la imagen guardada
  FID = face_recognition.load_image_file("temp.jpg") # carga de imagen reescalada
  Locations = face_recognition.face_locations(FID)
  FaceVectors = face_recognition.face_encodings(FID, Locations)
  xr = FaceVectors[0]

  # Leemos el dataset ya codificado
  csvurl = os.path.join(PROJECT_ROOT, "Faces.csv")
  DF = pandas.read_csv(csvurl)
  filtered_df = DF[DF['File'].str.contains('A01369422')]
  xq = numpy.asarray(DF.iloc[[9],1:])[0]
  DF = DF.drop([9]) 
  DF = DF.reset_index(drop =True)

  # Extraer la matriz de diseño del dataframe
  X = numpy.asarray(DF.iloc[:,1:])

  # carga del modelo

  modelurl = os.path.join(PROJECT_ROOT, "PCAModel.p")
  Model = pickle.load( open( modelurl, "rb" ) )

  X_hat = Model.transform(X);

  xq = Model.transform(xr.reshape(1, -1))

  Sim = [] # Arreglo de similitud


  for xi in X_hat:
    sim = Similiarity(xq, xi)
    Sim.append(sim)

  Sim = numpy.asarray(Sim)

  Idx = numpy.argsort(Sim)

  print(DF.iloc[Idx[:5]])

  #El valor de la imagen mas parecida
  #print(Sim[Idx[0]])
  #print(Sim)
  resu = (Sim[Idx[0]]/(Sim[Idx[43]]))*100

  resultadobien= 100-resu
  print("Resultado :",resultadobien,"%")

  if resultadobien > 90:
    m = "Te la creo, identificación aprobada"
  else:
    m = "No son los mismos, Denegado"

  print(m)
  resultadobien = int(resultadobien)
  return resultadobien, m

conestojala()