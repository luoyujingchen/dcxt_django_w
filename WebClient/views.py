from django.shortcuts import render


# Create your views here.
def go_add_dish(request):
    return render(request,'addDishPage.html')


def gogo(request):
    return render(request,'addDish.html')