from .views.LogoutViews import LogoutViewSet
from .views.LoginViews import LoginViewSet
from .views.RegisterViews import RegisterView
from .views.UpdatePasswordViews import UpdatePasswordView
from .views.ForgetPasswordViews import ForgetPasswordView
from rest_framework.routers import DefaultRouter


router=DefaultRouter()

router.register('register', RegisterView, basename='register')
router.register('login', LoginViewSet, basename='login')
router.register('logout', LogoutViewSet, basename='logout')
router.register('forgetPassword', ForgetPasswordView, basename='forgetPassword')
router.register('updatePassword', UpdatePasswordView, basename='updatePassword')

urlpatterns = router.urls

