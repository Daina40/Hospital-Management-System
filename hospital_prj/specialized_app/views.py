from django.shortcuts import render, redirect
from .forms import SpecialityForm
from django.contrib import messages
from .models import *

# Create your views here.

def specialized_details(request):
    specialized = Speciality.objects.all()
    form = SpecialityForm()

    if request.method == 'POST':
        form = SpecialityForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Dr. Speciality added successfully")

    context = {
        'form' : form,
        'specialized' : specialized
    }
    
    return render(request, 'specialized.html', context)

def specialized_delete_item(request, id):
    specialized = Speciality.objects.get(id=id)
    specialized.delete()
    messages.info(request, 'Item deleted successfully')
    return redirect('specialized_details')

def specialized_edit_item(request, id):
    specializes = Speciality.objects.all()
    specialized = Speciality.objects.get(id=id)

    if request.method == 'POST':
        form = SpecialityForm(request.POST, instance=specialized)
        if form.is_valid():
            form.save()
            messages.info(request, "Patient updated successfully")
            return redirect('specialized_details')

    else:
        form = SpecialityForm(instance=specialized)

    context = {
        'form': form,
        'specializes' : specializes
    }
    return render(request, 'specialized_edit.html', context)