from django.db import models
from datetime import datetime
from rest_framework import serializers
from IcarusDP import validator as vd


class Coupon:
    def __init__(self, ptcs, ssdkl, origin, destination, departure, campaign='base'):
        self.ptcs = ptcs  # {"ADT": 1,"CHD": 1,"INF": 1}
        self.ssdkl = ssdkl  # :"9a9c4face96c4314b8ff939f9682be14"
        self.origin = origin
        self.destination = destination
        self.departure = departure or datetime.now()
        self.campaign = campaign


class CouponSerializer(serializers.Serializer):
    ptcs = serializers.DictField()
    ssdkl = serializers.CharField(max_length=200)
    origin = serializers.CharField(max_length=3)
    destination = serializers.CharField(max_length=3)
    departure = serializers.DateField()

    def create(self, validated_data):
        return Coupon(**validated_data)

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
            if ptcs['CHD'] > 1000 or ptcs['INF'] > 1000: # Don't know anythin about this limit
                raise serializers.ValidationError("Wow, your lucky guy but no, check cargo airplane")
            return ptcs

    def update(self, instance, campaign):
        instance.campaign = campaign
        instance.save()

# Create your models here.


