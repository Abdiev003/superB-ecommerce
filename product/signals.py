from django.db.models.signals import post_save
from django.dispatch import receiver

from product.models import (
    Category,
)

from product.common import slugify


# @receiver(post_save, sender=Category)
# def create_product_slug(sender, instance, created, **kwargs):
#     # if created:
#     #     instance.slug = slugify(instance.title)
#     #     instance.save() 
#     pass