from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Цена'
    )

    def __str__(self):
        return self.name
