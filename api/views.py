from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import PaintingTable,BidTable
from api.serializers import PaintingTableSerializer, BidTableSerializer
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@api_view(['GET'])
def getAllPaintingData(request):
    resultSet = PaintingTable.objects.all()
    serializers = PaintingTableSerializer(resultSet, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getPaintingData(request,id):
    try:
        painting = PaintingTable.objects.get(id = id)
    except PaintingTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializers = PaintingTableSerializer(painting)
    return Response(serializers.data)

@api_view(['DELETE'])
def deletePaintingData(request,id):
    try:
        painting = PaintingTable.objects.get(id = id)
    except PaintingTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    painting.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def getAllBidData(request):
    resultSet = BidTable.objects.all()
    serializers = BidTableSerializer(resultSet, many=True)
    return Response(serializers.data)



@api_view(['POST'])
def addRecordToBidTable(request):

    data = {'paintingRef': request.data.get('id'), 'name': request.data.get('name'), 'finalBidAmt': request.data.get('finalBidAmt')}
    #print(data)
    try:
        painting = PaintingTable.objects.get(id = request.data.get('id'))
    except PaintingTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #data['paintingRef'] = painting
    serializers = BidTableSerializer(data=data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)






@csrf_exempt
def updatePaintingData(request):
    if request.method == "PUT":
        body = json.loads(request.body)
        id = body['id']
        try:
            painting = PaintingTable.objects.get(id = id)
            painting.availableForBid = body['availableForBid']
            painting.save()
            return JsonResponse({'result': 1})
        except PaintingTable.DoesNotExist:
            return JsonResponse({'result': 0})
    else:
        return JsonResponse({'result': 0})
