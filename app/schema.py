from graphene_django import DjangoObjectType
import graphene

from blog.models import Post, Tag


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    tags = graphene.List(TagType)

    def resolve_posts(self, info):
        return Post.objects.all()

    def resolve_tags(self, info):
        return Post.objects.all()


schema = graphene.Schema(query=Query)
