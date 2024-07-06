from django.shortcuts import render

def index(request):
    # division_by_zero = 1 / 0  
    # allrecord = record
    return render(request, "index.html")