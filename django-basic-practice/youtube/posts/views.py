from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import loader
from . import models
from . import forms

def post_list(request):
    template = loader.get_template('post_list.html')
    posts = models.Post.objects.all().values()
    context = {
        'posts' : posts,
    }
    return HttpResponse(template.render(context=context, request=request))

def post_deatil(request, post_id):
    template = loader.get_template('detail.html')
    try:
        post = models.Post.objects.get(id=post_id)
    except models.Post.DoesNotExist:
        template404 = loader.get_template('404.html')
        return HttpResponseNotFound(template404.render())
    comment = models.Comment.objects.filter(post=post)
    context = {
        'post' : post,
        'comment' : comment
    }
    return HttpResponse(template.render(context=context, request=request))

def post_create(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            models.Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/post_list/')
    else:
        form = forms.PostForm()

    template = loader.get_template('post_form.html')
    
    context = {
        'form' : form,
    }

    return HttpResponse(template.render(context=context, request=request))
