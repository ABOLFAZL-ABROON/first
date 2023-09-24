from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound,Http404
import datetime
current_datetime = datetime.datetime.now()
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
days = {
    'satureday': 'this day is satureday',
    'sunday': 'this day is sunday',
    'monday': 'this day is monday',
    'thuesday': 'this day is thuesday',
    'wednesday': 'this day is wednesday',
    'thursday': 'this day is thursday',
    'friday': 'this day is friday'
}

def dynamic_day(request,day):
    day_data = days.get(day)
    if day_data is None:
        raise Http404()
        #response_data = render_to_string('404.html')
        #return HttpResponseNotFound(response_data)
    conetxt = {
        "data" : day_data,
            "day" : day
    }
    return render(request,'web/web.html',conetxt)
     
def days_list(request):
    days_list = list(days.keys())
    contex = {
        'days' : days_list
    }
    return render(request,'web/index.html',contex)


def dynamic_days_by_number(request, day):
    days_names = list(days.keys())
    if day > len(days_names):
        return HttpResponseNotFound('day is not exist')
    redirect_day = days_names[day -1]
    redirect_url = reverse('days-of-week',args=[redirect_day])
    return HttpResponseRedirect(redirect_url)
    #return HttpResponse(day)

def date_time(request):
    return HttpResponse(current_datetime)
