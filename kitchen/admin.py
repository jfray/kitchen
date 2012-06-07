from kitchen.models import Member
from kitchen.models import Order
from kitchen.models import Customer
from kitchen.models import Line
from kitchen.models import Party
from kitchen.models import Expediter

from django.contrib import admin

admin.site.register(Member)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Line)
admin.site.register(Party)
admin.site.register(Expediter)
