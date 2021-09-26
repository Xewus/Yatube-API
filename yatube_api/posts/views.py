from django.http import HttpResponse


def home_view(request):
    return HttpResponse(
        '''The resource is only available as an API.
        Use "http://127.0.0.1:8000/api/v1/" if you have registrashin
        else "http://127.0.0.1:8000/api/v1/posts/"''')
