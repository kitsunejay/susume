from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    en = serializers.CharField()
    ja = serializers.CharField()
    ens = serializers.CharField()
    jas = serializers.CharField(allow_blank=True,default='')

    def create(self, validated_data):
        """
        Create and return a new `Job` instance, given the validated data.
        """
        return Job.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.en = validated_data.get('en', instance.en)
        instance.ja = validated_data.get('ja', instance.ja)
        instance.ens = validated_data.get('ens', instance.ens)
        instance.jas = validated_data.get('jas', instance.jas)
        instance.save()
        return instance