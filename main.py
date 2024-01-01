import discord
from discord.ext import commands
from discord import app_commands
from proofutils import ProofUtils

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
  print('Ready')
  await bot.tree.sync()

@bot.tree.command(name="proof", description="[BETA]")
@app_commands.choices(type=[
  app_commands.Choice(name='Boost 🪅', value=1),
  app_commands.Choice(name='Classic ❌', value=2),
  app_commands.Choice(name='Basic ⚡', value=3)
])
@app_commands.describe(question = "PUT \n FOR NEW LINE", response = "PUT \n for NEW LINE")
async def proof(interaction: discord.Interaction, type: app_commands.Choice[int], receiver_username: str, question: str, response: str):
  await interaction.response.defer(thinking=True)
  proof = ProofUtils(sender_username=interaction.user.name, sender_avatar=interaction.user.avatar.url, receiver_username=receiver_username, messages=[question, response], nitro_type=type.value).generate()
  await interaction.channel.send(content=f"Your Proof: <@{interaction.user.id}>", files=[discord.File(proof, "proof.png")])

@bot.tree.command(name="premium", description="Get Premium for FREE and unlock Roblox Giftcards & MORE PROOFS! 🤩")
async def premium(interaction):
  await interaction.response.send_message("Invite 2 owners = Premium (DM Vyro after) 🤯")

bot.run("MTA1NzM1NTg4NTI1ODc1MjAyMA.GmJ9TH.Wg6a7L-F355iMb9iPa945a1BFk9imKsyFL65qo")