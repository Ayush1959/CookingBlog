from django.shortcuts import render


def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you like to contact us, Please email at', 'srihari.ayush@gmail.com']})
