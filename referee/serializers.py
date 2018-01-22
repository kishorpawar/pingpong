# rest_framework import
from rest_framework import serializers

#model imports
from referee.models import Game, Score
from django.contrib.auth.models import User as Player

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Player
		fields = ('username',)

class GameSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Game
		fields = ('__all__')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Score
		fields = ('__all__')