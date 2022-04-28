from django.http import HttpResponse


# Create your views here.

def site_map(request):
    return HttpResponse("Site map: About")
