"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add: # loop over items in items to add
        current_cart.setdefault(item, 0) # set the default value of each item to 1 
        current_cart[item] += 1
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    cart = {}
    for item in notes:
        cart.setdefault(item, 1)
    return cart

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    fulfillment = {}
    for item,count in cart.items():
        aisle, needs_fridge = aisle_mapping[item]
        fulfillment[item]=[count, aisle, needs_fridge]
    reverse_sort = dict(sorted(fulfillment.items(),reverse=True))
    return reverse_sort


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for item, order_details in fulfillment_cart.items():
        if item in store_inventory:
            order_quantity = order_details[0]
            current_quantity = store_inventory[item][0]
            
            new_quantity = current_quantity - order_quantity
            
            if new_quantity <= 0:
                store_inventory[item][0] = 'Out of Stock'
            else:
                store_inventory[item][0] = new_quantity
    
    return store_inventory
