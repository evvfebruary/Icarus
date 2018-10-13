from django.forms import ModelForm, CharField
from IcarusDP import models


class SSDKLCampaignForm(ModelForm):
    ssdkl = CharField(max_length=300)
    campaign = CharField(max_length=300)

    class Meta:
        fields = ('ssdkl', 'campaign')
        model = models.SSDKLCampaign