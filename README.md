# Gumbot
A discord bot coded with the discord.py library.
The name comes from why I'm coding this bot, to use in the discord server of the Twitch streamer [Gummiiy](https://www.twitch.tv/gummiiy)
# Features
- Unit conversion for distance, speed, weight and temperature
# Installation
## Environment variables
NOTE: you currently *have* to set all environment variables.
### TOKEN
The bot token to connect your bot to discord, you may look at this as an API key. (see setup below to find your bot token)
### OWNER_ID
The discord user ID that can run owner commands. For self hosting, I recommend setting this to your own user ID!
### COMMAND_PREFIX
The symbol or word to put in front of commands. For `!`, running for example the `ping` command would look like `!ping`.
> For any postgreSQL variables, please look at [the posgreSQL Docker documentation](https://github.com/docker-library/docs/blob/master/postgres/README.md)
## Setup
First, create a discord app and invite it to your (test) server.
1. Go to https://discord.com/developers/home and log in with discord
2. Under `Applications`, press `New Application` and give it a name (e.g. gumbot)
3. Under `Bot`, turn on all **Privileged Gateway Intents**. This is also where you find your `TOKEN`! Press **reset token** and copy it to somewhere, it won't be showed again!
4. Under `OAuth2`, find the **OAuth2 URL Generator** and select bot>administrator (I will add a specific permissions list later), copy the link and paste it into a new tab. Select the (test) server you want to add the bot to, and press continue, Authorize.
You'll also need the user ID of the person you want to give access to owner commands: https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID
## Final steps
> Make sure you have Docker and Docker-compose installed on your system
1. Clone the repo
2. Make sure you're working in the project's root directory
3. Rename `./.env.example` to `./.env`, and set the environment variables (see below)
4. Then run `docker compose up --build`, this will create the "gumbot" and "db"(postgreSQL) containers (db CURRENTLY unused)
This will start up the bot, the bot owner will have to send `!sync` (or with a different prefix) to sync the bot's command tree to discord. (you might have to reload discord after `!sync` to load the commands)