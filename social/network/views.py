from django.shortcuts import render
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
  form = PostForm()
  return render(request, 'network/index.html', {'form': form})

@login_required
def all_post(request):
  return render(request, 'network/post.html')
