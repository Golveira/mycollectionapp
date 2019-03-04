from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Collection, Item, Category
from .forms import NewCollectionForm, NewItemForm


@login_required
def collections_list(request):
    categories = Category.objects.all()
    collections = Collection.objects.filter(user=request.user)
    context = {
        'collections': collections,
        'categories': categories,
    }
    return render(request, 'collection/collections_list.html', context)


@login_required
def category_filter(request, id):
    category = get_object_or_404(Category, id=id)
    user_collections = request.user.collection_set.all()
    filtred_collections = user_collections.filter(category=category)
    context = {
        'category_name': category.name,
        'collections': filtred_collections
    }
    return render(request, 'collection/category_filter.html', context)


@login_required
def collection_items(request, id):
    collection = Collection.objects.get(id=id)
    items = collection.item_set.all()
    context = {
        'collection': collection,
        'items': items
    }
    return render(request, 'collection/collection_items_list.html', context)


@login_required
def new_collection(request):
    if request.method == 'POST':
        form = NewCollectionForm(
            request.POST, request.FILES)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.user = request.user
            collection.save()
            return redirect('collection_list')
    else:
        form = NewCollectionForm()
    return render(request, 'collection/new_collection_form.html', {'form': form})


@login_required
def edit_collection(request, id):
    collection = get_object_or_404(Collection, id=id)
    if request.method == 'POST':
        form = NewCollectionForm(request.POST, request.FILES, instance=collection)
        if form.is_valid():
            form.save()
            return redirect('collection_items', id=collection.id)
    else:
        form = NewCollectionForm(instance=collection)
    return render(request, 'collection/edit_collection_form.html', {'form': form})


@login_required
def delete_collection(request, id):
    collection = get_object_or_404(Collection, id=id)
    collection.delete()
    return redirect('collection_list')


@login_required
def item_info(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('collection_items', id=item.collection.id)
    else:
        form = NewItemForm(instance=item)
    return render(request, 'collection/item_info_form.html', {'form': form, 'item': item})


@login_required
def new_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('collection_items', id=item.collection.id)
    else:
        form = NewItemForm(user=request.user)
    return render(request, 'collection/new_item_form.html', {'form': form})


@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    item.delete()
    return redirect('collection_items', id=item.collection.id)

