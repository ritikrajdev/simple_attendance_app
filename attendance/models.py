from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    client_name = models.CharField(max_length=100)
    head_office = models.CharField(max_length=100)
    contact_person_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=16)

    def __str__(self):
        return self.client_name


class Vendor(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    vendor_name = models.CharField(max_length=100)
    office_address = models.CharField(max_length=500)
    contact_person = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=16)

    def __str__(self):
        return self.vendor_name


class SubVendor(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    sub_vendor_name = models.CharField(max_length=100)
    office_address = models.CharField(max_length=500)
    contact_person = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=16)

    def __str__(self):
        return self.sub_vendor_name


class Team(models.Model):
    sub_vendor = models.ForeignKey(SubVendor, on_delete=models.CASCADE)

    team_name = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100, blank=True)
    team_leader = models.CharField(max_length=100, blank=True)
    crt_date = models.DateField()
    location = models.CharField(max_length=500)

    def __str__(self):
        return self.team_name


class Employee(models.Model):
    KYC_DOCUMENT = (
        ('aadhaar', 'AADHAAR'),
        ('voter', 'Voter'),
        ('ration', 'Ration'),
        ('pan', 'PAN')
    )

    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    promoter_id = models.CharField(max_length=100)
    promoter_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    pin_code = models.CharField(max_length=10, blank=True)
    date_of_joining = models.DateField(blank=True)
    date_of_leaving = models.DateField(blank=True)
    kyc_document_type = models.CharField(max_length=10, choices=KYC_DOCUMENT, blank=True)
    kyc_document_number = models.CharField(max_length=20, blank=True)
    wage = models.IntegerField(blank=True)
    bank_name = models.CharField(max_length=100, blank=True)
    name_on_account = models.CharField(max_length=100, blank=True)
    account_number = models.CharField(max_length=20, blank=True)
    ifsc_code = models.CharField(max_length=20, blank=True)
    blood_group = models.CharField(max_length=10, blank=True)
    emergency_number = models.CharField(max_length=16, blank=True)

    # TODO: id Proof, Photo, Address Proof

    def __str__(self):
        return self.promoter_name


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    time_manday = models.CharField(max_length=10, default='0')
    sale_manday = models.CharField(max_length=10, default='0')
    date = models.DateField()

    def __str__(self):
        return self.employee.promoter_id
