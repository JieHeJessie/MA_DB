from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    pro_id = models.AutoField(primary_key=True)
    node = models.CharField(max_length=20,blank=True, null=True)
    pro_date = models.DateField(blank=True, null=True)
    project_name = models.CharField(max_length=50, blank=True, null=True)
    service = models.CharField(max_length=45, blank=True, null=True)
    instrument = models.CharField(max_length=45, blank=True, null=True)
    person = models.CharField(max_length=45, blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    num_sample = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=20,blank=True, null=True)
    int_ext = models.CharField(max_length=3, blank=True, null=True)
    state = models.CharField(max_length=3, blank=True, null=True)
    country = models.CharField(max_length=11, blank=True, null=True)
    user_define1 = models.CharField(max_length=20,blank=True, null=True)
    user_define2 = models.CharField(max_length=20,blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cus_count = models.CharField(max_length=1, blank=True, null=True)

class Node(models.Model):
    node_name=models.CharField(max_length=40)
    node_abbr=models.CharField(max_length=10)


class user(models.Model):
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=40)

class invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_date = models.DateField(blank=True, null=True)
    invoice_num = models.CharField(max_length=50,blank=True, null=True)
    bad_debt = models.CharField(max_length=20,blank=True, null=True)
    quote = models.CharField(max_length=20,blank=True, null=True)
    paid = models.CharField(max_length=20,blank=True,null=True)
    ma_staff = models.CharField(max_length=20,blank=True,null=True)
    project_invoice = models.CharField(max_length=50,blank=True,null=True)
    service_type = models.CharField(max_length=20,blank=True,null=True)
    instrument = models.CharField(max_length=20,blank=True,null=True)
    person_invoice = models.CharField(max_length=50,blank=True,null=True)
    address = models.CharField(max_length=50,blank=True,null=True)
    no_sample_in = models.CharField(max_length=20,blank=True,null=True)
    category_in = models.CharField(max_length=20,blank=True,null=True)
    int_ext_in = models.CharField(max_length=20,blank=True,null=True)
    user_define1_in = models.CharField(max_length=20,blank=True,null=True)
    user_define2_in = models.CharField(max_length=20,blank=True,null=True)
    sub_total_in = models.CharField(max_length=20,blank=True,null=True)
    reconciliation = models.CharField(max_length=20,blank=True,null=True)
    running_total = models.CharField(max_length=20,blank=True,null=True)


class quote(models.Model):
    quote_id = models.AutoField(primary_key=True)
    quote_num = models.CharField(max_length=50, blank=True, null=True)
    quote_year = models.CharField(max_length=50, blank=True, null=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    concatenate = models.CharField(max_length=50, blank=True, null=True)
    client = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    quote_staff = models.CharField(max_length=50, blank=True, null=True)
    quote_date = models.DateField(blank=True, null=True)
    quote_value = models.CharField(max_length=50, blank=True, null=True)
    grant_not = models.CharField(max_length=50, blank=True, null=True)
    accept = models.CharField(max_length=50, blank=True, null=True)
    invoiced_not = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)




class ImportFile(models.Model):

    file = models.FileField(upload_to='File')
    name = models.CharField(max_length=50, verbose_name=u'filename')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name







