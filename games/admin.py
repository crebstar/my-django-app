from django.contrib import admin
from games.models import Game, GameRating


class GameRatingInline(admin.StackedInline):
	model = GameRating
	extra = 0

class GameAdmin(admin.ModelAdmin):
	# Class GameAdmin extends admin.ModelAdmin class
	fields = ['name','pub_date','genre','age_limit']
	inlines = [GameRatingInline]


class GameRatingAdmin(admin.ModelAdmin):
	fields = ['game','rating']



admin.site.register(Game, GameAdmin)
