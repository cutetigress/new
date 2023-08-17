from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  memberid = models.IntegerField(null=True)
  modifiedtime = models.DateField(null=True)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

class Client(models.Model):

  name = models.CharField(max_length=255)
  clientid = models.CharField(max_length=255)
  createtime = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  memberid = models.IntegerField(null=True)

  def __str__(self):
    return f"{self.name}"


class Matters(models.Model):
  subjectmatters = models.CharField(max_length=255)
  matterid = models.IntegerField(null=True)
  narrative=models.CharField(max_length=255)
  createtime = models.DateField(null=True)
  clientnumber = models.IntegerField(null=True)
  memberid = models.IntegerField(null=True)
  mattersattachment=models.FileField(null=True)
  currentmattersituation=models.CharField(max_length=255)
  lastmattersituation = models.CharField(max_length=255)
  def __str__(self):
    return f"{self.subjectmatters}"


class Request(models.Model):
  name = models.CharField(max_length=255)
  requestid = models.IntegerField(null=True)
  createtime = models.DateField(null=True)
  matterid = models.IntegerField(null=True)
  requestattachment = models.FileField(null=True)
  currentrequestsituation = models.CharField(max_length=255)
  lastrequestsituation = models.CharField(max_length=255)
  def __str__(self):
    return f"{self.name}"


# Create your models here.
