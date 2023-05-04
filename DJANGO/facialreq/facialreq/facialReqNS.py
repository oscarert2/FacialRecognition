from IPython.lib.display import FileLinks
import pandas
import numpy
import cv2
import face_recognition
import glob
from matplotlib import pyplot

# Esto solo se hace una vez en el BackEnd

def DesignMatrix(Options):
  SPath = Options.SPath # Source path todas las imagenes
  #Files = glob.glob(SPath + "**/**.jpg")
  Files = glob.glob("face_imgs/TC3002B_Faces/*/*.jpg")
  OutFile = Options.OutFile # Nombre del archivo de salida en CSV
  X = [] # Matriz de diseño vacia
  L = [] # Etiquetas de a quien pertenece la fotografia
  for File in Files:
    # Leer la imagen de la cara y guardala en la matrix X como un vector
    #x = numpy.random.rand(512);
    try:
      x = Image2Vector(File)
    except:
      continue
    X.append(x)
    L.append(File)
    print(File)

  DF = pandas.DataFrame(X)
  DF.insert(0,"File",L)
  DF.to_csv(Options.OutFile, index = False)

def Image2Vector(File):
  I = cv2.imread(File) # Leer la imagen de la foto
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
  x = FaceVectors[0]
  return x

def Similiarity(a,b):
  return numpy.linalg.norm(a-b)


# Llamada de la function para generar la matriz de diseño

class Opt:
  pass

Options = Opt

Options.SPath = "TC3002B_Faces/"
Options.OutFile = "Faces.csv"

DesignMatrix(Options)




