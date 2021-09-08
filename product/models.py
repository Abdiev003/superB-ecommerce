from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """
    in this table you can store categories
    """

    # relation`s
    category = models.ManyToManyField(
        "self", related_name="product_categories", blank=True)

    # information`s
    title = models.CharField(_("Category Name"), max_length=80, db_index=True)

    # moderation`s
    slug = models.SlugField(
        _("Category Slug"), max_length=100, db_index=True, unique=True, editable=False)
    is_main = models.BooleanField(_("Main Category"), default=True)
    is_second = models.BooleanField(_("Second Category"), default=False)
    is_third = models.BooleanField(_("Third Category"), default=False)
    is_published = models.BooleanField(_("Published"), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('-created_at',)

    @property
    def get_slug(self):
        slug = ''
        for item in self.category.all():
            slug += item.title
        return slug

    def __str__(self):
        if self.is_main:
            title = f'{self.title}'
        elif self.is_second:
            title = f'{self.title}'
        else:
            print(self.category.all())
            title = f'{self.category.all().last()} {self.title} '
        return title
