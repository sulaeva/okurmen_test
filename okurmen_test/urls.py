from django.urls import path, include
from .views import QuestionViewSet, ChoiceViewSet, RegisterView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register(r'question', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'register', RegisterView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

