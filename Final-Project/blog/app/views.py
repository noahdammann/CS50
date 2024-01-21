from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import Post, Subscriber

# Create your views here.
def index(request):

    posts = Post.objects.all()

    return render(request, "app/index.html", {
        "posts" : posts
    })


def post(request, id):

    post = Post.objects.get(pk=id)

    return render(request, "app/post.html", {
        "post" : post
    })


@login_required
def new(request):

    if request.method == "GET":
        return render(request, "app/new.html")

    else:
        
        title = request.POST["title"]
        content = request.POST["content"]
        url = request.POST["url"]

        post = Post.objects.create(title=title, content=content, url=url)

        post.save

        return HttpResponseRedirect(reverse("index"))


def newsletter(request):

    if request.method == "GET":
        return render(request, "app/newsletter.html")

    else:
        email = request.POST["email"]
        subscriber = Subscriber.objects.create(email=email)
        subscriber.save()
        return HttpResponseRedirect(reverse('index'))


def contact(request):

    if request.method == "GET":
        return render(request, "app/contact.html")

def about(request):

    return render(request, "app/about.html")