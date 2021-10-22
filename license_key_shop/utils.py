from .models import SoldDateList


def sell_key(who, key):
    SoldDateList.objects.create(created_by=who, key=key)
