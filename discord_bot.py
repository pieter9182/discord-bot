import discord
intents = discord.Intents.default()
intents.messages= True
client = discord.Client(intents=intents)
def on_ready():
    guild = client.guilds(0)
    print(guild.name, "is the name of the server")
    print(client.user, "has connected to the client")


client.run("MTAzNzY1NjY0MzQzOTE4NTkyMA.Gv5_1a.Kb-cymvXcF5maeQmANZihOUxhcwS-PUOZz3-ns")

