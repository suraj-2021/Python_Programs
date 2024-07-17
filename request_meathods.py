from django.http import HttpResponse

def your_view(request):
    name = request.GET.get('name','Guest')
    email = request.POST.get('eamil','')
    profile_pic = request.FILES.get('Profile_Pic')

    return HttpResponse(f"Hi my name is {name} and my email is {email}")
