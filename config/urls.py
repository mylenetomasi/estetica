from django.contrib import admin
from django.urls import include, path
from usuario.router import router as usuario_router

from rest_framework.routers import DefaultRouter

from estetica.views import (
    AgendamentoViewSet,
    ClienteViewSet,
    PacoteViewSet,
    ProcedimentoViewSet,
    PacotesProcessoViewSet,
)

router = DefaultRouter()
router.register(r"pacotesprocesso", PacotesProcessoViewSet)
router.register(r"pacote", PacoteViewSet)
router.register(r"agendamento", AgendamentoViewSet)
router.register(r"procedimento", ProcedimentoViewSet)
router.register(r"cliente", ClienteViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/usuario", include(usuario_router.urls)),
]
