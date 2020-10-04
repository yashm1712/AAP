import django_filters
from .models import *


class MemberFilter(django_filters.FilterSet):
    class Meta:
        model = Member
        fields = ['Graduation_Starting_Year', 'Graduation_Ending_Year', 'Branch']
