from django import template
from men.views import *

register = template.Library()

@register.simple_tag()
def get_categories():
    return cats_db

@register.inclusion_tag("list_categories.html")
def show_categories(selected=0):
    cats = cats_db
    return {"cats": cats, "selected": selected}
