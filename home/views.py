from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    text="merhaba dunya"
    context={'text':text}
    return render(request,'index.html',context)