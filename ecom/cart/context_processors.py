from .cart import Cart

def cart(requests):
    return {'cart' : Cart(requests)}