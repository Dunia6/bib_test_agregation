from rest_framework import filters
from datetime import datetime, timedelta


class LastTenDaysFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        tenDaysAgo = datetime.now() - timedelta(days= 10)
        return queryset.filter(pubdate__gte= tenDaysAgo)