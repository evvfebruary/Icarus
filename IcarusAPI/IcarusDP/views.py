from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from IcarusDP.models import CouponSerializer


class CampaignView(APIView):
    parser_classes = (JSONParser,)

    def post(self, request):
        cpn = CouponSerializer(data=request.data)
        print(cpn.is_valid())
        print(cpn.errors)
        print(cpn.validated_data)
        return Response({'received data': request.data})

