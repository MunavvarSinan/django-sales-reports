from django.shortcuts import render
from django.views.generic import ListView
from .models import Sales
# Create your views here.
def home_view(request):
    hello = 'something'
    return render(request, 'sales/home.html', {'h': hello}) # the dictionary is like passing a context to the template


class SalesListView(ListView):
    model = Sales
    template_name = 'sales/main.html'
    context_object_name = 'qs' # this is the default name for the query set