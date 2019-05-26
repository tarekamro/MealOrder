from orders.models import Order
from django.shortcuts import render


def view_orders(request):
    orders = Order.objects.all()

    context = {'orders': orders}
    return render(request, 'admin_view.html', context)
