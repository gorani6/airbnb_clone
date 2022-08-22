from tkinter import CASCADE, N
from django.db import models
from core import models as core_models
from django.utils import timezone

# Create your models here.

class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    STATUS_PENDIG = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDIG, "pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANCELED, "canceled"),
    )

    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDIG)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", related_name='reservations', on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", related_name="reservations", on_delete=CASCADE)

    def __str__(self):
        return f'{self.room} = {self.check_in}'

    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    in_progress.boolean = True


    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out
    
    is_finished.boolean = True