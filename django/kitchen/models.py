from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from durationfield.db.models.fields.duration import DurationField

class Person(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField()

  def __unicode__(self):
    return " ".join([self.first_name, self.last_name])

class Customer(models.Model):
  member = models.ForeignKey(Person)
  credits = models.IntegerField()
  
  def __unicode__(self):
    return "%s:%s" % (self.member, self.credits)

class Line(models.Model):
  member = models.ForeignKey(Person)
  is_available = models.BooleanField()

  def __unicode__(self):
    return "%s:Available" % self.member if self.is_available else "%s:Unavailable" % self.member

class Party(models.Model):
  member = models.ForeignKey(Person)
  is_notified = models.BooleanField()
  is_approver = models.BooleanField()

  def __unicode__(self):
    n = "NOTIFY" if self.is_notified else "NOT_NOTIFIED"
    a = "APPROVER" if self.is_approver else "NOT_APPROVER"  
    return "%s:%s,%s" % (self.member, n, a)

class Expediter(models.Model):
  member = models.ForeignKey(Person)
  is_notified = models.BooleanField()

  def __unicode__(self):
    return "%s:NOTIFY" % self.member if self.is_notified else "%s:NOT_NOTIFIED" % self.member

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
  expediter = models.ForeignKey(Expediter)
  line = models.ManyToManyField(Line)
  party = models.ManyToManyField(Party)
  reservation_date = models.DateTimeField(blank=True, null=True)
  time_to_delivery = DurationField()
  priority = models.CharField(max_length=10, choices=Priority.choices)
  station = models.CharField(max_length=10, choices=Station.choices)

  def __unicode__(self):
    return self.name
