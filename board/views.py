from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import *
from .forms import *

def index(request):
    board_list = Board.objects.all()
    page = request.GET.get('page','1')
    paginator = Paginator(board_list,'6')

    context = {
        'page_obj':paginator.page(page)
    }
    return render(request, 'board/index.html', context)

def post(request):
    if request.method=='POST':
        for i in range(10):
            title = request.POST['title']
            content = request.POST['content']
            board = Board(
                title = title,
                content = content
            )
            board.save()
        return redirect('board:detail')
    else:
        boardForm = BoardForm
        context = {
            'boardForm':boardForm,
        }
        return render(request,'board/post.html',context)
    
def detail(request):
    return render(request,'board/detail.html')
def update(request):
    pass
