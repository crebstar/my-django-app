from django.db import models

# Create your models here.

class Game(models.Model):
	name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	genre = models.CharField(max_length=80)
	age_limit = models.IntegerField(default=18)

	def __unicode__(self):
		return self.name

class GameDescription(models.Model):
	game = models.ForeignKey(Game)
	description = models.CharField(max_length=500)

	def __unicode__(self):
		return self.description


class GameRating(models.Model):
	game = models.ForeignKey(Game)
	rating = models.IntegerField(default=3)

	def __unicode__(self):
		return self.game.name


