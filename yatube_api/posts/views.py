from django.http import HttpResponse


def home_view(request):
    return HttpResponse('The resource is only available as an API.')
