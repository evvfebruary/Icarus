from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView


class CampaignView(APIView):
    parser_classes = (JSONParser,)

    def post(self, request):
        return Response({'received data': request.data})

