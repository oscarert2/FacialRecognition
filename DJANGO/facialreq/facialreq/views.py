from django.shortcuts import render
from .forms import UploadForm

def home(request):
    return render(request, 'base.html', context)
    form = UploadForm(request.POST or None, request.FILES or None)
    context= { 'form': form ,}
