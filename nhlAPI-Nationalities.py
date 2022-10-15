#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import json
import requests
import numpy as np
import pickle

game_data = []
year = '/2022'
season_type = '02'

base = 'https://statsapi.web.nhl.com/api/v1/'
results = requests.get('https://statsapi.web.nhl.com/api/v1/teams')


teams = results.json()

rosterDict = {}

for team  in  teams['teams']:
    results = requests.get('https://statsapi.web.nhl.com/api/v1/teams/'+ str(team['id']) + '/roster')
    data = results.json()
    rosterDict[team['id']] =  data['roster']

bioData = pd.DataFrame()
for team in teams['teams']:
    teamId = team['id']
    for player in rosterDict[teamId]:
        playerId = player['person']['id']
        response = requests.get(base+'people/'+str(playerId))
        bio = response.json()
        data = pd.json_normalize(bio['people'])
        bioData = bioData.append(data)


endUrl = '/stats?stats=statsSingleSeason&season=20212022'
stats2022 = pd.DataFrame()
for player in bioData['id']:
    playerId = player
    response = requests.get(base+'people/'+str(playerId)+endUrl)
    stats = response.json()
    for stat in stats['stats']:
        row = pd.json_normalize(stat['splits'])
        row.insert(0,'id',playerId)
        stats2022 = stats2022.append(row)

stats2022.to_csv('stats2022NHL.csv')
bioData.to_csv('bioDataNHL.csv')



