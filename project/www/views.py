from django.shortcuts import render
from .models import Industry,Offer
from .forms import OfferForm

industry = Industry.objects.all()
offer = Offer.objects.all()



def index(request):
    offer_form = OfferForm()  # Create an instance of the OfferForm
    return render(request, 'www/index.html', {'offer_form': offer_form})




def index2(request):

    return render(request, 'www/index2.html', {})
