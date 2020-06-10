import graphene
from graphene_django.types import DjangoObjectType
from .models import Polling
from graphene import Connection, ConnectionField, Node, Int


class PollInfo(DjangoObjectType):
    class Meta:
        model = Polling


class Query(graphene.ObjectType):
    all_data = graphene.List(PollInfo)
    count = graphene.Int()

    @graphene.resolve_only_args
    def resolve_all_data(self):
        return Polling.objects.filter(soap_know='True')

    @graphene.resolve_only_args
    def resolve_count(self):
        return Polling.objects.filter(soap_know='True').count()


