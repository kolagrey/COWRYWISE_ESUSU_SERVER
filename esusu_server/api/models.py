from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Account Group Model
""" 

This model holds information about groups.
Group admin is a valid account (linked by email).
A group can only be created by a valid user 

"""


class AccountGroup(models.Model):
    # account Group ID
    group_id = models.AutoField(primary_key=True, null=False)
    # account group name
    group_name = models.CharField(max_length=100, null=False)
    # account group description
    group_description = models.CharField(max_length=140)
    # account group admin
    group_admin = models.EmailField(blank=False, null=False)
    # account group maximum capacity
    maximum_capacity = models.IntegerField()
    # account contribution amount
    contribution_amount = models.IntegerField()
    # account group searchable status
    group_code = models.CharField(max_length=6, null=True, blank=True)
    # account group searchable status
    searchable = models.BooleanField(default=False)
    # account created date
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.group_name


# Account (Users) Model
""" 

This model holds information about users.
A user can belong to a group or be assigned to one.

"""


class Account(models.Model):
    # account ID
    account_id = models.AutoField(primary_key=True, null=False)
    # accountholder firstname
    firstname = models.CharField(max_length=100, null=False)
    # account holder lastname
    lastname = models.CharField(max_length=100, null=False)
    # accountholder email
    email = models.EmailField(blank=False, null=False)
    # accountholder mobile number
    mobile = models.CharField(max_length=16, null=False)
    # account created date
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.firstname + ' ' + self.lastname


# Account & Account Group Relationship Model
""" 

This model holds information about groups.
Group admin is a valid account (linked by email).
A group can only be created by a valid user 

Note: Replacement for deprecated group_id field in Account model

"""


class AccountGroupRelationship(models.Model):
    # Relationship ID
    rid = models.AutoField(primary_key=True, null=False)
    # account group reference
    group_id = models.ForeignKey(
        AccountGroup, null=False, db_column='group_id', blank=False, on_delete=models.CASCADE)
    # account holder reference
    account_id = models.ForeignKey(
        Account, null=False, db_column='account_id', blank=False, on_delete=models.CASCADE)
    # account holder group owner status
    is_admin = models.BooleanField(null=True, blank=True, default=False)
    # created date
    created = models.DateTimeField(default=timezone.now)


# Group Payout List Model
class GroupPayoutList(models.Model):
    # Group Payout ID
    gpl_id = models.AutoField(primary_key=True, null=False)
    # account group reference
    group_id = models.ForeignKey(
        AccountGroup, null=False, db_column='group_id', blank=False, on_delete=models.CASCADE)
    # account holder reference
    account_id = models.ForeignKey(
        Account, null=False, db_column='account_id', blank=False, on_delete=models.CASCADE)
    # payout status
    payout_status = models.BooleanField(default=False)
    # account created date
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created']


# Group Contribution Model


class GroupContribution(models.Model):
    # Group Contribution ID
    gc_id = models.AutoField(primary_key=True, null=False)
    # account group reference
    group_id = models.ForeignKey(
        AccountGroup, null=False, db_column='group_id', blank=False, on_delete=models.CASCADE)
    # account holder reference
    account_id = models.ForeignKey(
        Account, null=False, db_column='account_id', blank=False, on_delete=models.CASCADE)
    # contribution amount
    contribution_amount = models.IntegerField()
    # account created date
    contribution_date = models.DateTimeField(default=timezone.now)


# Group Payout Log Model
class GroupPayoutLog(models.Model):
    # Group Payout Log ID
    log_id = models.AutoField(primary_key=True, null=False)
    # account group reference
    group_id = models.ForeignKey(
        AccountGroup, null=False, db_column='group_id', blank=False, on_delete=models.CASCADE)
    # account holder reference
    account_id = models.ForeignKey(
        Account, null=False, db_column='account_id', blank=False, on_delete=models.CASCADE)
    # payout amount
    payout_amount = models.IntegerField()
    # payout log date
    payout_date = models.DateTimeField(default=timezone.now)
