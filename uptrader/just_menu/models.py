from django.db import models


class Country(models.Model):
    country = models.TextField(max_length=30,
                               verbose_name='Страна')

    def __str__(self) -> str:
        return self.country

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Brand(models.Model):
    brand_name = models.TextField(max_length=30,
                                  verbose_name='Производитель')
    brand_fk = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="brand",
        )

    def __str__(self) -> str:
        return self.brand_name

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Model(models.Model):
    model_name = models.TextField(max_length=30,
                                  verbose_name='Модель')
    model_fk = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name="model"
        )

    def __str__(self) -> str:
        return self.model_name

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

