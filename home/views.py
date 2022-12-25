from django.http import HttpResponse
from django.shortcuts import render

from Library.models import Category,Library


# Create your views here.
def index(request):
    category = Category.objects.all()
    sliderdata = Library.objects.all().order_by('?')[0:6]
    newLibrary= Library.objects.order_by('-create_at')[0:4]
    context={'category': category,'sliderdata':sliderdata,'newLibrary':newLibrary}

    return render(request,'index.html',context)
