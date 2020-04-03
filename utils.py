from django.http import HttpResponse


def index(request):
    print("193非常牛逼")

    return HttpResponse("success")


def demo(request):

    print("this is dev")
    print("11111")

    return HttpResponse("我在dev分支上")


class Queue(object):

    pass
