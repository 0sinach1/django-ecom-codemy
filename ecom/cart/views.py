from django.shortcuts import render

def cart_summary(requests):
    return render(requests, 'card_summary.html', {})

def cart_add(requests):
    pass

def cart_delete(requests):
    pass

def cart_update(requests):
    pass