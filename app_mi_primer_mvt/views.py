from django.shortcuts import render
from django.http import HttpResponse
from app_mi_primer_mvt.models import concesionario




def concesionario_1(request):
    context={}
    context["concesionario"]= concesionario.objects.all()
    return render(request, "app_primer_mvt/concesionario_1.html", context)