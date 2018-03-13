from django import forms

from .models import Subscriber, StuExcSignUp

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ["name", "email"]

class FeaturedForm(forms.ModelForm):
    class Meta:
        model = StuExcSignUp
        fields = ["name", "number", "email", "link", "file", "message"]
