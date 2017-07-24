from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "Crunchy!"}
    return render(request, 'rango/index.html', context=context_dict)
