from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    # information`s
    first_name = models.CharField(
        _('First Name'), max_length=50, db_index=True)
    email = models.EmailField(_("Email Address"), max_length=254, db_index=True)
    company = models.CharField(
        _("Company"), max_length=80, null=True, blank=True)
    telephone = models.CharField(_("Telephone"), max_length=13)
    address = models.CharField(_("Address"), max_length=254)
    comment = models.TextField(_("Comment"))

    # moderation`s
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
        ordering = ("-created_at",)


class Subscribe(models.Model):
    """
    Subscribers are stored here
    """

    # information`s
    email = models.EmailField(
        _('Email Address'), max_length=255, unique=True, db_index=True)

    # moderation`s
    is_active = models.BooleanField(_('Active'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Subscriber")
        verbose_name_plural = _("Subscribers")
        ordering = ("-created_at",)

    def __str__(self):
        return self.email
