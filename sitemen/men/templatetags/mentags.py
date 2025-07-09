from django import template
from men.views import *

register = template.Library()

@register.inclusion_tag("list_categories.html")
def show_categories(selected=0):
    cats = Category.objects.all()
    return {"cats": cats, "selected": selected}


@register.inclusion_tag("list_tags.html")
def show_all_tags():
    return {"tags": TagPost.objects.all()}
