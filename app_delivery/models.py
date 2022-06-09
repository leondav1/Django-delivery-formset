from django.db import models


class Delivery(models.Model):
    ACTIVE_CHOICES = [
        ('notebooks', 'Ноутбуки'),
        ('phones', 'Телефоны'),
        ('accessories', 'Комплектующие'),
    ]
    title = models.CharField(verbose_name='Название товара', max_length=100)
    product_type = models.CharField(verbose_name='Тип товара', max_length=100, choices=ACTIVE_CHOICES)
    delivery_date = models.DateField(verbose_name='Дата доставки')
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)

    class Meta:
        ordering = ['delivery_date']

    def __str__(self):
        return self.title


class Address(models.Model):
    addr = models.CharField(verbose_name='Адрес пункта выдачи', max_length=100)
    delivery = models.ForeignKey(
        'Delivery',
        verbose_name='Доставка',
        default=None,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='addresses'
    )

    def __str__(self):
        return self.addr


class File(models.Model):
    file = models.FileField(verbose_name='Файл', upload_to='files/', blank=True)
    name = models.CharField(verbose_name='Имя файла', max_length=50)
    delivery = models.ForeignKey(
        'Delivery',
        verbose_name='Доставка',
        default=None,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='files'
    )

    def __str__(self):
        return f'Файл {self.name} для доставки {self.delivery.title}'
