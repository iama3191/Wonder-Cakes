from django.shortcuts import render, redirect


def view_bag(request):
    """A view to return the shopping bag page"""
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the product to the shopping bag """

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

    request.session['bag'] = bag
    return redirect(redirect_url)