from django.views.generic import ListView
from typing import TypeVar, Generic
from django.db.models.query import QuerySet
from .models import TestModel

TView = TypeVar('TView', bound=ListView)

class AppTypeQuerysetMixin(Generic[TView]):
    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        user = self.request.user
        
        if user.is_superuser:
            return queryset
        elif user.is_staff:
            return queryset.filter(is_published=True)
        else:
            return queryset.filter(owner=user)

class TestListView(AppTypeQuerysetMixin, ListView):
    model = TestModel
    template_name = 'test_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset