
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')
def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepunc=request.POST.get('removepunc','off')

    fullcaps=request.POST.get('UPPERCASE')
    newlineremover=request.POST.get('newlineremover')
    extraspaceremover=request.POST.get('extraspaceremover')
    charactercount=request.POST.get('charactercount')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}
        djtext=analyzed


    if(fullcaps=="on"):
            analyzed=""
            for char in djtext:
                analyzed=analyzed+char.upper()
            params = {'analyzed_text': analyzed}
            djtext=analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if(char!="\n" and char!="\r"):
                         analyzed = analyzed + char

        params = {'analyzed_text':analyzed}
        djtext=analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                   analyzed = analyzed + char

        params = {'text':analyzed }
        djtext=analyzed



    if(removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("Please choose the correct option and try again!")


    return render(request, 'analyze.html', params)





