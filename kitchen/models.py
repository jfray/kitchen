from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from durationfield.db.models.fields.duration import DurationField

class KitchenUser(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField()
  
  def __unicode__(self):
    return " ".join([self.first_name, self.last_name])

class Station(DjangoChoices):
  cooking = ChoiceItem("cooking")
  thawed = ChoiceItem("thawed")
  frozen = ChoiceItem("frozen")
  burnt = ChoiceItem("burnt")

class Priority(DjangoChoices):
  high = ChoiceItem("high")
  medium = ChoiceItem("medium")
  low = ChoiceItem("low")

class Order(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()
  expo = models.ForeignKey(KitchenUser)
  line = models.ManyToManyField(KitchenUser, related_name="%(app_label)s_%(class)s_related_line")
  party = models.ManyToManyField(KitchenUser, related_name="%(app_label)s_%(class)s_related_party")
  reservation_date = models.DateTimeField(blank=True, null=True)
  time_to_delivery = DurationField()
  priority = models.CharField(max_length=10, choices=Priority.choices)
  station = models.CharField(max_length=10, choices=Station.choices)

  def __unicode__(self):
    return self.name
