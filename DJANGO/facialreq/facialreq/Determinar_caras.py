import pandas
import pickle
from sklearn.decomposition import PCA
import numpy

def Similiarity(a,b):
  # metrica de similitud
  # depende de la naturaleza del manifold
  # puede ser que se haga pequeña (caso L2) o se haga grande (caso Producto interno)
  # Tarea: tener varias metricas en esta funcion para seleccionar una
  return numpy.linalg.norm(a-b)

Similiarity(numpy.asarray([1,2,3]),numpy.asarray([1,2,3]))

# Leemos el dataset ya codificado
DF = pandas.read_csv("Faces.csv")
# Demostracion la cara de el renglon 9
print(DF.loc[[9], "File"])
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

xq = Model.transform(xq.reshape(1, -1))

Sim = [] # Arreglo de similitud

# Tarea quitar este ciclo for de las lineas 24 - 31 (Participacion)

for xi in X_hat:
  sim = Similiarity(xq, xi)
  Sim.append(sim)

Sim = numpy.asarray(Sim)

Idx = numpy.argsort(Sim)

print(DF.iloc[Idx[:5]])

