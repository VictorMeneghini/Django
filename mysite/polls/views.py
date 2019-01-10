from django.http import HttpResponse

def index(request):
    print(request, '<<<<<<')
    return HttpResponse('Hello, world. u are at the polls index')

