from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """A view to return the shopping bag page"""
   
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    flavor = None

    if 'product_flavor' in request.POST:
        flavor = request.POST['product_flavor']
    bag = request.session.get('bag', {})

    if flavor:
        if item_id in list(bag.keys()):
            if flavor in bag[item_id]['items_by_flavor'].keys():
                bag[item_id]['items_by_flavor'][flavor] += quantity
            else:
                bag[item_id]['items_by_flavor'][flavor] = quantity
        else:
            bag[item_id] = {'items_by_flavor': {flavor: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, item_id):
    """ Update (adding or removing) the quantity of the 
    product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    flavor = None

    if 'product_flavor' in request.POST:
        flavor = request.POST['product_flavor']
    bag = request.session.get('bag', {})

    if flavor:
        if quantity > 0:
            bag[item_id]['items_by_flavor'][flavor] = quantity
        else:
            del bag[item_id]['items_by_flavor'][flavor]
            if not bag[item_id]['items_by_flavor']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the product from the shopping bag """

    try:
        flavor = None
        if 'product_flavor' in request.POST:
            flavor = request.POST['product_flavor']
        bag = request.session.get('bag', {})

        if flavor:
            del bag[item_id]['items_by_flavor'][flavor]
            if not bag[item_id]['items_by_flavor']:
                bag.pop(item_id)

        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)