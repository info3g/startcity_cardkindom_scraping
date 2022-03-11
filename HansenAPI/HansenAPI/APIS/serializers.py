import uuid
from rest_framework import serializers
 
# create a serializer
class StarcitygamesSerializer(serializers.Serializer):
    # initialize fields
    Title = serializers.CharField()
    Editions = serializers.CharField()


class cardkingdomSerializer(serializers.Serializer):
    # initialize fields
    uuid = serializers.CharField()

