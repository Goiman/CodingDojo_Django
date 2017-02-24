from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		# "leagues": League.objects.all(),
		# "teams": Team.objects.all(),
		# "players": Player.objects.all(),

		"teams1": Team.objects.all().filter(league__name__contains="Atlantic Soccer"),#1.

		"players": Player.objects.all().filter(curr_team__team_name__contains="Penguins"),#2.

		"players1": Player.objects.all().filter(curr_team__league__name__startswith="International Collegiate"),#3.

		"players2": Player.objects.all().filter(curr_team__league__name__startswith="American Conference").filter(last_name="Lopez"),#4.

		"players3": Player.objects.all().filter(curr_team__league__sport="Football"),#5

		"teams2": Team.objects.all().filter(curr_players__first_name="Sophia"),#6.

		"leagues": League.objects.all().filter(teams__curr_players__first_name="Sophia"),#7.

		"players4": Player.objects.all().filter(last_name = "Flores").exclude(curr_team__team_name="Roughriders"),#8.

		"teams3": Team.objects.all().filter(all_players__first_name="Samuel"),#9.

		'manitoba':Player.objects.filter(all_teams__team_name__contains="Tiger-Cats"),#10

        'wichita':Player.objects.filter(all_teams__team_name__contains="Vikings").exclude(curr_team__team_name__contains="Vikings"),#11

        'jacob':Team.objects.filter(all_players__first_name="Jacob").filter(all_players__last_name="Gray").exclude(location='Oregon'),#12

		"players5": Player.objects.all().filter(all_teams__league__name__contains="Atlantic Federation").filter(first_name="Joshua"),#13

		"12teams":Team.objects.annotate(num_player=Count('all_players')).filter(num_player__gte=12),#14
       "tplayers":Player.objects.annotate(num_team=Count('all_teams')).order_by('num_team'),#15
		# Simple finds
		# "leagues": League.objects.all().filter(sport="Baseball"),#1
		# "leagues": League.objects.all().filter(name__contains="Womens"),#2
		# "leagues": League.objects.all().filter(sport__contains="Hockey"),#3
		# "leagues": League.objects.all().filter(sport__icontains="Football"),#4
		# "leagues": League.objects.all().filter(name__contains="Conference"),#5
		# "leagues": League.objects.all().filter(name__contains="Atlantic"),#6

		# "teams": Team.objects.all().filter(location="Dallas"),#7
		# "teams": Team.objects.all().filter(team_name__contains="Raptors"),#8
		# "teams": Team.objects.all().filter(location__contains="City"),#9
		# "teams": Team.objects.all().filter(team_name__startswith="T"),#10
		# "teams": Team.objects.all().order_by("location"),#11
		# "teams": Team.objects.all().order_by("team_name"),#12

		# "players": Player.objects.all().filter(last_name__contains="Cooper"),#13
		# "players": Player.objects.all().filter(first_name__contains="Joshua"),#14
		# "players": Player.objects.all().filter(last_name__contains="Cooper").filter(first_name__icontains="Joshua"),#15
		# "players": Player.objects.all().filter(first_name__contains="Alexander").filter(first_name__contains="Wyatt"),#16

		# ForeignKey Relationships
		# "teams": Team.objects.all().filter(league__name__contains="Atlantic Soccer"),#1. Find all teams in the Atlantic Soccer Conference
		# "players": Player.objects.all().filter(team__team_name__contains="Penguins"),#2. Find all (current) players on the Boston Penguins

		# "players":Player.objects.all().filter(league__name__startswith="International"),#3. Find all (current) players in the International Collegiate Baseball Conference
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
