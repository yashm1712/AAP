from django.contrib import messages
from django.shortcuts import render, redirect

from .models import *

from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def blog_home(request):
    blogs = Blog.objects.order_by('time')[::-1]
    user = request.user
    context = {'blogs': blogs, 'user': user}
    return render(request, 'blog/blog_home.html', context)


def blog_like(request):
    user = request.user

    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        print('blog ID -', blog_id)
        blog_obj = Blog.objects.get(Sr_No=blog_id)

        if user in blog_obj.liked.all():
            blog_obj.liked.remove(user)
        else:
            blog_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, blog_id=blog_id)
        if not created:
            if like.likes == 'Like':
                like.likes = 'Unlike'
            else:
                like.likes = 'Like'

        like.save()

    return redirect('/blog/')


def blog_detail(request,id):
    blog = Blog.objects.get(Sr_No=id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})


def add_blog(request,):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        pic = request.FILES['image']
        user_ = request.user

        if len(title) < 5 or len(content) < 100:
            messages.error(request, "Please fill the blog correctly !!!")

        else:
            blog = Blog(user=user_, title=title, content=content, pic=pic)
            blog.save()
            messages.success(request, "Your blog has been submitted successfully.")

    return render(request, 'blog/add_blog.html')


def your_blog(request, id):
    blogs = Blog.objects.filter(user_id=id).order_by('time')[::-1]
    return render(request, 'blog/blog_home.html', {'blogs': blogs})
