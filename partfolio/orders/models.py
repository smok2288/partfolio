from django.db import models
from market.models import Product
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from coupons.models import Coupon


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Фамилия')
    last_name = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField()
    address = models.CharField(max_length=200, verbose_name='Адрес')
    postal_code = models.CharField(max_length=10, verbose_name='Почтовый индекс')
    city = models.CharField(max_length=50, verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=True)
    coupon = models.ForeignKey(Coupon, related_name='orders',on_delete=models.PROTECT, null=True, blank=True)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return '{}'.format(self, id)

    def get_total_cost(self):
        total_coast = sum(item.get_coast() for item in self.items.all())
        return total_coast-total_coast*(self.discount/Decimal('100'))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='orders_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_coast(self):
        return self.price*self.quantity

