from django import template
from men.views import *

register = template.Library()

@register.inclusion_tag("list_categories.html")
def show_categories(selected=0):
    cats = Category.objects.all()
    return {"cats": cats, "selected": selected}
