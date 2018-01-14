# rest_framework import
from rest_framework import serializers

#model imports
from referee.models import Game
from django.contrib.auth.models import User as Player

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Player
		fields = ('username',)

class GameSerializer(serializers.HyperlinkedModelSerializer):

	players = PlayerSerializer(many = True, read_only = True)
	class Meta:
		model = Game
		fields = ('referee', 'players', 'attacker', 'status', 'game_type')

