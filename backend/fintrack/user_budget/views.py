from django.shortcuts import render
from .models import Expenses, Expenditures
from django.http import HttpResponse



# Create your views here
def expenses_info(request):
    expenses = Expenses.objects.all()
    expenditures = Expenditures.objects.select_related('category').all()
    context = {
        'expenses': expenses,
        'expenditures': expenditures,
    }
    return render(request, 'expenses/expenses_info.html', context)

