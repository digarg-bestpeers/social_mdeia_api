from rest_framework import serializers
from network.models import Post, User


class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ['username']


class PostSerializer(serializers.ModelSerializer):
  user = UserSerializer(many=False, read_only=True)
  class Meta:
    model = Post
    fields = ['body', 'created_at', 'user', 'id']
    read_only_fields = ['id']

  def create(self, validated_data):
    post = Post.objects.create(user=self.context['request'].user, **validated_data)
    return post

  def update(self, instance, validated_data):
    data = validated_data.get('body')
    instance.body = data
    instance.save()
    return instance



