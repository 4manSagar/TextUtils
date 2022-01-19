# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def navigator(request):
    return HttpResponse('''<h1>My Personal Navigator</h1><br><br>
                        <ul>
                            <li><a href="https://www.youtube.com">YouTube</a></li>
                            <li><a href="https://www.google.com">Google</a></li>
                            <li><a href="https://www.facebook.com/">Facebook</a></li>
                            <li><a href="https://www.amazon.in">Amazon</a></li>
                            <li><a href="https://poki.com/">Poki games</a></li>
                        </ul><br><br>
                        <button><a href="/">Go back</a></button>
                        ''')


def index(request):
    return render(request, 'index.html')


def analyze(request):

    djtext = request.POST.get('text', 'no text')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    purpose = ""
    if removepunc == "on":
        purpose += "| Remove Punctuations "
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        djtext = analyzed

    if fullcaps == "on":
        purpose += "| Capitalize "
        djtext = djtext.upper()

    if newlineremover == "on":
        purpose += "| Remove new lines "
        analyzed = ""

        for char in djtext:
            if char != '\r' and char != '\n':
                analyzed += char

        djtext = analyzed

    if extraspaceremover == "on":
        purpose += "| Remove extra spaces "
        analyzed = ""
        for i, char in enumerate(djtext):
            if not(djtext[i] == " " and djtext[i+1] == " "):
                analyzed += char
        djtext = analyzed
    purpose += "|"
    params = {'analyzed_text': djtext, 'purpose': purpose}
    return render(request, 'analyze.html', params)
