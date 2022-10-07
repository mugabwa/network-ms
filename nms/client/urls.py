from rest_framework import routers
from nms.client.views import ClientViewset

router = routers.SimpleRouter()
router.register(r'clients', ClientViewset, basename='Client')

urlpatterns = router.urls