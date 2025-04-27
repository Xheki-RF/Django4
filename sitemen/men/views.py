from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    games = ["DS3", "DS2", "DS1", "ER"]
    # t = render_to_string("index.html")
    # return HttpResponse(t)
    data = {"title": "main page", "game": games, 'num': 5}

    return render(request, "index.html", data)


def about(request):
    return render(request, "about.html")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Articles by categories</h1><p>id {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f"<h1>Articles by categories</h1><p>slug {cat_slug}</p>")

def archive(request, year):
    if year < 2005:
        url = reverse("cats", args=("music", ))
        return HttpResponseRedirect(url)
    
    return HttpResponse(f"<h1>Articles by years</h1><p>year {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
