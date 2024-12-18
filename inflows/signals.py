from django.db.models.signals import post_save
from django.dispatch import receiver
from inflows.models import Inflows


@receiver(post_save, sender=Inflows)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity += instance.quantity
            product.save()