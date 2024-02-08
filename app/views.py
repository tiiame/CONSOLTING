from django.shortcuts import render
from.models import *
# Create your views here.
def index(request):

    banner = Banner.objects.all()
    static = Static.objects.first()
    servis = Servic.objects.all()
    results = Results.objects.all()
    Contakt = contakt.objects.all()
    Review = review.objects.all()
    Social = social.objects.all()

    context = {"Banner": Banner,
               "Static": Static,
               "Servic":Servic,
               "Results":Results,
               "contakt":contakt,
               "review":review,
               "social":social,
               }



    return render(request, 'index.html', context)
