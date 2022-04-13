from django.http import HttpResponse
from django.shortcuts import render


def index(reauest):
    return render(reauest, 'index.html')


def analyze(reauest):

    djtext = reauest.POST.get('text', 'default')

    removepunc = reauest.POST.get('removepunc', 'off')
    fullcaps = reauest.POST.get('fullcaps','off')
    newline = reauest.POST.get('newline','off')
    extraspaceremover = reauest.POST.get('extraspaceremover','off')


    if removepunc == "on":
        punctuations = ''' !()::;;<>?@#'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'remove punctuation', 'analyzed_text': analyzed}
        #djtext = analyzed
        return render(reauest, 'analyze.html', params)
    if (fullcaps== "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'in UPPER CASE', 'analyzed_text': analyzed}
        #djtext = analyzed
        return render(reauest, 'analyze.html', params)


    if (extraspaceremover =="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1] == " "):

                analyzed= analyzed + char

        params = {'purpose': 'ExtraSpaces Remover', 'analyzed_text': analyzed}
        #djtext = analyzed
        return render(reauest, 'analyze.html', params)

    if (newline == "on"):
        analyzed = ""
        for char in djtext:
            if char!= "\n" and char!= "\r":
                    analyzed = analyzed + char

            params = {'purpose': 'NewLine remover', 'analyzed_text': analyzed}
            #djtext = analyzed
        if (removepunc != "on" and newline != "on" and fullcaps != "on" and extraspaceremover != "on"):
            return HttpResponse(" Error..!!Select atleat any one option")

        return render(reauest, 'analyze.html', params)




