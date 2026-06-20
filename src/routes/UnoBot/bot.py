import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

cores = ["R", "G", "B", "Y"]

partida = {
    "ativa": False,
    "jogadores": [],
    "maos": {},
    "baralho": [],
    "mesa": None,
    "turno": 0
}

def criar_baralho():
    deck = []

    for cor in cores:
        for n in range(10):
            deck.append(f"{cor}{n}")

        for _ in range(2):
            deck.append(f"{cor}+2")
            deck.append(f"{cor}SKIP")
            deck.append(f"{cor}REV")

    for _ in range(4):
        deck.append("WILD")
        deck.append("WILD+4")

    random.shuffle(deck)
    return deck

@bot.event
async def on_ready():
    print(f"{bot.user} online!")

@bot.command()
async def uno(ctx):
    partida["ativa"] = False
    partida["jogadores"] = []
    partida["maos"] = {}

    await ctx.send(
        "Partida criada!\nUse !entrar"
    )
@bot.command()
async def sair(ctx):

    if ctx.author not in partida["jogadores"]:
        await ctx.send("Você não está na partida.")
        return

    partida["jogadores"].remove(ctx.author)

    if ctx.author.id in partida["maos"]:
        del partida["maos"][ctx.author.id]

    await ctx.send(
        f"{ctx.author.mention} saiu da partida."
    )

    if len(partida["jogadores"]) < 2:
        partida["ativa"] = False

        await ctx.send(
            "Jogadores insuficientes. A partida foi encerrada."
        )
@bot.command()
async def entrar(ctx):

    if ctx.author in partida["jogadores"]:
        return

    partida["jogadores"].append(ctx.author)

    await ctx.send(
        f"{ctx.author.mention} entrou."
    )

@bot.command()
async def iniciar(ctx):

    if len(partida["jogadores"]) < 2:
        await ctx.send("São necessários 2 jogadores.")
        return

    partida["baralho"] = criar_baralho()

    for jogador in partida["jogadores"]:

        mao = []

        for _ in range(7):
            mao.append(
                partida["baralho"].pop()
            )

        partida["maos"][jogador.id] = mao

        try:
            await jogador.send(
                "Suas cartas:\n" +
                "\n".join(mao)
            )
        except:
            pass

    partida["mesa"] = partida["baralho"].pop()
    partida["turno"] = 0
    partida["ativa"] = True

    await ctx.send(
        f"Mesa: {partida['mesa']}\n"
        f"Turno: {partida['jogadores'][0].mention}"
    )

@bot.command()
async def mao(ctx):

    if ctx.author.id not in partida["maos"]:
        return

    await ctx.author.send(
        "\n".join(
            partida["maos"][ctx.author.id]
        )
    )

@bot.command()
async def comprar(ctx):

    atual = partida["jogadores"][partida["turno"]]

    if atual != ctx.author:
        return

    carta = partida["baralho"].pop()

    partida["maos"][ctx.author.id].append(carta)

    await ctx.author.send(
        f"Você comprou {carta}"
    )

    partida["turno"] = (
        partida["turno"] + 1
    ) % len(partida["jogadores"])

@bot.command()
async def jogar(ctx, *, carta):

    atual = partida["jogadores"][partida["turno"]]

    if atual != ctx.author:
        return

    mao = partida["maos"][ctx.author.id]

    if carta not in mao:
        await ctx.send(
            "Você não possui essa carta."
        )
        return

    mao.remove(carta)

    partida["mesa"] = carta

    if len(mao) == 1:
        await ctx.send(
            f"{ctx.author.mention} UNO!"
        )

    if len(mao) == 0:
        await ctx.send(
            f"🏆 {ctx.author.mention} venceu!"
        )

        partida["ativa"] = False
        return

    partida["turno"] = (
        partida["turno"] + 1
    ) % len(partida["jogadores"])

    await ctx.send(
        f"{ctx.author.mention} jogou {carta}\n"
        f"Mesa: {partida['mesa']}\n"
        f"Próximo: {partida['jogadores'][partida['turno']].mention}"
    )

bot.run(TOKEN)