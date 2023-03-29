from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.
@login_required
def make_a_post(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        description = request.POST['description']
        image = request.FILES.get('image')

        post = Post(post_user_id = user_id, description = description, image = image)
        post.save()

        return redirect('callback')
    return render(request, 'post_content/make_a_post.html')