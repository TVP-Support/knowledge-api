from rest_framework import serializers


class AddFaciViewSerializer(serializers.Serializer):
    AIM_TYPE_CHOICES = ('solution', 'idea', 'sync')

    aim = serializers.CharField(max_length=255)
    if_not_reached = serializers.CharField(max_length=255)
    aim_type = serializers.ChoiceField(choices=AIM_TYPE_CHOICES)


class GetListFaciSerializer(serializers.Serializer):
    count_on_page = serializers.IntegerField(min_value=1, max_value=100)
    page_number = serializers.IntegerField(min_value=1)


class FaciEditMembersSerializer(serializers.Serializer):
    for_what = serializers.CharField(max_length=100)


class FaciEditAgendaSerializer(serializers.Serializer):
    themes = serializers.CharField(max_length=1000, allow_blank=True, allow_null=False)
    questions = serializers.CharField(max_length=2000, allow_blank=True, allow_null=False)
    themes_duration = serializers.IntegerField(min_value=1)


class FaciEditPreparingSerializer(serializers.Serializer):
    duration = serializers.IntegerField(min_value=1)
    place = serializers.CharField(max_length=100, allow_blank=True, allow_null=False)
    dt_meeting = serializers.DateTimeField()


class FaciEditKeyThoughtsSerializer(serializers.Serializer):
    key_thoughts = serializers.CharField(max_length=10000, allow_blank=True, allow_null=False)
    parked_thoughts = serializers.CharField(max_length=10000, allow_blank=True, allow_null=False)


class FaciEditAgreementsSerializer(serializers.Serializer):
    other_agreements = serializers.CharField(max_length=10000, allow_blank=True, allow_null=False)
