from django.view.decorators import require_GET, require_POST,require_safe
from django.shortcuts import HttpResponse

@require_GET()
def sample_view(request):
    return HttpResponse("Only the GET requests can access this view!")

#require_POST() decorator
@require_POST()
def sample_view(request):
    return HttpResponse("This view only responds to POST requessts")

#require_safe() decorator
@require_safe()
def sample_view(request):
    return HttpResponse("Only the GeT and HEAD request methods can access this view")
