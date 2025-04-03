
from django.dispatch import Signal

# Define a signal
order_created = Signal(providing_args=["order", "user"])

# In your view or wherever the event occurs
order_created.send(sender=self.__class__, order=order, user=request.user)

# receive the signal
@receiver(order_created)
def handle_order_created(sender, order, user, **kwargs):
    print(f"Order {order.id} created by {user.username}")
