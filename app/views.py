from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm

# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = MyForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            print(cleaned_data)
            form = MyForm()
            return HttpResponse("Yay! you are human.")
        else:
            return HttpResponse("OOPS! Bot suspected.")

    else:
        form = MyForm()

    return render(request, 'index.html', {'form': form})
