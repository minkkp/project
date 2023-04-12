from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from .models import *
from .forms import *

def index(request):
    board_list = Board.objects.all().order_by('-id')
    page = request.GET.get('page','1')
    paginator = Paginator(board_list,'7')

    context = {
        'page_obj':paginator.page(page)
    }
    return render(request, 'board/index.html', context)

def post(request):
    if request.method=='POST':
        title = request.POST['title']
        content = request.POST['content']
        board = Board(
            title = title,
            content = content
        )
        board.save()
        return redirect('board:detail',board.pk)
    else:
        boardForm = BoardForm
        context = {
            'boardForm':boardForm,
        }
        return render(request,'board/post.html',context)
    
def detail(request,pk):
    board = Board.objects.get(id=pk)
    comments = Comment.objects.filter(board=pk)
    page = request.GET.get('page','1')
    paginator = Paginator(comments,'3')
    context = {'board':board,
               'page_obj':paginator.page(page)}

    return render(request,'board/detail.html',context)

def comment(request,pk):
    # if request.user.is_authenticated: 
    board = get_object_or_404(Board, pk=pk)
    content = request.POST['content']
    comment = Comment(
            user = request.user,
            content = content,
            board = board,
    )
    comment.save()
    return redirect('board:detail',pk)

    # return redirect('accounts:login')

def update(request):
    pass
