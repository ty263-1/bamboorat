from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
]

urlpatterns += [
    path('product/shopee/draft/', views.draft, name='draft'),
]
