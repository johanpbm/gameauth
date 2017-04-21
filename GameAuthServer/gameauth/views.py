#from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
#from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Activity

def index(request):
    latest_activity_list = Activity.objects.order_by('-name')[:3]
    #template = loader.get_template('gameauth/index.html')
    context = {
        'latest_activity_list' : latest_activity_list,
    }
    #output = ', '.join(q.description for q in latest_activity_list)
    #return HttpResponse(output)
    #return HttpResponse(template.render(context,request))
    return render(request, 'gameauth/index.html', context)

# Create your views here.

def detail(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    #try:
    #    activity = Activity.objects.get(pk=activity_id)
    #except Activity.DoesNotExist:
    #    raise Http404("Activity does not exist")
    #return HttpResponse("You're looking at activity %s." % activity_id)
    return render(request, 'gameauth/detail.html', {'activity': activity})
    
def results (request, activity_id):
    response = "You're looking at the results of activity %s."
    return HttpResponse(response % activity_id)

def addActivity(request, activity_id):
    return HttpResponse("You're adding an activity %s." % activity_id)