from django.contrib import admin
from .models import RescueSpecialist
from .models import PatientRecord
from .models import Physicians_Order
from .models import Procedures
from .models import Vital_Signs

# Register your models here.
admin.site.register(RescueSpecialist)
admin.site.register(PatientRecord)
admin.site.register(Physicians_Order)
admin.site.register(Procedures)
admin.site.register(Vital_Signs)