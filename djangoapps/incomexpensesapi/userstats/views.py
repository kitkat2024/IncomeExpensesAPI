from django.shortcuts import render
from rest_framework import views, status
from income.models import Income
import datetime
from rest_framework import response


# Create your views here.


class IncomeSourcesSummaryStats(views.APIView):

    def get_amount_for_source(self, income_list, source):
        income = income_list.filter(source=source)
        amount = 0
        for i in income:
            amount += i.amount
        return {'amount': str(amount)}

    def get_source(self, income):
        return income.source

    def get(self, request):
        todays_date = datetime.date.today()
        ayear_ago = todays_date - datetime.timedelta(days=30*12)
        income = Income.objects.filter(owner=request.user, date__gte=ayear_ago, date__lte=todays_date)

        final = {}
        sources = list(set(map(self.get_source, income)))

        for source in sources:
            final[source] = self.get_amount_for_source(income, source)

        return response.Response({'income_source_data': final}, status=status.HTTP_200_OK)

