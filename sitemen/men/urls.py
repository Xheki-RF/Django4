from django.contrib import admin
from django.urls import path, re_path, register_converter
from men.views import *
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("contacts/", contacts, name="contacts"),
    path("addpage/", addpage, name="addpage"),
    path("login/", login, name="login"),
    path("post/<int:post_id>/", show_post, name="post"),
]
