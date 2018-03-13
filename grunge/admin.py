# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Song, Band, Album, StudioExclusive, Interview, Subscriber, StuExcSignUp, Gig
# Register your models here.

admin.site.register(Song)
admin.site.register(Band)
admin.site.register(Album)
admin.site.register(StudioExclusive)
admin.site.register(Interview)
admin.site.register(Subscriber)
admin.site.register(StuExcSignUp)
admin.site.register(Gig)
