import pandas
import pickle
from sklearn.decomposition import PCA
import numpy

from facialReqNS import *

def Similiarity(a,b):
  # metrica de similitud
  # depende de la naturaleza del manifold
  # puede ser que se haga pequeña (caso L2) o se haga grande (caso Producto interno)
  # Tarea: tener varias metricas en esta funcion para seleccionar una
  return numpy.linalg.norm(a-b)

Similiarity(numpy.asarray([1,2,3]),numpy.asarray([1,2,3]))


I = cv2.imread("../images/image.jpg") # Leer la imagen de la foto
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

print(xr)




# Leemos el dataset ya codificado
DF = pandas.read_csv("Faces.csv")
filtered_df = DF[DF['File'].str.contains('A01369422')]
# Demostracion la cara de el renglon 9
#print(DF.loc[[9], "File"])
# Demostracion el vector de la cara 8
xq = numpy.asarray(DF.iloc[[9],1:])[0]
# Elimino de la base de datos la cara a buscar
DF = DF.drop([9]) # Quita la cara de la persona a buscar
# Reset a los indices
DF = DF.reset_index(drop =True)

# Extraer la matriz de diseño del dataframe
X = numpy.asarray(DF.iloc[:,1:])

# carga del modelo

Model = pickle.load( open( "PCAModel.p", "rb" ) )

X_hat = Model.transform(X);




#print(X_hat)
#print(X)
xq = Model.transform(xr.reshape(1, -1))

#print("xq")
#print(xq)

Sim = [] # Arreglo de similitud

# Tarea quitar este ciclo for de las lineas 24 - 31 (Participacion)

for xi in X_hat:
  sim = Similiarity(xq, xi)
  Sim.append(sim)

Sim = numpy.asarray(Sim)

Idx = numpy.argsort(Sim)

print(DF.iloc[Idx[:5]])

#print(Idx)


#El valor de la imagen mas parecida
print(Sim[Idx[0]])

resu = 100 - Sim[Idx[0]]

print("Resultado :",resu,"%")

