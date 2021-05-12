from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from django.utils.translation import gettext_lazy as _

from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    header = models.CharField(
        max_length=100,
        default="Curriculum Vitae",
        blank=False,
        verbose_name=_("Título principal"),
    )

    subheader = models.CharField(
        max_length=100,
        default="powered by Django",
        blank=False,
        verbose_name=_("Subtítulo"),
    )

    avatar = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        related_name="home_page_avatars",
        verbose_name=_("Avatar"),
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("header"),
            FieldPanel("subheader"),
        ], heading=_("Cabecera")),
        ImageChooserPanel("avatar"),
    ]

    template = "home/home_page.html"

    class Meta:
        verbose_name = "Curriculum"
