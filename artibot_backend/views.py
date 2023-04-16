from django.shortcuts import render 

def index( request ): 
    return render( request, 'index.html', context={
        "title": "Hello World",
    })

def chatbot( request ): 
    return render( request, 'index2.html', context={
        "title" : "Artibot Chatbot"
    })