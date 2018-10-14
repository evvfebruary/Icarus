
from djongo import models
from rest_framework import serializers
from IcarusDP import validator as vd

class SSDKLCampaign(models.Model):
    ssdkl = models.CharField(max_length=200)
    campaign = models.CharField(max_length=200)


class Coupon(models.Model):
    ptcs = models.DictField()
    ssdkl = models.CharField(max_length=200)
    origin = models.CharField(max_length=3)
    destination = models.CharField(max_length=3)
    departure = models.DateField()
    campaign = models.CharField(max_length=20, default="base")


class CouponSerializer(serializers.Serializer):
    ptcs = serializers.DictField()
    ssdkl = serializers.CharField(max_length=200)
    origin = serializers.CharField(max_length=3)
    destination = serializers.CharField(max_length=3)
    departure = serializers.DateField()
    campaign = serializers.CharField(max_length=20, default="base")

    def create(self, validated_data):
        return Coupon.objects.get_or_create(**validated_data)

    def validate_origin(self, iata_code):
        if not vd.is_iatacode_valid(iata_code):
            raise serializers.ValidationError("Wrong IATA code")
        return iata_code

    def validate_destination(self, iata_code):
        if not vd.is_iatacode_valid(iata_code):
            raise serializers.ValidationError("Wrong IATA code")
        return iata_code

    def validate_departure(self, datetime):
        if not vd.is_datetime_valid(datetime):
            raise serializers.ValidationError("Wrong departure time")
        return datetime

    def validate_ptcs(self, ptcs):
        if list(ptcs.keys()) != ['ADT', 'CHD', 'INF']:
            raise serializers.ValidationError("Wrong pcts fields, must be ['ADT', 'CHD', 'INF'] but have {}".format(str(ptcs.keys())))
        else:
            if ptcs["ADT"] < 1:
                raise serializers.ValidationError("Wrong adult passengers fields")
            if ptcs['CHD'] > 1000 or ptcs['INF'] > 1000: # Don't know anything about this limit
                raise serializers.ValidationError("Wow, your lucky guy but no, check cargo airplane")
            return ptcs

    def update(self, instance, campaign):
        instance.campaign = campaign
        instance.save()

# Create your models here.


