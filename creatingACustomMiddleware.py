from django.utils.deprecation import MiddlewareMixin

class CustomMiddleWareClass(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response 

    def __call__(self, request):
        # Add custom attributes to the request object
        request.message = "Hello-World-!"
        request.message1 = "Hello-World-!-1"
        
        # Get the response from the next middleware or view
        response = self.get_response(request)

        # Modify the response if the status code is 200
        if response.status_code == 200:
            original = response.content.decode("utf-8")
            modified = f"I modified it : {original}"
            response.content = modified.encode('utf-8')

        return response
