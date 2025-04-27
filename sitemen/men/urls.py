from django.contrib import admin
from django.urls import path, re_path, register_converter
from men.views import *
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("cats/<int:cat_id>/", categories, name="cats_id"),
    path("cats/<slug:cat_slug>/", categories_by_slug, name="cats"),
    path("archive/<year4:year>/", archive, name="archive"),
]
