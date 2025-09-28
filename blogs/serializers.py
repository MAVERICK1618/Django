from rest_framework import serializers
from .models import Blog , Comments


class CommentsSerializers( serializers.ModelSerializer ):
    
    class Meta:
        model = Comments
        fields = "__all__"
         
class BlogSerializers( serializers.ModelSerializer ):
    comments = CommentsSerializers(many = True , read_only = True)
    class Meta:
        model = Blog
        fields = "__all__"