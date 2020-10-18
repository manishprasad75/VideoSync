from django.shortcuts import render
from django.http import HttpResponse
from .forms import FileForm
from .models import File
# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello, World</h1>")

def allVideo(request):
    context = {
        'videos': File.objects.all()
    }
    return render(request, "showpage.html", context)


def showfile(request):

    if request.method == 'POST':
        form = FileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        context = {
            'videos': File.objects.all()
        }
    
        return render(request, "showpage.html", context)


    lastfile= File.objects.last()

    filepath= lastfile.filepath

    filename= lastfile.name


    form= FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    
    context= {'filepath': filepath,
              'form': form,
              'filename': filename
              }
    
      
    return render(request, 'updateform.html', context)
