from django.http import HttpResponse
from django.shortcuts import render

from Library.models import Category


# Create your views here.
def index(request):
    category = Category.objects.all()
    context={'category': category}
    return render(request,'index.html',context)
