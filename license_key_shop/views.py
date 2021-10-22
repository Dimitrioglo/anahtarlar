import datetime
from calendar import monthrange

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User
from .models import Product, SoldDateList, UserExtended
from .serializers import UserExtendedSerializer, UserSerializer


class SalesInfoDateViewSet(ModelViewSet):
    serializer_class = UserExtendedSerializer
    queryset = UserExtended.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id')
        month = request.GET.get('month')

        if user_id is None:
            user = request.user.user_extended
        else:
            user = self.get_queryset().get(user_id=user_id)

        dates = self.all_dates_in_month(int(month))
        user_childs = user.user_child.all()

        if not user_childs:
            sold_statistic = []
            result = self.statistics_by_user(user, dates, str(user.id))
            sold_statistic.append(result)
        else:
            sold_statistic = {
                "user_name": str(user),
                "child": []
            }
            self.statistics_by_user(user, dates, str(user.id))
            for user in user_childs:
                childs_ids = user.get_all_children(only_ids=True)
                if not childs_ids:
                    childs_ids = str(user.id)

                result = self.statistics_by_user(user, dates, childs_ids)
                sold_statistic['child'].append(result)
        return Response(sold_statistic)

    def statistics_by_user(self, user, dates, date_user):
        user_statistic = {
            "user": str(user),
            "key_limit": str(user.key_limit),
            "statistics_by_day": []
        }
        obj, total_user_sold = self.statistics_by_date(dates, date_user)
        user_statistic['total_user_sold'] = total_user_sold
        user_statistic['statistics_by_day'].append(obj)
        return user_statistic
    
    @staticmethod
    def statistics_by_date(dates, childs_ids):
        total_user_sold = 0
        obj = []
        for date in dates:
            from_date = datetime.datetime.strptime(str(date), '%Y-%m-%d').replace(hour=0, minute=0, second=0)
            to_date = datetime.datetime.strptime(str(date), '%Y-%m-%d').replace(hour=23, minute=59, second=59)
            key_sold_instances_count = SoldDateList.objects.filter(created_date__range=(from_date, to_date),
                                                                   created_by_id__in=childs_ids).count()
            obj.append({
                "date": str(date),
                "key_sold_today": key_sold_instances_count
            })
            total_user_sold += key_sold_instances_count

        return obj, total_user_sold

    @staticmethod
    def all_dates_in_month(month):
        current_date = datetime.datetime.now()
        days_in_month = monthrange(current_date.year, month)[1]
        result = [datetime.date(current_date.year, month, day) for day in range(1, days_in_month + 1)]
        return result


class SalesInfoTypeViewSet(ModelViewSet):
    serializer_class = UserExtendedSerializer
    queryset = UserExtended.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):

        user_id = request.GET.get('user_id')
        if user_id is None:
            user = request.user.user_extended
        else:
            user = self.get_queryset().get(user_id=user_id)

        user_childs = user.user_child.all()
        products = Product.objects.all()

        if not user_childs:
            sold_statistic = []
            lst = self.statistic_by_product(products, user, str(user.id))
            sold_statistic.append(lst)
        else:
            sold_statistic = {
                "user_name": str(user),
                "child": []
            }
            for user in user_childs:
                childs_ids = user.get_all_children(only_ids=True)

                if not childs_ids:
                    childs_ids = str(user.id)

                lst = self.statistic_by_product(products, user, childs_ids)
                sold_statistic['child'].append(lst)

        return Response(sold_statistic)

    @staticmethod
    def statistic_by_product(products, user, product_user):
        user_statistic = {
            "user": str(user),
            "key_limit": str(user.key_limit),
            "statistics_by_product": []
        }
        total_product_key_sold = 0
        for product in products:
            key_sold_instances_count = SoldDateList.objects.filter(key__product__name=product,
                                                                   created_by_id__in=product_user).count()
            obj = {
                "product": str(product),
                "product_key_sold": key_sold_instances_count
            }
            user_statistic['statistics_by_product'].append(obj)
            total_product_key_sold += key_sold_instances_count

        user_statistic['total_product_key_sold'] = total_product_key_sold

        return user_statistic


class RegisterUserViewSet(ModelViewSet):
    serializer_class = UserExtendedSerializer
    queryset = UserExtended.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        post_data = request.data
        serializer_user = UserSerializer(data=post_data)
        if serializer_user.is_valid():
            serializer_user.save()
            user_created = serializer_user.data['username']
            user_obj = User.objects.get(username=user_created)
            post_data['user'] = str(user_obj.id)
            serializer_user_extended = UserExtendedSerializer(data=post_data)

            if serializer_user_extended.is_valid():
                serializer_user_extended.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(serializer_user_extended.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer_user.errors, status=status.HTTP_400_BAD_REQUEST)
