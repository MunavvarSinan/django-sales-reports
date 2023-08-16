from django.urls import path
from .views import ( home_view, SalesListView)

app_name = 'sales'

urlpatterns = [
    path('', home_view, name='home'),
    path('list/', SalesListView.as_view(), name='list') # is we are using class based views we need to use .as_view() inorder to convert it to a view
]
