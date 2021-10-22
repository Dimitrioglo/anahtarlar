from django.contrib import admin
from .models import UserExtended, UserExtendedSpecification, Product, UserProduct, Key, SoldDateList
from django.contrib.auth.models import Permission
import nested_admin


class KeyInline(nested_admin.NestedStackedInline):
    model = Key
    extra = 1


@admin.register(Product)
class ProductAdmin(nested_admin.NestedModelAdmin):
    model = Product
    inlines = [KeyInline]
    extra = 1


class UserProductInline(nested_admin.NestedStackedInline):
    model = UserProduct
    extra = 1


class UserExtendedSpecificationInline(nested_admin.NestedStackedInline):
    model = UserExtendedSpecification
    extra = 1


@admin.register(UserExtended)
class UserExtendedAdmin(nested_admin.NestedModelAdmin):
    inlines = [UserExtendedSpecificationInline, UserProductInline]
    extra = 1


admin.site.register(Permission)
admin.site.register(SoldDateList)

