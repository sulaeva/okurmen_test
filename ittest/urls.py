from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Импортируем ViewSet'ы и RegisterView из приложения okurmen_test
from okurmen_test.views import QuestionViewSet, ChoiceViewSet, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Регистрируем роуты для ViewSet'ов
router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # API с ViewSet'ами
    path('api/', include(router.urls)),

    # Регистрация пользователя
    path('api/register/', RegisterView.as_view()),

    # JWT: получение токена
    path('api/token/', TokenObtainPairView.as_view()),

    # JWT: обновление access токена
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
