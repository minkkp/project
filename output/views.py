from django.shortcuts import render
from django.views.decorators.http import require_http_methods,require_POST,require_safe
from .models import *

@require_http_methods(['GET','POST'])
def result(request):
    if request.method=='POST':
        upload = Upload( 
            user_id = request.user,
            img_file = request.FILES.get('image')
        )
    upload.save()
    return render(request,'output/result.html',{'upload':upload})

@require_http_methods(['GET','POST'])
def map(request):
    return render(request,'output/map.html')