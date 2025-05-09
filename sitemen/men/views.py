from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


data_db = [
    {
        "id": 1,
        "title": "Angelina Joly",
        "content": """GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA 
        GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA GOYDA SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO 
        SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO SVO """,
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
    data = {
        "title": "Main page", 
        "menu": options, 
        'posts': data_db}

    return render(request, "index.html", data)


def show_post(request, post_id):
    return HttpResponse(f"Article with id={post_id}")

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
