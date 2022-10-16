from django.urls import path
from rest_framework import routers
from nms.payment.views import InvoicesViewset

router = routers.SimpleRouter()
router.register(r'payment', InvoicesViewset, basename='Payment')

urlpatterns = router.urls
