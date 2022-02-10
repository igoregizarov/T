from django.shortcuts import render

# Create your views here.


def main(request):
    content = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', content)


def registers(request):
    content = {
        'title': 'Регистрация',
    }
    return render(request, 'mainapp/registers.html', content)


def contacts(request):
    content = {
        'title': 'Контакты',
    }
    return render(request, 'mainapp/contacts.html', content)