from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    item_list = Hospital.objects.all()
    context = {
        'item_list' : item_list
    }
    return render(request, 'index.html', context)

def add_item(request):
    if request.method=='POST':
        name = request.POST['name']
        address = request.POST['address']
        contact = request.POST['contact']
        
        if name == '' or address == '' or contact == '':
            messages.warning(request, "Please insert the information")
            return redirect('index')
        
        else:
            item = Hospital(name = name, address = address, contact = contact)
            item.save()
            messages.info(request, "Item addedd successfully")
    else:
        pass

    item_list = Hospital.objects.all()
    context = {
        'item_list' : item_list
    }
    return render(request, 'index.html', context)


def delete_item(request, id):
    item = Hospital.objects.get(id=id)
    item.delete()
    messages.info(request, "Item deleted success")
    return redirect('index')

def edit_item(request, id):
    latest_item = Hospital.objects.get(id=id)
    item_list = Hospital.objects.all()
    context = {
        'latest_item' : latest_item,
        'item_list' : item_list
    }
    return render(request, 'index.html', context)

def update_item(request, id):
    item = Hospital.objects.get(id=id)
    item.name = request.POST['name']
    item.address = request.POST['address']
    item.contact = request.POST['contact']
    item.save()
    messages.info(request, "Item updated successfully")
    return redirect('index')
