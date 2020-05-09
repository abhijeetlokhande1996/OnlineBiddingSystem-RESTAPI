from rest_framework.serializers import ModelSerializer

from rest_framework import serializers
from api.models import PaintingTable, BidTable

class PaintingTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaintingTable
        fields = ('id','picture','paintingName','creator','claimedAmt','availableForBid')


class BidTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidTable
        fields = ('paintingRef','finalBidAmt','name')
