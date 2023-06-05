import django_filters
from .models import*

class CompaniesFilter(django_filters.FilterSet):

    class Meta:
        model = Companies
        fields = ['Kurulus_turu','Ulke','Calisan_sayisi',]
