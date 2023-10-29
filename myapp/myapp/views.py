from django.http import HttpResponse
import datetime

def test(request):
    print("this is work as a consol.log")
    now = datetime.datetime.now()

    return HttpResponse("<h1>hi parag, this is a heading</h1>" + str(now))

def about(request):
    print("this is work as a consol.log")
    now = datetime.datetime.now()

    return HttpResponse("<h1>hi parag, this is a heading of about us  page</h1>" + str(now))    