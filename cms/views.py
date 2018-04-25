from django.shortcuts import render
from cms.models import Pages
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def slash(request):
    if request.method == 'GET':
        response = ''
        # response = """<form method=PUT accept-charset="utf-8">ADD CONTENT:<br>
        #               <input type="text" name="resource" value="Resource"  <br>>
        #               <input type="text" name="content"  value="Content"   <br>>
        #               <input type="submit" value="Submit"></form>
        #               <input type="hidden" name="_method" value="put" />"""
        for Page in Pages.objects.all():
            redirection = "<a href=/" + str(Page.id) + ">" + Page.name + "</a>"
            response += (str(Page.id) + ' : ' + redirection + "<br>")
        return(HttpResponse(response))
    elif request.method == 'PUT':
        try:
            name_rcv, page_rcv = str(request.body).split("/")
            print(type(name_rcv))
            new_page = Pages(name=name_rcv, page=page_rcv)
            new_page.save()
            response = "<html><body><h1>Name " + name_rcv + " and page "
            response += page_rcv + " added</h1>"
            response += "<p><a href=/>Back to home page</a></p>"
            return(HttpResponse(response))
        except ValueError:
            return(HttpResponse("Invalid sintax in PUT. Expected name/page"))

            return(HttpResponseNotFound("NOT FOUND"))
    else:
        return(HttpResponseNotFound("NOT FOUND"))


def number(self, num):
    try:
        Page = Pages.objects.get(id=str(num))
        return(HttpResponse(Page.page))
    except ObjectDoesNotExist:
        return(HttpResponse("Resource not in database"))

def notfound(self):
    return(HttpResponseNotFound("NOT FOUND"))
