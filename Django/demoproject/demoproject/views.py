from django.http import HttpResponse

def handler404(request, exception): # Custom 404 error. 
    return HttpResponse('404: Call on page not found')


def index(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content) 