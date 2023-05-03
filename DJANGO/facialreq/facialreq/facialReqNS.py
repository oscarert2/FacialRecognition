import glob
from matplotlib import pyplot
import skimage
import numpy

Files = glob.glob("D:\Github_desktop\FacialRecognition\DJANGO\facialreq\face_imgs\TC3002B_Faces/*/*.jpg")

fig, ax = pyplot.subplots(4,5, figsize = [9,6] );

ny = 600;

print(len(Files))

for k in range(ax.size):
    if k < len(Files):
        I = skimage.io.imread(Files[k])
        nx = I.shape[1]/I.shape[0] * ny 
        I = skimage.transform.resize(I, (ny,nx))
        j = k // ax.shape[0]
        i = k % ax.shape[0]
        ax[i,j].imshow(I)
        ax[i,j].axis("off")
        ax[i,j].set_title(Files[k].split("/")[1])

pyplot.show()
