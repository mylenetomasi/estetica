from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from estetica.views import AgendamentoViewSet,ClienteViewSet,PacoteViewSet,ProcedimentoViewSet, PacotesProcessoViewSet

router = DefaultRouter()
router.register(r"pacotesprocesso", PacotesProcessoViewSet)
router.register(r"pacote", PacoteViewSet)
router.register(r"agendamento", AgendamentoViewSet)
router.register(r"procedimento", ProcedimentoViewSet)
router.register(r"cliente", ClienteViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]