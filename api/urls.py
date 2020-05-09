from django.urls import path
from . import views

urlpatterns = [
    path('getAllPaintingData', views.getAllPaintingData),
    path('getPaintingData/<int:id>', views.getPaintingData),
    path('deletePaintingData/<int:id>', views.deletePaintingData),
    path('updatePaintingData', views.updatePaintingData),
    path('addRecordToBidTable', views.addRecordToBidTable),
    #getAllBidData
    path('getAllBidData', views.getAllBidData),

]
