from rest_framework import serializers
from .models import Person, Observation_Period, Visit_Occurrence, Visit_Detail, Condition_Occurrence, Drug_Exposure,Procedure_Occurrence,Device_Exposure,Measurement,Observation, Death, Note, Note_Nlp, Specimen, Fact_Relationship, Location, Care_Site, Provider




class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person 
        fields = '__all__'

class Observation_PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Observation_Period 
        fields = '__all__'

class Visit_OccurrenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit_Occurrence 
        fields = '__all__'

class Visit_DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit_Detail
        fields = '__all__'

class Condition_OccurrenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condition_Occurrence 
        fields = '__all__'

class Drug_ExposureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drug_Exposure 
        fields = '__all__'

class Procedure_OccurrenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Procedure_Occurrence
        fields = '__all__'

class Device_ExposureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device_Exposure
        fields = '__all__'

class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement 
        fields = '__all__'

class ObservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Observation 
        fields = '__all__'

class DeathSerializer(serializers.ModelSerializer):

    class Meta:
        model = Death
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'

class Note_NlpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note_Nlp
        fields = '__all__'

class SpecimenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specimen
        fields = '__all__'

class Fact_RelationshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fact_Relationship
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

class Care_SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Care_Site
        fields = '__all__'

class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'