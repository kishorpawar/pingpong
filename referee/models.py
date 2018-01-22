# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# django imports
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


GAME_STATUS = (
	('QUEUED', 'QUEUED'),
	('STARTED', 'STARTED'),
	('IN-PROGRESS', 'IN-PROGRESS'),
	('COMPLETE', 'COMPLETE'),
	('TIE', 'TIE'),
	('CANCELLED', 'CANCELLED'),
	)

GAME_TYPE = (
	('LEAGUE', 'LEAGUE'),
	('QUARTER_FINAL', 'QUARTER FINAL'),
	('SEMI_FINAL', 'SEMI FINAL'),
	('FINAL', 'FINAL'),
	)


class Game(models.Model):
	referee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referee')
	player_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='opponent_1')
	player_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='opponent_2')
	attacker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attacker')
	status = models.CharField(max_length=20, choices=GAME_STATUS, default='QUEUED')
	game_type = models.CharField(max_length=20, choices=GAME_TYPE, default='LEAGUE')


class Score(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='games')
	player_1_score = models.PositiveSmallIntegerField()
	player_2_score = models.PositiveSmallIntegerField()

class Play(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='running_games')
	# attacker = 