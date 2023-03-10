from rest_framework import serializers
from .models import Review
from likes.models import Like


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    book_image = serializers.ReadOnlyField(source='book.cover.url')
    book_title = serializers.ReadOnlyField(source='book.title')
    book_author = serializers.ReadOnlyField(source='book.author')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        request = self.context['request']
        user = request.user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, review=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Review
        fields = [
            'id', 'book', 'title', 'description', 'book_started',
            'book_finished', 'rating', 'created_at', 'updated_at',
            'tags', 'draft', 'like_id', 'likes_count',
            'comments_count', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'book_image', 'book_title', 'book_author'
        ]
