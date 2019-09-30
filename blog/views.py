from django.shortcuts import render, get_object_or_404
from .models import Board
# from .forms import UploadFileForm

def home(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def board(request):
    boards = Board.objects
    return render(request, 'blog/board.html', {'boards':boards})

def detail(request, blog_id):
    blog_detail= get_object_or_404(Board, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})
