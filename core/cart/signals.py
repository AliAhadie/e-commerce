from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .cart import CartSession


@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    cart = CartSession(request.session)
    print(cart)
    cart.sync_cart_from_db(user)

@receiver(user_logged_out)
def post_logout(sender, user, request, **kwargs):
    cart = CartSession(request.session)
    cart.merge_cart_from_session_to_db(user)
    # Explicitly save the session if needed
    request.session.save()