from django.contrib.auth.models import User, Group
from rest_framework import serializers

from . models import WrBank

class WrBankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WrBank
        fields = ('wrbank_date', 'wrbank_deposit_withdrawal', 'wrbank_money1', 'wrbank_note', 'wrbank_money2',  'wrbank_money3', 'wrbank_aggregate', 'wrbank_loan_balance', 'wrbank_bankbook_balance', )
    