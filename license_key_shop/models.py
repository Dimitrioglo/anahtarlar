from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


#     User types: Owner, Partner, Store, Seller
class UserExtended(models.Model):
    parent = models.ForeignKey('UserExtended', on_delete=models.CASCADE, null=True, blank=True,
                               related_name='user_child')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_extended')

    def __str__(self):
        return self.user.username

    def get_all_children(self, self_include=False, only_ids=False):
        r = []
        if self_include:
            if only_ids:
                r.append(self.id)
            else:
                r.append(self)

        for c in self.user_child.all():
            _r = c.get_all_children(self_include=True, only_ids=only_ids)
            if 0 < len(_r):
                r.extend(_r)
        return r


class UserExtendedSpecification(models.Model):
    user_extended = models.ForeignKey(UserExtended, on_delete=models.CASCADE,
                                      related_name="user_extended_specification")
    date_created = models.DateField()
    due_date = models.DateField()
    key_limit = models.IntegerField(default=0)
    daily_available_keys = models.IntegerField(default=0)
    sold_min = models.IntegerField(default=0)
    sold_min_due_date = models.DateField()
    key_left = models.IntegerField(default=0)

    def __str__(self):
        return str(self.date_created)


class Product(models.Model):
    user_extended = models.ManyToManyField(UserExtended, through="UserProduct")
    name = models.CharField(max_length=150, blank=True)
    license_duration = models.IntegerField(default=0)
    device_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Key(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, related_name='product_key')
    key = models.CharField(max_length=50, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.key


class UserProduct(models.Model):
    user = models.ForeignKey(UserExtended, on_delete=models.CASCADE, related_name='user_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_users')
    key_quantity = models.IntegerField(default=0)


class SoldDateList(models.Model):
    created_by = models.ForeignKey(UserExtended, on_delete=models.CASCADE, related_name='user_sold_date', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    key = models.ForeignKey(Key, on_delete=models.CASCADE, related_name="sold_key", blank=True)

    def __str__(self):
        return self.created_by.user.username
