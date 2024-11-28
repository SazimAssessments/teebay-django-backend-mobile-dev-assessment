from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Purchase, Rent
from firebase_admin import messaging
import logging

@receiver(post_save, sender=Purchase)
def send_notification_on_purchase(sender, instance: Purchase, created, **kwargs):
    if created:
        fcm_token = instance.product.seller.firebase_console_manager_token

        message = messaging.Message(
            notification=messaging.Notification(
                title="Your Product has been purchased",
                body=f"{instance.product.title} has been purchased by {instance.buyer.first_name}",
            ),
            data={'product_id': str(instance.id)},
            token=fcm_token
        )

        try:
            response = messaging.send(message)
            logging.critical(f'Successfully sent push notification {response}')

        except Exception as e:
            logging.critical(f'Error sending push notification: {e}')


@receiver(post_save, sender=Rent)
def send_notification_on_rent(sender, instance: Purchase, created, **kwargs):
    if created:
        fcm_token = instance.product.seller.firebase_console_manager_token

        message = messaging.Message(
            notification=messaging.Notification(
                title="Your Product has been rented",
                body=f"{instance.product.title} has been rented by {instance.buyer.first_name}",
            ),
            data={'product_id': str(instance.id)},
            token=fcm_token
        )

        try:
            response = messaging.send(message)
            logging.info(f'Successfully sent push notification {response}')

        except Exception as e:
            logging.critical(f'Error sending push notification: {e}')
