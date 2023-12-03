from django.shortcuts import render, get_object_or_404, redirect

from accounts.models import UserProfile
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required

@login_required
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

@login_required
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_detail.html', {'item': item})

@login_required
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            return redirect('shop:item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})

@login_required
def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('shop:item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form})

@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('shop:item_list')
    return render(request, 'item_confirm_delete.html',{'item':item})


def items_purchased(request):
    current_user_profile = UserProfile.objects.get(user=request.user)
    purchased_items = current_user_profile.items_purchased.all()
    return render(request, 'purchased_items.html', {'purchased_items': purchased_items})

def add_item_to_purchased(request, item_id):
    item = Item.objects.get(pk=item_id)
    current_user_profile = UserProfile.objects.get(user=request.user)
    current_user_profile.items_purchased.add(item)
    return redirect('shop:purchased_items')

def remove_item_from_purchased(request, item_id):
    item = Item.objects.get(pk=item_id)
    current_user_profile = UserProfile.objects.get(user=request.user)
    current_user_profile.items_purchased.remove(item)
    return redirect('shop:purchased_items')

