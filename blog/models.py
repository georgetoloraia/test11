from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models

def validate_email_domain(value):
    if not value.endswith('@redberry.ge'):
        raise ValidationError(
            _('%(value)s is not a valid email address from Redberry domain'),
            params={'value': value},
        )

class Category(models.Model):
    title = models.CharField(max_length=100)
    text_color = models.CharField(max_length=7)
    background_color = models.CharField(max_length=7)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    publish_date = models.DateTimeField()
    categories = models.ManyToManyField(Category)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, validators=[validate_email_domain])
