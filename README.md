# Python SteamUser
An easy-to-use Python Library to get information about steam users with just 2 lines of code

## Installation

 1. Make sure [Requests](https://pypi.org/project/requests/) is installed, as it's required
 2. Download the latest version of this repository and put it in your project
 3. Import the steamUser class with `from steamUser import steamUser`
 4. If you want a example, check out [example.py](https://github.com/dev-zeo/python-steamuser/blob/master/example.py)

## Getting started

 1. Make sure you have a valid Steam Web API key from [this link](https://steamcommunity.com/dev/apikey)
 2. Initialize the steamUser class with a SteamID64 and your API key
 3. You now have access to various functions from this class

## User Class
If you have initialized the steamUser class you have access to this below given functions
### getUser()
This function returns a dictionary of user information, an example return would be:
```python
{
	"name": "zeo",
	"steamid": "STEAM_0:0:145738165",
	"steamid64": "76561198251742058",
	"profileurl": "[https://steamcommunity.com/id/zeo-dev/](https://steamcommunity.com/id/zeo-dev/)",
	"onlinestate": "Online",
	"visibilityState": "Public",
	"avatars": {
		"normal": "",
		"medium": "",
		"full": ""
	}
}
```
### getGames(includeFree = False)
Returns the amount of games the user has and a list of game objects. If includeFree is True, it will also return the free games.

> Keep in mind that this will return None, None if the steam profile is Private or Friends Only

An example of a game object would be:
```python
{
	"id": "4000",
	"name": "Garry's Mod",
	"playtime": "4290"
}
```
### getBans()
Returns if the user has been VAC banned once and the amount of VAC bans the user has.

## Credits
https://gist.github.com/bcahue/4eae86ae1d10364bb66d for the SteamID64 to SteamID convert function