from django.shortcuts import render
from django.http import HttpResponseRedirect


def directory(request):
    if request.method == 'GET':
        return render(request, 'corsairDirectory/corsair-directory.html')


def templates(request):
    if request.method == 'GET':
        return render(request, 'templates/corsairDirectory/directory.js')