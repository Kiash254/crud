from django import views
from django.urls import path
from numpy import delete

from portfolio.views import Create, home,Delete
app_name="portfolio"

urlpatterns = [
    path("",home,name="home"),
    path("create",Create,name="create"),
    # path("detail/<int:pk>/",Detail,name="detail"),
    # path("update/<int:pk>/",Update,name="update"),
    path("delete/<int:pk>/",Delete,name="delete")
    
]
