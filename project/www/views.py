# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Industry, Offer, AcceptedOffer
from .forms import OfferForm

def index(request):
    if request.method == 'POST':
        form = OfferForm(request.POST, request.FILES)
        if form.is_valid():
            offer = form.save()
            selected_industries = offer.industry.all().values_list('name', flat=True)
            return render(request, 'www/index.html', {'offer_form': OfferForm(), 'offer': offer, 'selected_industries': selected_industries})
    else:
        form = OfferForm()
    return render(request, 'www/index.html', {'offer_form': form})

def accept_offer(request):
    if request.method == "POST":
        offer_id = request.POST.get("offer_id")
        offer = get_object_or_404(Offer, pk=offer_id)

        # Create an AcceptedOffer object based on the offer data
        accepted_offer = AcceptedOffer.objects.create(
            name=offer.name,
            surname=offer.surname,
            mail=offer.mail,
            number=offer.number,
            price = offer.price,
            photo=offer.photo,
            text=offer.text,
            
        )

        # Copy industry relations
        
        accepted_offer.industry.set(offer.industry.all())
        # Delete the offer after accepting it
        offer.delete()
        
        return redirect('index2')

def index2(request):
    accepted_offers = AcceptedOffer.objects.all()
    return render(request, 'www/index2.html', {'accepted_offers': accepted_offers})
