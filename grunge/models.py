# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=1000)
    brief = models.TextField(max_length=100000)
    rating = models.IntegerField(default=0)
    cover = models.ImageField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp"]

class Album(models.Model):
    name = models.CharField(max_length=1000)
    band = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    brief = models.TextField(max_length=100000)
    cover = models.ImageField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp"]


class Song(models.Model):
    name = models.CharField(max_length=1000)
    cover = models.ImageField(null=True, blank=True)
    frequency = models.IntegerField(default=0)
    file = models.FileField(max_length=500)
    album = models.ForeignKey(Album, null=True, blank=True)
    band = models.ForeignKey(Band, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp"]

    def clean(self):
        super(Song, self).clean()
        if self.band is None and self.album is None:
            raise ValidationError('You need to add either Band or Album!')

class StudioExclusive(models.Model):
    name = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    brief = models.TextField(max_length=100000)
    frequency = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ["-timestamp"]

class Interview(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)
    cover = models.ImageField(null=True, blank=True)
    brief = models.TextField(max_length=100000)
    frequency = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp"]

class Subscriber(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.name



class StuExcSignUp(models.Model):
    name = models.CharField(max_length=1000)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    email = models.CharField(max_length=1000)
    message = models.TextField(max_length=100000)
    link = models.CharField(max_length=1000)
    file = models.FileField(max_length=500)


    def __unicode__(self):
        return self.name

class Gig(models.Model):
    name = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    cover = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return self.name
