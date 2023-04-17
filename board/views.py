from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_http_methods,require_POST,require_safe
from django.contrib import messages
from django.core.paginator import Paginator
from .models import *
from .forms import *

@require_safe
def index(request):
    board_list = Board.objects.all().order_by('-id') # 게시글 id 내림차순으로 정렬
    page = request.GET.get('page','1') # url주소로부터 게시물 페이징 정보를 받아옴, 호출 없으면 default 1
    paginator = Paginator(board_list,'7') # 7개 게시물 = 1개 페이지로 처리

    context = {
        'page_obj':paginator.page(page) # paging정보를 context로 전달
    }
    return render(request, 'board/index.html', context)

@require_http_methods(['GET','POST'])
def post(request):
    if request.user.is_authenticated: # 권한(로그인) 유무 확인
        if request.method=='POST':
            qna_title = request.POST['qna_title']
            qna_content = request.POST['qna_content']
            board = Board( 
                qna_title = qna_title,
                qna_content = qna_content,
                user_id=request.user,
            ) # Board 모델객체 생성후 request받은값을 저장
            board.save() 
            return redirect('board:detail',board.pk)
        else:
            return render(request,'board/post.html')
    else:
        messages.error(request,'로그인이 필요한 기능입니다')
        return redirect('board:index')         
    
@require_safe
def detail(request,pk):
    board = Board.objects.get(id=pk) 
    comments = Comment.objects.filter(qna_no=pk) # 게시물과 일치하는 댓글들 필터링
    page = request.GET.get('page','1') # url주소로부터 댓글 페이징 정보를 받아옴, 호출 없으면 default 1
    paginator = Paginator(comments,'3') # 3개댓글 = 1개 페이지로 처리
 
    context = {'board':board,
               'page_obj':paginator.page(page),
               'user_id':str(request.user),}

    return render(request,'board/detail.html',context)

@require_POST
def comment(request,pk):
    if request.user.is_authenticated:
        board = get_object_or_404(Board, pk=pk)
        content = request.POST['content']
        comment = Comment(
                user_id = request.user,
                com_comment = content,
                qna_no = board, # 게시물 : 댓글 , 1:N 관계 형성
        )
        comment.save()
        return redirect('board:detail',pk)
    else:
        messages.error(request,'로그인이 필요한 기능입니다')
        return redirect('board:detail',pk)   


# 댓글삭제
@require_POST
def del_com(request,pk1,pk2): 
    comments = Comment.objects.filter(qna_no=pk1) # 게시물과 매칭되는 댓글들을 가져옴
    comment = get_object_or_404(Comment, pk=pk2) # 매칭된 댓글중 삭제할 pk를 선택
    comment.delete()
    messages.success(request,"댓글이 삭제되었습니다")
    return redirect('board:detail',pk1)

# 게시물 수정
@require_http_methods(['GET','POST'])
def update(request,pk):
    board = Board.objects.get(id=pk)
    if request.method=='POST': # 게시물 제목,내용값 요청받아서 게시물 객체에 재할당 
        board.qna_title = request.POST['qna_title']
        board.qna_content = request.POST['qna_content']
        board.save()
        messages.success(request,"게시글이 수정되었습니다")
        return redirect('board:detail',board.pk)
    else:
        context = {'board':board,}
    return render(request,'board/update.html',context)

# 게시물 삭제
@require_POST
def delete(request,pk):
    board = Board.objects.get(id=pk)
    board.delete()

    board_list = Board.objects.all().order_by('-id')
    page = request.GET.get('page','1') # url주소로부터 페이징 정보를 받아옴, 정보 없으면 default 1
    paginator = Paginator(board_list,'7') # 7개단위당 1개 페이지로 처리

    context = {
        'page_obj':paginator.page(page)
    }
    messages.success(request,"게시글이 삭제되었습니다")
    return render(request, 'board/index.html', context)

