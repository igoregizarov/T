from django.shortcuts import render

# Create your views here.


def main(request):
    content = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', content)