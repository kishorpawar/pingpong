# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# django imports
from django.shortcuts import render
from django.contrib.auth.models import User as Player

# rest_framework import
from rest_framework import viewsets, status
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# serializrs import 
from referee.serializers import GameSerializer, PlayerSerializer, ScoreSerializer

# import models
from referee.models import Game, Score

from referee import attributes as attr
from referee.permissions import RefereePermission
# Create your views here.


class GameViewSet(viewsets.ModelViewSet):
	queryset = Game.objects.all()
	serializer_class = GameSerializer
	permission_classes = (IsAuthenticated, RefereePermission)

	def create(self, request):

		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception = True)
		data = serializer.validated_data

		player_1 = data["player_1"].username
		player_2 = data["player_2"].username

		if attr.DEFENCE_ARRAY[player_1] == attr.DEFENCE_ARRAY[player_2]:
			if Game.objects.filter(player_1 = data["player_1"], 
									player_2 = data["player_2"],
									game_type = data["game_type"]).exists():
				raise ValidationError("Game for them is already created.")
			self.perform_create(serializer)
			return Response(serializer.data, status.HTTP_201_CREATED)
		else:
			return Response("DEFENCE_ARRAY should have same no. of elements.", status.HTTP_406_NOT_ACCEPTABLE)

class PlayerViewSet(viewsets.ModelViewSet):
	queryset = Player.objects.all()
	serializer_class = PlayerSerializer


class ScoreViewSet(viewsets.ModelViewSet):
	queryset = Score.objects.all()
	serializer_class = ScoreSerializer

	def create(self, request):
		serializer = self.get_serializer(data = request.data)
		serializer.is_valid(raise_exception = True)