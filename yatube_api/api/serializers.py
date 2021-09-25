from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, PrimaryKeyRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class CommentSerializer(serializers.ModelSerializer):
    post = PrimaryKeyRelatedField(
        queryset=Post.objects.all(), required=False)
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id', 'post', 'created')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = "__all__"
        read_only_fields = ('__all__',)


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'pub_date')


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ('user', 'following')

    validators = [UniqueTogetherValidator
                  (queryset=Follow.objects.all(),
                   fields=('name', 'followihg')),
                  UniqueTogetherValidator
                  (queryset=Follow.objects.all(),
                   fields=('name', 'name'))]
