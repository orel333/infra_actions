from django.http import HttpResponse


def index(request):
    return HttpResponse('Крутое получилось плаванье!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
