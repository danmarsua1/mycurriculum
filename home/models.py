from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page


class HomePage(Page):

    template = "home/home_page.html"

    class Meta:
        verbose_name = "Curriculum"


