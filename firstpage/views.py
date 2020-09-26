from django.shortcuts import render, get_object_or_404, redirect


def firstpage(request):
    return render(request, 'firstpage/firstpage.html')
