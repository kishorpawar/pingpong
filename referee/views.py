# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# django imports
from django.shortcuts import render
from django.contrib.auth.models import User as Player

# rest_framework import
from rest_framework import viewsets

# serializrs import 
from referee.serializers import GameSerializer, PlayerSerializer

# import models
from referee.models import Game

# Create your views here.


class GameViewSet(viewsets.ModelViewSet):
	queryset = Game.objects.all()
	serializer_class = GameSerializer


class PlayerViewSet(viewsets.ModelViewSet):
	queryset = Player.objects.all()
	serializer_class = PlayerSerializer
