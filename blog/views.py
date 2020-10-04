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


def blog_detail(request, id):
    blog = Blog.objects.get(Sr_No=id)
    comments = Comment.objects.filter(blog_c=blog).order_by('timestamp')[::-1]
    count = Comment.objects.filter(blog_c=blog).count()
    context = {'blog': blog, 'comments': comments, 'count': count}
    return render(request, 'blog/blog_detail.html', context)


def blog_comment(request):
    if request.method == 'POST':
        user_ = request.user
        comments = request.POST['comments']
        blog_no = request.POST['blog_no']
        blogs = Blog.objects.get(Sr_No=blog_no)

        comment = Comment(user=user_, comments=comments, blog_c=blogs)
        comment.save()
        messages.success(request, "Your comment has been posted successfully.")
        return redirect('/blog/blog/' + blog_no)

    # return render(request, 'blog/blog_detail.html', {'blog': blogs})


def add_blog(request, ):
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
    user = request.user
    context = {'blogs': blogs, 'user': user}
    return render(request, 'blog/blog_home.html', context)


def search(request):
    query = request.GET['query']
    user = request.user

    if len(query) > 50:
        blogs = Blog.objects.none()

    else:
        blog_title = Blog.objects.filter(title__icontains=query)
        blog_content = Blog.objects.filter(content__icontains=query)
        first_name = Blog.objects.filter(user__first_name__icontains=query)
        last_name = Blog.objects.filter(user__last_name__icontains=query)

        blogs = blog_title | blog_content | first_name | last_name

    context = {'blogs': blogs, 'user': user, 'query': query}
    return render(request, 'blog/search.html', context)


def blog_delete(request, blog_id):
    blog_ = Blog.objects.filter(Sr_No=blog_id)
    image_path = blog_[0].pic.url
    blog_.delete()
    messages.info(request, 'Your Blog has been successfully deleted.')
    return redirect('/blog')

