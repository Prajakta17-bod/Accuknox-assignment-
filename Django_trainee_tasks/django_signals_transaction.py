from django.db import transaction
from django.dispatch import Signal, receiver
from django.db import models


my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Receiver executed")
    
    raise Exception("Simulated error")


class MyModel(models.Model):
    name = models.CharField(max_length=100)


try:
    with transaction.atomic():
        print("Creating instance...")
        MyModel.objects.create(name="Test")
        my_signal.send(sender=None)
except Exception as e:
  print(f"Transaction rolled back due to: {e}")
