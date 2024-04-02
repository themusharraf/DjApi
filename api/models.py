from django.db import models


class User(models.Model):
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    username = models.CharField(verbose_name="Telegram username", max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name='Telegram ID', unique=True, default=1)
    email = models.CharField(verbose_name='Email', max_length=50, null=True)

    def __str__(self):
        return f"{self.id} - {self.telegram_id} - {self.full_name}"


class Product(models.Model):
    product_name = models.CharField(verbose_name="Product name", max_length=50)
    photo = models.CharField(verbose_name="Rasm", max_length=200, null=True)
    price = models.DecimalField(verbose_name="Price", decimal_places=2, max_digits=8)
    description = models.TextField(verbose_name="Product about", max_length=3000, null=True)

    category_code = models.CharField(verbose_name="Category code", max_length=20)
    category_name = models.CharField(verbose_name="Category nomi", max_length=30)
    subcategory_code = models.CharField(verbose_name="Ost-Category code", max_length=20)
    subcategory_name = models.CharField(verbose_name="Ost-Category name", max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"№ {self.id} - {self.product_name}"
