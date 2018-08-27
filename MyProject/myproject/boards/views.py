from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#from django.http import Http404
from .models import Board
from django.shortcuts import render, get_object_or_404

def home(request):
	boards = Board.objects.all()
	return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
	board = get_object_or_404(Board, pk=pk)
	return render(request, 'topics.html', {'board':board})