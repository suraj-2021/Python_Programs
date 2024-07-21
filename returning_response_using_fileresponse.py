from django.http import FileResponse

def download_file(request):
    response = FileResponse(open('filename.png', "rb"))
    response['Content-Disposition'] = 'attachment'; filename= "subjective.jpg"
    return respose


def hills(request):
    hill_response = FileResponse(open("greenhills.jpg",'rb'))
    hill_response['Content-Disposition'] = 'attachment'; filename="greenhills.jpg"
    return hill_response

def airemriates(request):
    air_response = FileRespnse(open("AirRules.txt","rb"))
    air_response['Content-Disposition'] = 'attachment'; filename='guidelines.txt'
    return air_response
