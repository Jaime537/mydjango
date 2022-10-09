from django.shortcuts import render
def index(request):
    return render(request,'hello/admin/index.html')
# Create your views here.
