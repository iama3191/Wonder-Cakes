from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
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
                messages.success(request, f'Updated flavor{flavor.upper()} {product.name} quantity to {bag[item_id]["items_by_flavor"][flavor]}')
            else:
                bag[item_id]['items_by_flavor'][flavor] = quantity
                messages.success(request, f'Added flavor {flavor.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_flavor': {flavor: quantity}}
            messages.success(request, f'Added flavor {flavor.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, item_id):
    """ Update (adding or removing) the quantity of the 
    product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    flavor = None

    if 'product_flavor' in request.POST:
        flavor = request.POST['product_flavor']
    bag = request.session.get('bag', {})

    if flavor:
        if quantity > 0:
            bag[item_id]['items_by_flavor'][flavor] = quantity
            messages.success(request, f'Updated flavor {flavor.upper()} {product.name} quantity to {bag[item_id]["items_by_flavor"][flavor]}')
        else:
            del bag[item_id]['items_by_flavor'][flavor]
            if not bag[item_id]['items_by_flavor']:
                bag.pop(item_id)
            messages.success(request, f'Removed flavor {flavor.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the product from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        flavor = None
        if 'product_flavor' in request.POST:
            flavor = request.POST['product_flavor']
        bag = request.session.get('bag', {})

        if flavor:
            del bag[item_id]['items_by_flavor'][flavor]
            if not bag[item_id]['items_by_flavor']:
                bag.pop(item_id)
            messages.success(request, f'Removed flavor {flavor.upper()} {product.name} from your bag')

        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)