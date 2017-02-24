from django.shortcuts import render, HttpResponse
import datetime
import arrow
import time

# Create your views here.
def index(request):
    i = datetime.datetime.now()
    print time.localtime()
    currentDateTime = ("%s/%s/%s" % (i.day,i.month,i.year)) + (" %s:%s:%s" % (i.hour,i.minute,i.second))
    context={
    "currentDateTime":currentDateTime
    }
    return render(request, 'timedisplay/index.html', context)
