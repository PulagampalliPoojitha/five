from django.shortcuts import render

# Create your views here.
def wish(request):

    d={'name':'Dishanya','age':'8'}

    return render(request,'wish.html',context=d)
