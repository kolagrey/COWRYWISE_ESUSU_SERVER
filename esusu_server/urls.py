"""esusu_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from esusu_server.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

router.register(r'accounts', views.AccountViewSet)
router.register(r'account/groups', views.AccountGroupViewSet)
router.register(r'account/group/relationship', views.AccountGroupRelationshipViewSet)
router.register(r'contribution', views.GroupsContributionViewSet)
router.register(r'payout/list', views.GroupPayoutListViewSet)
router.register(r'payout', views.GroupPayoutLogViewSet)
router.register(r'admin/group', views.AdminGroupListView, basename='AccountGroup')
router.register(r'group/contributions', views.GroupContributionViewSet, basename='GroupContribution')
router.register(r'group/search', views.AccountGroupSearchViewSet, basename='AccountGroup')
router.register(r'group/code/search', views.AccountGroupCodeViewSet, basename='AccountGroup')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
