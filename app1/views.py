from django.shortcuts import render

# Create your views here.
def STATIC(request):
    return render(request,'static.html')