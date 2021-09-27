from posts.models import Comment, Follow, Group, Post, User
from rest_framework.relations import PrimaryKeyRelatedField, SlugRelatedField
from rest_framework.serializers import CurrentUserDefault, ModelSerializer
from rest_framework.validators import UniqueTogetherValidator


class GroupSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = "__all__"
        read_only_fields = ('__all__',)


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'pub_date')


class CommentSerializer(ModelSerializer):
    post = PrimaryKeyRelatedField(
        queryset=Post.objects.all(), required=False)
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id', 'post', 'created')


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='username',
                            read_only=True, default=CurrentUserDefault())
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ('id', 'user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(), fields=('user', 'following')),
            UniqueTogetherValidator(
                queryset=Follow.objects.all(), fields=('user', 'user'))
        ]
