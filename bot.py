import discord
from discord.ext import commands

# Crée une instance du bot
intents = discord.Intents.default()
intents.message_content = True  # Permet de lire le contenu des messages
bot = commands.Bot(command_prefix='!', intents=intents)

# Événement lorsque le bot est prêt
@bot.event
async def on_ready():
    print(f'{bot.user} est connecté à Discord !')

# Commande basique de test
@bot.command(name='ping', help='Répond avec Pong!')
async def ping(ctx):
    await ctx.send('Pong!')

# Commande pour dire bonjour
@bot.command(name='hello', help='Le bot dit bonjour')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.name}!')

# Gère les erreurs de commande
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Commande non trouvée.")
    else:
        print(f"Une erreur est survenue: {error}")
        await ctx.send("Désolé, une erreur est survenue.")

# Lancer le bot avec le token (remplace 'your_token' par ton token Discord)
bot.run('your_token')
