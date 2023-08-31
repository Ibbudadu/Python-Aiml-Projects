#i have created this file-ibbu
from django.http import  HttpResponse
from django.shortcuts import render


def index(request):

     return render(request, 'index.html')


def analyse(request):
    #get the text
    djtext= request.GET.get('text', 'default')
    #check checkbox value
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')

    #analysed = djtext
    if removepunc == "on":
         punctuations = '''!()-[]{};:"'\,<>./?@#$%^&*_~'''
         analysed = " "
         for char in djtext:
            if char not in punctuations:
               analysed = analysed + char
         params = {'purpose ': 'remove punc', 'analysed_text': analysed}
         return render(request, 'analyse.html', params )


    #analyse the text
    elif(fullcaps == 'on'):
        analysed = ' '
        for char in djtext:
            analysed = analysed + char.upper()

        params = {'purpose ': 'change to upper', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)

    elif(newlineremover ==" on"):
        for char in djtext:
            if char != '\n':
                analysed = analysed + char

        params = { 'purpose': 'removed Newlines', 'analysed_text': analysed }
        return render(request, 'analyse.html', params)


    else:
         return HttpResponse('error')

