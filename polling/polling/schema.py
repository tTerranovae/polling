import graphene
import poll.schema as poll


class Query(poll.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)