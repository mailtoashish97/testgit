from django.http import HttpResponse
from django.shortcuts import render
def about(request):
        return render(request,'about.html')
def home(request):

    return render(request,'home.html' )

def count(request):
    fulltext =request.GET['fulltext']
    wordlist=fulltext.split()

    worddict={}

    for word in wordlist:
        if word in worddict:
            worddict[word] =worddict[word] + 1
        else:
            worddict[word]=1

    
    return render(request,'count.html',{'fulltext':wordlist,'count':len(wordlist),'worddict':worddict.items})  
    