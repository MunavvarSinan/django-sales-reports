from django.shortcuts import render

# Create your views here.
def home_view(request):
    hello = 'something'
    return render(request, 'sales/main.html', {'h': hello}) # the dictionary is like passing a context to the template
