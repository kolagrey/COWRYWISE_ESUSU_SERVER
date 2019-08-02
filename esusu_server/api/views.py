from rest_framework import viewsets
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.response import Response
from random import randint

from django.db.models import Q
from django.contrib.auth.models import User, Group
from .serializers import *
from .models import *


# Admin View
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be created viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be created viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# API View

class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be created, viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows account groups to be created, viewed or edited.
    """
    queryset = AccountGroup.objects.all()
    serializer_class = AccountGroupSerializer
    http_method_names = ['post', 'patch', 'get', 'head']

    def create(self, request):
        group_code = randint(100000, 999999)
        try:
            serializer = AccountGroupSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(group_code=group_code)
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Exception as exc:
            return Response('Missing parameters {}'.format(exc), status=400)

class AccountGroupCodeViewSet(viewsets.ModelViewSet):
    serializer_class = AccountGroupSerializer
    http_method_names = ['get', 'head']

    def get_queryset(self):
        """
        This view should return a list of all the groups for
        the user (group admin) as determined by the identifier (email address expected) portion of the URL.
        """
        try:
            code = self.request.GET['code']
            if code is not None:
                queryset = AccountGroup.objects.filter(group_code=code)
                return queryset
            else:
                Response('Missing parameters', status=400)
        except (MultiValueDictKeyError, KeyError) as exc:
            Response('Missing parameters {}'.format(exc), status=400)


class AccountGroupSearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows account groups to be created, viewed or edited.
    """
    serializer_class = AccountGroupSerializer
    http_method_names = ['get', 'head']

    def get_queryset(self):
        """
        This view should return a list of all the groups for
        as determined by the search_params (search parameter)  portion of the URL.
        """
        try:
            search_params = self.request.GET['search_params']
            if search_params is not None:
                queryset = AccountGroup.objects.filter(Q(group_name__icontains=search_params) | Q(
                    group_description__icontains=search_params))
                return queryset
            else:
                queryset = AccountGroup.objects.all()
                return queryset
        except (MultiValueDictKeyError, KeyError) as exc:
            Response('Missing parameters {}'.format(exc), status=400)


class AdminGroupListView(viewsets.ModelViewSet):
    serializer_class = AccountGroupSerializer

    def get_queryset(self):
        """
        This view should return a list of all the groups for
        the user (group admin) as determined by the identifier (email address expected) portion of the URL.
        """
        try:
            identifier = self.request.GET['identifier']
            if identifier is not None:
                queryset = AccountGroup.objects.filter(group_admin=identifier)
                return queryset
            else:
                queryset = AccountGroup.objects.all()
                return queryset
        except (MultiValueDictKeyError, KeyError) as exc:
            Response('Missing parameters {}'.format(exc), status=400)


class AccountGroupRelationshipViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows account + group relationship to be viewed or edited.
    """
    
    queryset = AccountGroupRelationship.objects.all()
    serializer_class = AccountGroupRelationshipSerializer
    http_method_names = ['get', 'post', 'head']


class GroupsContributionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups contributions to be viewed
    """
    queryset = GroupContribution.objects.all()
    serializer_class = GroupContributionSerializer
    http_method_names = ['get', 'head']


class GroupContributionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group contributions to be viewed 
    """
    serializer_class = GroupContributionSerializer
    http_method_names = ['get', 'head']

    def get_queryset(self):
        """
        This view should return a list of all the groups for
        the user (group admin) as determined by the identifier (email address expected) portion of the URL.
        """
        try:
            identifier = self.request.GET['identifier']
            if identifier.isdigit():
                if identifier is not None:
                    queryset = GroupContribution.objects.filter(
                        group_id=identifier)
                    return queryset
                else:
                    Response('Missing parameters {}'.format(
                        identifier), status=400)
            else:
                Response('Invalid parameters {}'.format(
                    identifier), status=400)
        except (MultiValueDictKeyError, KeyError) as exc:
            Response('Missing parameters {}'.format(exc), status=400)


class GroupPayoutListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group payout list to be viewed or edited.
    """
    queryset = GroupPayoutList.objects.all()
    serializer_class = GroupPayoutListSerializer
    http_method_names = ['get', 'head']


class GroupPayoutLogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group payout log to be viewed or edited.
    """
    queryset = GroupPayoutLog.objects.all()
    serializer_class = GroupPayoutLogSerializer
    http_method_names = ['get', 'head']
