from django.shortcuts import render
import base64
from django.http import JsonResponse
from .Determinar_caras import *
from .settings import *


def home(request):
    return render(request, 'base.html')

def save_image(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data', '')
        image_data = image_data.replace('data:image/jpeg;base64,', '')
        image_data = base64.b64decode(image_data)

        with open('./images/image.jpg', 'wb') as f:
            f.write(image_data)

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})


def my_view(request):
    if request.method == 'POST':
        text_input_value = request.POST.get('my_text_input')
        # Do something with the text input value
        with open('./mat/mat.txt', 'wb') as f:
            f.write(text_input_value.encode())

        return render(request, 'base.html')
    else:
        return JsonResponse({'success': False})
    
    
def results(request):

    r, m = conestojala()
    print(r)

    return render(request, 'results.html', {"r":r , "m":m}  )


