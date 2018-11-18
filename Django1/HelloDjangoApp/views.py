from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")   
        }
    )

    #html_content = "<html><head><title>Hello, Django</title></head><body>"
    #html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
    #html_content += "</body></html>"

    #return HttpResponse(html_content)
