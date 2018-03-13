# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Song, Album, Band, StudioExclusive, Interview, Gig
from forms import SubscriberForm, FeaturedForm
# Create your views here.

def home(request):
    songs = Song.objects.all().order_by("-frequency")
    mp_int = Interview.objects.all().order_by("-frequency").first()
    mr_int = Interview.objects.all().first()
    mp_stu = StudioExclusive.objects.all().order_by("-frequency").first()
    mr_stu = StudioExclusive.objects.all().first()
    mr_alb = Album.objects.all().first()
    mr_band = Band.objects.all().first()
    subscribe_form = SubscriberForm(request.POST or None)
    stuexc_form = FeaturedForm(request.POST or None, request.FILES or None)

    if 'message' in request.POST:
        if stuexc_form.is_valid():
            instance1 = stuexc_form.save(commit=False)
            instance1.save()
            # print instance1.cleaned_data
            return redirect('home')
    else:
        if subscribe_form.is_valid():
            instance = subscribe_form.save(commit=False)
            instance.save()
            return redirect('home')


    return render(request, "base.html",
                  {"songs" : songs,
                   "stu_obj" : mp_stu,
                   "int_freq" : mp_int,
                   "int_rec" : mr_int,
                   "stu_rec" : mr_stu,
                   "alb_rec" : mr_alb,
                   "band_rec" : mr_band,
                   "subscribe_form" : subscribe_form,
                   "stuexc_form" : stuexc_form,
                   })


def alrev(request):
    album_list = Album.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(album_list, 12)
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        albums = paginator.page(1)
    except EmptyPage:
        albums = paginator.page(paginator.num_pages)

    return render(request, "alrev.htm", {"albums": albums})


def laban(request):
    band_list = Band.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(band_list, 12)
    try:
        bands = paginator.page(page)
    except PageNotAnInteger:
        bands = paginator.page(1)
    except EmptyPage:
        bands = paginator.page(paginator.num_pages)

    return render(request, "laban.html", {"bands": bands})

def alrev_detail(request, id):
    alrev = get_object_or_404(Album, id=id)
    return render(request, "album_single.htm", {"obj": alrev})

def interviews_detail(request, id):
    interview = get_object_or_404(Interview, id=id)
    interview.frequency+=1
    interview.save()
    return render(request, "single_page.htm", {"obj": interview})

def stuexc_detail(request, id):
    stuexc = get_object_or_404(StudioExclusive, id=id)
    stuexc.frequency+=1
    stuexc.save()
    return render(request, "single_page.htm", {"obj": stuexc})

def laban_detail(request, id):
    laban = get_object_or_404(Band, id=id)
    return render(request, "band_single.htm", {"obj": laban})

def interviews(request):
    interview_list = Interview.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(interview_list, 12)
    try:
        interviews = paginator.page(page)
    except PageNotAnInteger:
        interviews = paginator.page(1)
    except EmptyPage:
        interviews = paginator.page(paginator.num_pages)

    return render(request, "interview.html", {"interviews": interviews})


def stuexc(request):
    exclusive_list = StudioExclusive.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(exclusive_list, 12)
    try:
        exclusives = paginator.page(page)
    except PageNotAnInteger:
        exclusives = paginator.page(1)
    except EmptyPage:
        exclusives = paginator.page(paginator.num_pages)

    return render(request, "stuexc.html", {"exclusives": exclusives})


def gigs(request):
    gigs_list = Gig.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(gigs_list, 12)
    try:
        gigsP = paginator.page(page)
    except PageNotAnInteger:
        gigsP = paginator.page(1)
    except EmptyPage:
        gigsP = paginator.page(paginator.num_pages)
    return render(request, "gigs.htm", {"gigs":gigsP })

def song_detail(request, id):
    song = get_object_or_404(Song, id=id)
    song.frequency+=1
    song.save()
    return render(request, "song_single.htm", {"obj":song})