import requests
from discord_webhook import DiscordWebhook, DiscordEmbed


webhook = DiscordWebhook(url='WEBHOOK URL TOP SECRET KIDE')

embed = DiscordEmbed(title='<a:alarm:905101481785561229> Výpadek TrospySMP <a:alarm:905101481785561229>', description='Pracujeme na opravě! <a:pepeHacker:933465128328888361> ', color='FF0000')
embed.set_timestamp()
webhook.add_embed(embed)

r = requests.get('https://trospysmp.wtf/')

if r.status_code == 404 :
    print("Code 404")
    response = webhook.execute()
