from django.http import HttpResponse


def index(request):
    print("193非常牛逼")

    return HttpResponse("success")
