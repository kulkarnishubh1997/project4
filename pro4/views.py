from django.shortcuts import render

def base(request):
    return render(request,"base.html")

def child(request):
    return render(request,"child.html")

def child1(request):
    return render(request,"child1.html")




