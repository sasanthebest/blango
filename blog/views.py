from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import CommentForm
# Create your views here.
def index(request):
  # posts
  posts=Post.objects.filter(
    published_at__lte=timezone.now()
  )
  context={
    "posts":posts
  }
  return render(request,'blog/index.html',context)



def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user.is_active:
      if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
          comment = form.save(commit=False)
          comment.content_object = post
          comment.creator = request.user
          comment.save()
          return redirect(request.path_info)
      else:
        form=CommentForm()
    else:
      form=None
    return render(request, "blog/post-detail.html", {"post": post,"form":form})










