'''
Created on 2020/12/04

@author: Masaya Misaizu
'''
from riotwatcher import RiotWatcher

API_KEY = #API KEY which you will use
watcher = RiotWatcher(API_KEY)

region = 'kr' #server name.
name = 'Hide on bush' # Player name,I put the LoL pro gamer name in this case. His account:https://www.op.gg/summoner/userName=Hide%20on%20bush

summoner = watcher.summoner.by_name(region, name)
#This will shows the data of the player
summoner

match = watcher.match.matchlist_by_account(region, summoner['accountId'])
#Shows recent match list