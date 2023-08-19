from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  memberid = models.IntegerField(null=True)
  modifiedtime = models.DateField(null=True)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  def __str__(self):
    return self.lastname

class Client(models.Model):

  name = models.CharField(max_length=255)
  clientid = models.CharField(max_length=255)
  createtime = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  emailaddress = models.CharField(max_length=255)
  joined_date = models.DateField(null=True)
  memberid=models.ForeignKey(Member, on_delete=models.CASCADE)
  def __str__(self):
    return self.name


class Matters(models.Model):
  matters = models.CharField(max_length=255)
  matterid = models.IntegerField(null=True)
  narrative=models.CharField(max_length=255)
  createtime = models.DateField(null=True)
  memberid = models.IntegerField(null=True)
  mattersattachment=models.FileField(null=True)
  currentmattersituation=models.CharField(max_length=255)
  lastmattersituation = models.CharField(max_length=255)
  clientid=models.ForeignKey(Client, on_delete=models.CASCADE)
  def __str__(self):
    return self.matters


class Request(models.Model):
  name = models.CharField(max_length=255)
  requestid = models.IntegerField(null=True)
  createtime = models.DateField(null=True)
  requestattachment = models.FileField(null=True)
  currentrequestsituation = models.CharField(max_length=255)
  lastrequestsituation = models.CharField(max_length=255)
  matterid=models.ForeignKey(Matters, on_delete=models.CASCADE)
  def __str__(self):
    return self.name


# Create your models here.
