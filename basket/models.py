from django.db import models
from authapp.models import User
from mainapp.models import Product
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.functional import cached_property


class BasketQuerySet(models.QuerySet):

    def count_gt_2(self):
        return self.filter(quantity__gt=2)

    def count_lt_2(self):
        return self.filter(quantity__lt=2)

    def delete(self):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super().delete()


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    @cached_property
    def get_items_cached(self):
        return Basket.objects.filter(user=self.user)

    def total_quantity(self):
        baskets = self.get_items_cached
        return sum(basket.quantity for basket in baskets)

    def total_sum(self):
        baskets = self.get_items_cached
        return sum(basket.sum() for basket in baskets)

    def delete(self, using=None, keep_parents=False):
        self.product.quantity += self.quantity
        super().delete()

    def save(self, *args):
        if self.pk:
            self.product.quantity -= self.quantity - Basket.objects.get(pk=self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super().save(*args)

# @receiver(pre_save, sender=Basket)
# def product_quantity_update(sender, update_fields, instance, **kwargs):
#     if u
#     if instance.pk:
#         instance.product.quantity -= instance.quantity - instance.objects.get(pk=instance.pk).quantity
#     else:
#         instance.product.quantity -= instance.quantity
#     instance.product.save()
