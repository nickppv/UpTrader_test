from django.shortcuts import render


def index(request):
    return render(request, 'just_menu/index.html')


def brand(request, country):
    context_view = {
        'country': country,
    }
    return render(request, 'just_menu/brand.html', context_view)


def model(request, country, brand):
    context_view = {
        'country': country,
        'brand': brand,
    }
    return render(request, 'just_menu/model.html', context_view)
