from rest_framework import routers
from nms.network.views import BandwidthViewset

router = routers.SimpleRouter()
router.register(r'network', BandwidthViewset, basename='Network')

urlpatterns = router.urls