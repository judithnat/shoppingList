from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Shoplistclass #j imports model we created
from .forms import ListForm

#views connect models and templates

# Create your views here.
def shop_list(request): 
    items = Shoplistclass.objects.all()  #j queryset called items
    context = {
        'items':items
    }
    return render(request,'shoplistapp/shop_list.html', context)  #shop_list funct puts together template

def item_detail(request, pk):
    item = get_object_or_404(Shoplistclass, pk=pk)    #j queryset? pk= primary key, way of asking for objects
    context = {
        'item':item
    }
    return render(request, 'shoplistapp/item_detail.html', context) #j funct render args are 
    # request, what user wants, and xx.html, template to put it in, context

def urgency(request, pk):
    items = Shoplistclass.filter(urgency = 'UR')   #j queryset
    context = {
        'items':items
    }
    return render(request,'shoplistapp/urgency.html', context)

def item_new(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = User.objects.all()[0]
            item.entered_date = timezone.now()
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ListForm()
        context = {
        'form':form  
    }
    return render(request, 'shoplistapp/item_edit.html', context)  
    #contect in curly brackets is info to go in template
                
def item_edit(request, pk):
    item = get_object_or_404(Shoplistclass, pk=pk)
    if request.method == "POST":
        form = ListForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = User.objects.all()[0]
            item.entered_date = timezone.now()
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ListForm(instance=item)
        context = {
        'form':form
    }
    return render(request, 'shoplistapp/item_edit.html', context)
