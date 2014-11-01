"""
Generator of fixtures for round-robin head-to-head sports or gaming competitions. Provides fixtures from a list of teams.
"""

import random

def rotate(teamlist):
	x = len(teamlist) / 2
	hosts, visitors = teamlist[:x], teamlist[x:]
	return hosts[:1] + visitors[:1] + hosts[1:-1] + visitors[1:] + hosts[-1:]

def matchup(teamlist, reverse=False):
	x = len(teamlist) / 2
	hosts, visitors = teamlist[:x], teamlist[x:]

	if reverse:
		return zip(visitors, hosts)
	else:
		return zip(hosts, visitors)

def fixtures(teams, rounds=1, shuffle_first=True):

	if len(teams) % 2 == 1: # odd number of teams; add a bye
		teams = list(teams) + ['bye']

	if shuffle_first:
		random.shuffle(teams)

	fixtures = []

	for each in xrange(len(teams) - 1):
		teams = rotate(teams)
		fixtures.append(teams)

	random.shuffle(fixtures)

	final_fixtures = []

	for round_no in xrange(rounds):
		reverse = round_no % 2
		for schedule_no, schedule in enumerate(fixtures):
			if schedule_no % 2 == 1:
				final_fixtures.append(matchup(schedule, reverse=reverse))
			else:
				final_fixtures.append(matchup(schedule, reverse=(not reverse)))

	return final_fixtures