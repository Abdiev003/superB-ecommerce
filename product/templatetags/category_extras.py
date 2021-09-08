from django import template

from product.models import (
    Category,
)

register = template.Library()


@register.simple_tag()
def category_list(published, limitStart=None, limitStop=None):
    return Category.objects.filter(is_published=published)[limitStart:limitStop]
