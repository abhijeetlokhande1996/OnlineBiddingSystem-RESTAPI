from django.db import models

# Create your models here.
class PaintingTable(models.Model):
    id = models.AutoField(primary_key=True)
    picture = models.ImageField(upload_to='images/')
    paintingName = models.TextField()
    creator = models.TextField()
    claimedAmt = models.FloatField()
    availableForBid = models.BooleanField()
    def __str__(self):
        return str(self.id)

class BidTable(models.Model):
    paintingRef = models.ForeignKey(PaintingTable, on_delete=models.CASCADE)
    finalBidAmt = models.FloatField()
    name = models.TextField()

    def __str__(self):
        return str(self.paintingRef)
