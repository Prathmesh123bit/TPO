from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def index(request):
    # my_dict={'insert_me':'this is a Djngo Workshop'}
    return render(request,'placement_app/index.html',context=my_dict)
