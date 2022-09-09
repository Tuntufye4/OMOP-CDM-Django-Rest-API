
# Create your views here.
from django.shortcuts import render
from .models import Person, Observation_Period,Visit_Occurrence,Visit_Detail,Condition_Occurrence,Drug_Exposure,Procedure_Occurrence,Device_Exposure,Measurement,Observation,Death,Note,Note_Nlp,Specimen,Fact_Relationship,Location,Care_Site,Provider
from .serializers import PersonSerializer,Observation_PeriodSerializer,Visit_OccurrenceSerializer,Visit_DetailSerializer,Condition_OccurrenceSerializer,Drug_ExposureSerializer,Procedure_OccurrenceSerializer, Device_ExposureSerializer,MeasurementSerializer,ObservationSerializer,DeathSerializer,NoteSerializer,Note_NlpSerializer,SpecimenSerializer,Fact_RelationshipSerializer,LocationSerializer,Care_SiteSerializer,ProviderSerializer
from drf_multiple_model.views import ObjectMultipleModelAPIView


class TextAPIView(ObjectMultipleModelAPIView):
     def get_querylist(self):

         querylist = [

             {'queryset' : Person.objects.all(),'serializer_class' : PersonSerializer},
             {'queryset' : Observation_Period.objects.all(),'serializer_class' : Observation_PeriodSerializer},
             {'queryset' :Visit_Occurrence.objects.all(),'serializer_class' : Visit_OccurrenceSerializer},
             {'queryset' : Visit_Detail.objects.all(),'serializer_class' : Visit_DetailSerializer },
             {'queryset' : Condition_Occurrence.objects.all(),'serializer_class' : Condition_OccurrenceSerializer },
             {'queryset' : Drug_Exposure.objects.all(),'serializer_class' : Drug_ExposureSerializer},
             {'queryset' : Procedure_Occurrence.objects.all(),'serializer_class' : Procedure_OccurrenceSerializer},
             {'queryset' : Device_Exposure.objects.all(),'serializer_class' : Device_ExposureSerializer},
             {'queryset' : Measurement.objects.all(),'serializer_class' : MeasurementSerializer},
             {'queryset' : Observation.objects.all(),'serializer_class' : ObservationSerializer},
             {'queryset' : Death.objects.all(),'serializer_class' : DeathSerializer},
             {'queryset' : Note.objects.all(),'serializer_class' : NoteSerializer},
             {'queryset' : Note_Nlp.objects.all(), 'serializer_class' : Note_NlpSerializer},
             {'queryset' : Specimen.objects.all(),'serializer_class' : SpecimenSerializer},
             {'queryset' : Fact_Relationship.objects.all(),'serializer_class' : Fact_RelationshipSerializer},
             {'queryset' : Location.objects.all(),'serializer_class' : LocationSerializer},
             {'queryset' : Care_Site.objects.all(), 'serializer_class' : Care_SiteSerializer},
             {'queryset' : Provider.objects.all(),'serializer_class' : ProviderSerializer}
        
         ]

         return querylist
    

    
    

    
    

    


    

    

    

    

    




       