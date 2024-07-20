from django.http import StreamingHttpResponse
import time

def number_iterator():
    for i in range(1, 11):
        yield f"{i}\n" 
        time.sleep(1)

def streaming_data(request):
    return StreamingHttpResponse(number_iterator(), content_type='text/plain')
