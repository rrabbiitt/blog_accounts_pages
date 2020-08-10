from django.shortcuts import render
from .models import Portfolio

def portfolio(request):
    portfolio = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolio':portfolio})
