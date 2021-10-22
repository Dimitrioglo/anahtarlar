from django.contrib import admin
from .models import UserExtended, Product, UserProduct, Key, SoldDateList
from django.contrib.auth.models import Permission
import nested_admin


class KeyInline(nested_admin.NestedStackedInline):
    model = Key
    extra = 1


@admin.register(Product)
class ProductInline(nested_admin.NestedModelAdmin):
    model = Product
    inlines = [KeyInline]


class UserProductInline(nested_admin.NestedStackedInline):
    model = UserProduct
    extra = 1


@admin.register(UserExtended)
class UserExtendedAdmin(nested_admin.NestedModelAdmin):
    inlines = [UserProductInline]


admin.site.register(Permission)
admin.site.register(SoldDateList)
admin.site.register(UserProduct)
