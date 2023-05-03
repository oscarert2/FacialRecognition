from django.shortcuts import render
import base64
from django.http import JsonResponse


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