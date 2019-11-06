from steamUser import steamUser

# Initialize the steamUser class with the user's SteamID and your Steam API Key
# This API Key is invalid, make sure you are using a valid one
user = steamUser("76561198294489872", "3324D9923DD5D196F63E02160C36F20D")

# Get the user's information
userInfo = user.getUser()

# Get the user game count and a list of games
gameCount, userGames = user.getGames()

# Check if the user is banned and the amount of bans
vacBanned, banCount = user.getBans()