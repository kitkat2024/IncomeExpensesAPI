from django.urls import path
from .views import IncomeSourcesSummaryStats


urlpatterns = [
    path('income_source_data/', IncomeSourcesSummaryStats.as_view(), name='income-source-data')
]