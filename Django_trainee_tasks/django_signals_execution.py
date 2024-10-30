from django.dispatch import Signal, receiver
import time

my_signal = Signal()


@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Receiver started")
    time.sleep(2)  
    print("Receiver finished")

print("Sending signal...")
my_signal.send(sender=None)
print("Signal sent.")


