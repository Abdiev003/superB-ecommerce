from django.contrib import admin

from product.models import (
    Category,
)

from product.common import slugify


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "is_main", "is_published", 'id')
    list_display_links = ("title",)
    readonly_fields = ('slug',)
    list_filter = ("title", "is_published")
    search_fields = ('title',)
    # prepopulated_fields = {'slug': ('title',)}


    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        category = form.instance
        if not category.category.all().last():
            category.slug = slugify(f'{category.title}')
        else:
            category.slug = slugify(f'{category.category.all().last()} {category.title}')
        category.save()

    def get_form(self, request, obj=None, **kwargs):
        form = super(CategoryAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['category'].widget.attrs['style'] = 'height: 160px;'
        return form