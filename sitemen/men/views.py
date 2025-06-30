from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from men.models import Women, Category


data_db = [
    {
        "id": 1,
        "title": "Angelina Joly",
        "content": """Biography of Angelina Joly""",
        "is_published": True,
    },
    {
        "id": 2,
        "title": "Margo Robby",
        "content": "Biography of Margo Robby",
        "is_published": False,
    },
    {
        "id": 3,
        "title": "Julia Roberts",
        "content": "Biography of Julia Roberts",
        "is_published": True,
    },
]


options = [
    {"title": "About site", "url_name": "about"},
    {"title": "Contact information", "url_name": "contacts"},
    {"title": "Add article", "url_name": "addpage"},
    {"title": "Sign in", "url_name": "login"},
]


# Create your views here.
def index(request):
    posts = Women.published.all()
    data = {
        "title": "Main page", 
        "menu": options, 
        'posts': posts,
        "selected": 0}

    return render(request, "index.html", data)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    data = {
        "title": post.title,
        "menu": options,
        "post": post,
        "cat_selected": 1,
    }
    return render(request, 'post.html', data)

def about(request):
    return render(request, "about.html", {"title": "About site", "menu": options})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")


def addpage(request):
    return HttpResponse("<h1>Add article</h1>")


def contacts(request):
    return HttpResponse("<h1>Phone: 8(800)555-35-35</h1>")


def login(request):
    return HttpResponse("<h1>Sign in</h1>")


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk)
    
    data = {
        "title": f"Category {category.name}", 
        "menu": options, 
        "posts": posts, 
        "selected": category.pk}

    return render(request, "index.html", data)
