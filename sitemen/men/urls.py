from django.contrib import admin
from django.urls import path, re_path, register_converter
from men.views import *
from . import converters
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("contacts/", contacts, name="contacts"),
    path("addpage/", addpage, name="addpage"),
    path("login/", login, name="login"),
    path("post/<slug:post_slug>/", show_post, name="post"),
    path("category/<int:cat_id>/", show_category, name="category")
]

urlpatterns += staticfiles_urlpatterns()