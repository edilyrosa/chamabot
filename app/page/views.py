from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
  return HttpResponse("<h1>Bienvenido a: quien quieres ser?</h1>")

def resultados(request):
  return render(request, "paginas/resultados.html")

def index(request):
  return render(request, "paginas/index.html")