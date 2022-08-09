from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import DwellerForm
from .models import Monarch, Dweller, Peasant


def home(request):
    return render(request, 'home.html', {})


@login_required(login_url='/users/sign_in/')
def hierarchy(request, value):
    king = Monarch.objects.get()
    seniors = king.senior_set.all().order_by('-id')
    search = request.GET.get('search')

    if value == 'seniors':
        return render(
            request,
            'hierarchy.html',
            {"king": king, 'value': value, 'seniors': seniors})

    if value == 'dwellers' or search:
        dwellers = Dweller.objects.all().order_by('-id')

        dwellers = dwellers.filter(
            Q(first_name__icontains=search)
            | Q(last_name__icontains=search)
            | Q(social_status__icontains=search)
            | Q(salary_per_month__icontains=search)
            | Q(obeys_to__first_name__icontains=search)
            | Q(obeys_to__last_name__icontains=search)
            | Q(age__icontains=search)) if search else dwellers

        return render(
            request,
            'hierarchy.html',
            {"king": king, 'value': value, 'dwellers': dwellers})

    if value == 'peasants':
        peasants = Peasant.objects.all().order_by('-owner_id')

        return render(
            request,
            'hierarchy.html',
            {"king": king, 'value': value, 'peasants': peasants})

    return render(
        request,
        'hierarchy.html',
        {"king": king, 'value': value, })


def create_dweller(request):
    form = DwellerForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        instance = form.save(commit=False)
        if instance.social_status == 'Merchant':
            instance.salary_per_month = 200
        elif instance.social_status == 'Landlord':
            instance.salary_per_month = 500
        elif instance.social_status == 'Knight':
            instance.salary_per_month = 1000
        instance.save()
        return redirect('estates:hierarchy', value='dwellers')
    return render(request, 'create_dweller.html', {'form': form})


def edit_dweller(request, pk):
    dweller = Dweller.objects.get(pk=pk)

    form = DwellerForm(request.POST or None, instance=dweller)
    if form.is_valid() and request.method == 'POST':
        instance = form.save(commit=False)
        if instance.social_status == 'Merchant':
            instance.salary_per_month = 200
        elif instance.social_status == 'Landlord':
            instance.salary_per_month = 500
        elif instance.social_status == 'Knight':
            instance.salary_per_month = 1000
        instance.save()
        return redirect('estates:hierarchy', value='dwellers')
    return render(request, 'edit_dweller.html', {'form': form, 'dweller': dweller})


def delete_dweller(request, pk):
    Dweller.objects.get(pk=pk).delete()
    return redirect('estates:hierarchy', value='dwellers')
