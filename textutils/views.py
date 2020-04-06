# I have created this file- Prem
from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
    #return HttpResponse('''<h1> PskClicks </h1> <a href="pskclicks.github.io/web/"> Webpage</a>''')
#def about(request):
 #   return HttpResponse("About Page")

def index(request):
    return render(request,'index.html')
    #return HttpResponse("Home")
def analyze(request):
    #Get the text
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    uppercase = request.GET.get('uppercase','off')
    newlineremove=request.GET.get('newlineremove','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charcount=request.GET.get('charcount','off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(uppercase == "on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+  char .upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    elif(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
               analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    elif(charcount == "on"):
        analyzed = ""
        lenght=len(djtext)

        params = {'purpose': 'Total number of characters', 'analyzed_text': analyzed,'print':lenght}
        # Analyze the text
        return render(request, 'analyze.html', params)


    else:
        return HttpResponse("Error")


def capfirst(request):
    return HttpResponse("Capitalize first")
def newlineremove(request):
    return  HttpResponse("New line remove")
def spaceremove(request):
    return  HttpResponse("Remove space")
def charcount(request):
    return  HttpResponse("Char Count")
