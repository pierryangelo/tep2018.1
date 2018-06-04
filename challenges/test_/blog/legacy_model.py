# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    user = models.ForeignKey('Users', models.CASCADE, related_name="addresses")
    street = models.CharField(max_length=None)
    suite = models.CharField(max_length=None)
    city = models.CharField(max_length=None)
    zipcode = models.CharField(max_length=None)

    class Meta:
        managed = True
        db_table = 'addresses'


class Comment(models.Model):
    post = models.ForeignKey('Posts', models.CASCADE)
    name = models.CharField(max_length=None)
    email = models.EmailField()
    body = models.TextField()

    class Meta:
        managed = True
        db_table = 'comments'


class Post(models.Model):
    user = models.ForeignKey('Users', models.CASCADE, related_name='posts')
    title = models.CharField(max_length=None)
    body = models.TextField()

    class Meta:
        managed = True
        db_table = 'posts'


class User(models.Model):
    name = models.CharField(max_length=None, blank=True, null=True)
    email = models.EmailField()

    class Meta:
        managed = True
        db_table = 'users'
