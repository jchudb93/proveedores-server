from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
admin.site.register(StrategicGoal)
admin.site.register(Service)
admin.site.register(Contract)
admin.site.register(Provider)
admin.site.register(Supplier)
admin.site.register(Task)
admin.site.register(Agreement)
admin.site.register(Incident)