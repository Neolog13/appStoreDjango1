from django.db import models

class Product(models.Model):
    title = models.CharField('Denotation', max_length=50)
    assignment = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'PreProduct'
        verbose_name_plural = 'PreProducts'
