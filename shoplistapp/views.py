from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Shoplistclass #j imports model we created
from .forms import ListForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView

#views connect models and templates

# Create your views here.
class ItemList(ListView):
    model = Shoplistclass
    template_name = 'shoplistapp/shop_list.html'


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

 
class ItemCreate(CreateView):   
    model = Shoplistclass
    fields = ['item','urgency', 'shop', 'quantity', 'category']
    template_name = 'shoplistapp/item_edit.html'
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ItemCreate, self).form_valid(form)

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
