from django.shortcuts import render
from .models import Post
def post_list(request):
    all_post = Post.objects.all()
    print(all_post)
    return render(request, 'post/post_list.html')
