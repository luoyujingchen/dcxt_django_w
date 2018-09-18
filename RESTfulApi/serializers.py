from rest_framework import serializers

# class DishSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=200)
#     price = serializers.FloatField()
#     pic = serializers.CharField(max_length=400,allow_blank=True)
#     introduction = serializers.CharField(allow_blank=True)
#     weights = serializers.IntegerField()# 权重，0 最大
#
#     def create(self, validated_data):
#         return Dish.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.price = validated_data.get('price',instance.price)
#         instance.pic = validated_data.get('pic',instance.pic)
#         instance.introduction = validated_data.get('introduction',instance.introduction)
#         instance.weights = validated_data.get('weights',instance.weights)
#         instance.save()
#         return instance
from dcxt.models import Dish


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ('name','price','discount_price','discount','weight','introduction')