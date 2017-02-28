from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

consent_value = (
    ('Yes', 'Yes'),
    ('No', 'No'),)

litter_value = (
    ('Yes', 'Yes'),
    ('No', 'No'),)

spine_board_value = (
    ('Yes', 'Yes'),
    ('No', 'No'),)

scoop_value = (
    ('Yes', 'Yes'),
    ('No', 'No'),)

ked_value = (
    ('Yes', 'Yes'),
    ('No', 'No'),)

hard_collar_value = (
    ('Yes', 'Yes'),
    ('No', 'No'),)

traction_splint_value = (
    ('Yes', 'Yes'),
    ('No', 'No'),)

splint_value  = (
    ('Yes', 'Yes'),
    ('No', 'No'),)

float_blanket_value  = (
    ('Yes', 'Yes'),
    ('No', 'No'),)

inhalation_value  = (
    ('Yes', 'Yes'),
    ('No', 'No'),)


hot_cold_pack_value  = (
    ('Yes', 'Yes'),
    ('No', 'No'),)

burn_dressing_value  = (
    ('Yes', 'Yes'),
    ('No', 'No'),)

entonox_value  = (
    ('Yes', 'Yes'),
    ('No', 'No'),)

aed_value  = (
    ('Yes', 'Yes'),
    ('No', 'No'),)

rs_sign_value  = (
    ('Yes', 'Yes'),
    ('No', 'No'),)

co_sign  = (
    ('Yes', 'Yes'),
    ('No', 'No'),)

gender_value  = (
    ('Female', 'Female'),
    ('Male', 'Male'),)

airway_value = (
    ('Oro', 'Oro'),
    ('Naso', 'Naso'),)

severity_value = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
)



# Create your models here.
class RescueSpecialist(models.Model):
    user_name = models.CharField(max_length=200, blank=False)
    pwd = models.CharField(max_length=50, blank=False)
    emailid = models.EmailField(max_length=50, blank=False)

    def __str__(self):
        return self.user_name


class PatientRecord(models.Model):
    surname = models.CharField(max_length=200, blank=False)
    given_name = models.CharField(max_length=200, blank=False)
    address = models.TextField(max_length=500, blank=False)
    telephone = models.CharField(max_length=12, blank=False)
    weight = models.CharField(max_length=10, blank=False)
    bday = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=20,choices=gender_value)
    contact_form = models.CharField(max_length=100, blank=False)
    date = models.DateField()
    SAR_incident_no = models.CharField(primary_key=True, max_length=50, unique=True, null=False)
    date_of_injury = models.DateTimeField()
    place_first_seen = models.CharField(max_length=50)
    transferred_to = models.CharField(max_length=100)
    transferred_from = models.CharField(max_length=100)
    consent = models.CharField(max_length=50, choices=consent_value)
    chief_complaint = models.TextField(max_length=5000)
    mechanism_of_injury = models.TextField(max_length=5000)
    found_on_examination = models.TextField(max_length=5000)
    symptoms = models.TextField(max_length=500)
    allergies = models.TextField(max_length=500)
    medications = models.TextField(max_length=500)
    pertinent_past_history = models.TextField(max_length=500)
    last_meal = models.TextField(max_length=500)
    events_prior_emergency = models.TextField(max_length=500)
    onset = models.CharField(max_length=50)
    provocation = models.CharField(max_length=50)
    quality = models.CharField(max_length=50)
    radiations = models.CharField(max_length=50)
    severity = models.CharField(max_length=50,choices=severity_value)
    time_sec_assessment = models.TimeField()
    head_neck = models.TextField(max_length=1000)
    chest = models.TextField(max_length=1000)
    cardio_vascular = models.TextField(max_length=1000)
    abdomen = models.TextField(max_length=1000)
    pelvis = models.TextField(max_length=1000)
    back = models.TextField(max_length=1000)
    extremities = models.TextField(max_length=1000)
    neurological = models.TextField(max_length=1000)
    blood_loss = models.TextField(max_length=1000)
    o2_mask_type = models.TextField(max_length=1000)
    time_onn_of = models.TimeField()
    flow_rate = models.TextField(max_length=1000)
    airway_type = models.CharField(max_length=50,choices=airway_value)
    airway_size = models.IntegerField()
    treatment_plan = models.TextField(max_length=10000)
    basket_litter = models.CharField(max_length=50,choices=litter_value)
    spine_board = models.CharField(max_length=50,choices=spine_board_value)
    scoop = models.CharField(max_length=50,choices=scoop_value)
    ked = models.CharField(max_length=50,choices=ked_value)
    hard_collar = models.CharField(max_length=50,choices=hard_collar_value)
    traction_splint = models.CharField(max_length=50,choices=traction_splint_value)
    splint = models.CharField(max_length=50,choices=splint_value)
    float_blanket = models.CharField(max_length=50,choices=float_blanket_value)
    inhalation = models.CharField(max_length=50,choices=inhalation_value)
    hot_cold_pack = models.CharField(max_length=50,choices=hot_cold_pack_value)
    burn_dressing = models.CharField(max_length=50,choices=burn_dressing_value)
    entonox = models.CharField(max_length=50,choices=entonox_value)
    aed = models.CharField(max_length=50,choices=aed_value)
    other = models.TextField(max_length=1000)
    personal_effects = models.TextField(max_length=10000)
    rescue_sp_name = models.CharField(max_length=50,blank=False)
    rs_sign = models.CharField(max_length=50,choices=rs_sign_value)
    date_rs = models.DateField()
    vessel = models.TextField(max_length=5000)
    co_sign = models.CharField(max_length=50,choices=co_sign)
    date_co = models.DateField()

class Vital_Signs(models.Model):
    pt_sar_inc_no = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
    time_obsvd = models.TimeField()
    loc = models.TextField(max_length=500)
    pulse = models.TextField(max_length=500)
    respiration = models.TextField(max_length=500)
    pupils = models.TextField(max_length=500)
    skin = models.TextField(max_length=500)
    bp = models.TextField(max_length=500)
    temp = models.TextField(max_length=500)
    sat_perc = models.IntegerField()


class Procedures(models.Model):
    md_sar_inc_no = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
    time_on_off = models.TimeField()
    medications = models.TextField(max_length=500)
    results = models.TextField(max_length=500)

class Physicians_Order(models.Model):
    ph_sar_inc_no = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
    times = models.TimeField()
    orders = models.TextField(max_length=500)
    doctors_name = models.TextField(max_length=500)
    facility = models.TextField(max_length=500)
