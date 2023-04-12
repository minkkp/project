from django.shortcuts import render,redirect
from .models import *
from .forms import *

def post(request):
    if request.method=='POST':
        title = request.POST['title']
        content = request.POST['content']
        board = Board(
            title = title,
            content = content
        )
        board.save()
        return redirect('/main/')