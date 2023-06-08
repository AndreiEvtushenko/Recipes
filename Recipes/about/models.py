from django.db import models


class HelpFormModel(models.Model):
    name = models.CharField(
        max_length=30,
        help_text='Input name',
        blank=False,
    )
    text = models.TextField(
        max_length=350,
        help_text='Describe your issues or questions',
        blank=False,
    )
    email = models.EmailField(
        blank=False,
    )
