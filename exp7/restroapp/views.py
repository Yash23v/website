from django.shortcuts import render
def restrohome(request):
    return render(request,'restro.html')
def menupage(request):
    return render(request,'menu.html')
def adminpage(request):
    return render(request,'administration.html')
def contactus(request):
    return render(request,'contact.html')
