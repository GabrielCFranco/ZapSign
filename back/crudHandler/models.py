from django.db import models

class Company(models.Model):
    company_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    api_token = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Documents(models.Model):
    documents_ID = models.AutoField(primary_key=True)
    open_id = models.IntegerField()
    token = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=True, default=None)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255)
    companyID = models.ForeignKey("Company", on_delete=models.CASCADE)
    externalID = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Signers(models.Model):
    signers_ID = models.AutoField(primary_key=True)
    token = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    externalID = models.CharField(max_length=255, null=True)
    documentID = models.ForeignKey("Documents", on_delete=models.CASCADE)

    def __str__(self):
        return self.name