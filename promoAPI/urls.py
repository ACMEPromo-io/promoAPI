from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from Fornecedores.views import FornecedoresViewSet
from Promocoes.views import PromocoesViewSet
from Clientes.views import ClientesViewSet,ClientePromocaoViewSet
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Promo API')

router = routers.DefaultRouter()
router.register(r'fornecedor', FornecedoresViewSet, basename='Fornecedores')
router.register(r'promocao', PromocoesViewSet, basename='Promocoes')
router.register(r'cliente', ClientesViewSet, basename='Clientes')
router.register(r'clientepromocao', ClientePromocaoViewSet, basename='Clientes/Promoções')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]