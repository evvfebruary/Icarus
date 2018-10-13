from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from IcarusDP import forms
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from IcarusDP.models import CouponSerializer, Coupon, SSDKLCampaign


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


class CampaignView(APIView):
    parser_classes = (JSONParser,)

    def post(self, request):
        cpn = CouponSerializer(data=request.data)
        if cpn.is_valid():
            ssdkl = request.data['ssdkl']
            try:
                cmp_obj = SSDKLCampaign.objects.get(ssdkl = ssdkl)
            except SSDKLCampaign.DoesNotExist:
                cmp_obj = None
            if cmp_obj:
                cpn.validated_data['campaign'] = cmp_obj.campaign
            cpn_obj = cpn.create(cpn.validated_data)[0]
            return Response({'coupon': cpn_obj.campaign})
        else:
            return Response({'Handled error': cpn.errors})


@permission_classes((AllowAny,))
class databaseRequestsView(APIView):

    def get(self, request):
        coupons = Coupon.objects.all()
        campaign_rules = SSDKLCampaign.objects.all()
        form = forms.SSDKLCampaignForm
        return render(request, 'coupons.html', context = {"coupons": [coupon for coupon in coupons],
                                                          "rules":[campaign for campaign in campaign_rules],
                                                          "form":form})

    parser_classes = (FormParser,)

    def post(self, request):
            form = forms.SSDKLCampaignForm(request.POST)
            if form.is_valid():
                ssdcmp = form.save(commit=False)

                ssdcmp.save()
                return redirect('/coupons')
            else:
                print(form.errors)



