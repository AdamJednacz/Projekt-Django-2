# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import  Offer, AcceptedOffer, Like, Unlike
from .forms import OfferForm

def index(request):
    if request.method == 'POST':
        form = OfferForm(request.POST, request.FILES)
        if form.is_valid():
            offer = form.save()
            selected_industries = offer.industry.all().values_list('name', flat=True)
            return render(request, 'www/index.html', {'offer_form': OfferForm(), 'offer': offer, 'selected_industries': selected_industries })
    else:
        form = OfferForm()
    return render(request, 'www/index.html', {'offer_form': form})

def accept_offer(request):
    if request.method == "POST":
        offer_id = request.POST.get("offer_id")
        offer = get_object_or_404(Offer, pk=offer_id)
        accepted_offer = AcceptedOffer.objects.create(
            name=offer.name,
            surname=offer.surname,
            mail=offer.mail,
            number=offer.number,
            price = offer.price,
            photo=offer.photo,
            text=offer.text,
        )
        accepted_offer.industry.set(offer.industry.all())
        offer.delete()
        return redirect('index2')
    else:
        return redirect('index2')
def index2(request):
    accepted_offers = AcceptedOffer.objects.all()

    return render(request, 'www/index2.html', {'accepted_offers': accepted_offers})

def like(request):
    if request.method == 'POST':
        accept_offer_id = request.POST.get('accept_offer_id')
        accept_offer = get_object_or_404(AcceptedOffer, id=accept_offer_id)
        like, created = Like.objects.get_or_create(accept_offer=accept_offer)
        if not created:
            like.delete()
        return redirect('index2')

def unlike(request):
    if request.method == 'POST':
        accept_offer_id = request.POST.get('accept_offer_id')
        accept_offer = get_object_or_404(AcceptedOffer, id=accept_offer_id)
        unlike, created = Unlike.objects.get_or_create(accept_offer=accept_offer)
        if not created:
            unlike.delete()
        return redirect('index2')