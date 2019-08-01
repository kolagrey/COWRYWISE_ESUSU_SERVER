from django.contrib.auth.models import User, Group
from esusu_server.api.models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['account_id', 'firstname', 'lastname',
                  'email', 'mobile', 'created']
        depth = 1


class AccountGroupSerializer(serializers.HyperlinkedModelSerializer):
        
    class Meta:
        model = AccountGroup
        fields = ['group_id', 'group_name', 'group_description', 'group_admin',
                  'maximum_capacity', 'contribution_amount', 'group_code', 'searchable', 'created']


class AccountGroupRelationshipSerializer(serializers.HyperlinkedModelSerializer):
    group = serializers.CharField(source='group_id')
    user = serializers.CharField(source='account_id')

    class Meta:
        model = AccountGroupRelationship
        fields = ['rid', 'group', 'user',
                  'is_admin', 'created']
        depth = 1


class GroupContributionSerializer(serializers.HyperlinkedModelSerializer):
    group = serializers.CharField(source='group_id')
    user = serializers.CharField(source='account_id')

    class Meta:
        model = GroupContribution
        fields = ['gc_id', 'group', 'user',
                  'contribution_amount', 'contribution_date']
        depth = 1


class GroupPayoutListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.CharField(source='account_id')

    class Meta:
        model = GroupPayoutList
        fields = ['gpl_id', 'user',
                  'payout_status', 'created']
        depth = 1


class GroupPayoutLogSerializer(serializers.HyperlinkedModelSerializer):
    group = serializers.CharField(source='group_id')
    user = serializers.CharField(source='account_id')

    class Meta:
        model = GroupPayoutLog
        fields = ['log_id', 'group', 'user',
                  'payout_amount', 'payout_date']
        depth = 1
