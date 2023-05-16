from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .models import Item
from .forms import NewItemForm, EditItemForm


def items(request):
    query = request.GET.get('query', '')

    items = Item.objects.filter(is_sold=False,)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
    })


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk) # pk=pk one side is the primary key on the models(Item) itself and the other is the one we get from the url.
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
    })


@login_required
def new(request):
    if request.method=='POST':
        form = NewItemForm(request.POST, request.FILES) 
        """
        request.FILES: get file upload(dictionary). <form> that posted to the request had enctype="multipart/form-data", Otherise this dictionary will be empty.
        """

        if form.is_valid():
            item = form.save(commit=False)
            """
            commit=False: if we save item now, created_by won't be added
            """
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
    return render(request, 'item/form.html', {
        'form': form, 
        'title': 'New Item',
        
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })



@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return render(request, redirect('dashboard:index'))
