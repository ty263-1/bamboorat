from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def draft(request):
    return render(request, 'erp/shopee/product/draft/draft.html')
