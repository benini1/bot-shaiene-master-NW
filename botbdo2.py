import os
import discord
from discord.ext import commands

token = os.environ.get('token')
description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def comandos(ctx):

    embed = discord.Embed(color=0xeee657)
    embed.add_field(name="!diarios", value="Guia dos diários", inline="false")
    embed.add_field(name="!buffxp", value="Buffs para Leveling", inline="false")
    embed.add_field(name="!cdw", value="Discord e site da CDW", inline="false")
    embed.add_field(name="!fps", value="Guia para melhorar a performance do BDO", inline="false")
    embed.add_field(name="!tesouros", value="Itens tesouro do BDO", inline="false")
    embed.add_field(name="!portais", value="Possíveis locais dos portais Aakman/Hystria no deserto", inline="false")
    embed.add_field(name="!hystria", value="Mapa das rotações de Hystria", inline="false")
    embed.add_field(name="!permuta", value="Informações referentes a permuta", inline="false")
    embed.add_field(name="!db", value="Database dos itens do BDO", inline="false")
    embed.add_field(name="!discordclasses", value="Discord das classes do jogo", inline="false")

    await ctx.send("{0.author.mention}".format(ctx), embed=embed)

@bot.command()
async def diarios(ctx):
    embed = discord.Embed(color=0xeee657)
    embed.add_field(name="!deve", value="Guia diarios Deve", inline="false")
    embed.add_field(name="!dorin", value="Guia diarios Dorin", inline="false")
    embed.add_field(name="!agris", value="Guia diarios Agris", inline="false")
    embed.add_field(name="!bartali", value="Guia diarios Bartali", inline="false")

    await ctx.send("{0.author.mention}".format(ctx), embed=embed)

@bot.command()
async def deve(ctx):
    embed = discord.Embed(color=0xeee657)
    embed.add_field(name="Diarios de Deve", value="http://bit.ly/devediario")
    embed.set_footer(text="Guia feito por @PandaDruj www.twitch.tv/pandadruj")

    await ctx.send("{0.author.mention}".format(ctx), embed=embed)

@bot.command()
async def dorin(ctx):
    embed = discord.Embed(color=0xeee657)
    embed.add_field(name="Diarios de Dorin", value="https://tinyurl.com/dorinmorgrim")
    embed.set_footer(text="Guia feito por @PandaDruj www.twitch.tv/pandadruj")

    await ctx.send("{0.author.mention}".format(ctx), embed=embed)

@bot.command()
async def agris(ctx):
    embed = discord.Embed(color=0xeee657)
    embed.add_field(name="Diarios de Agris", value="https://tinyurl.com/diarioagris")
    embed.set_footer(text="Guia feito por @PandaDruj www.twitch.tv/pandadruj")

    await ctx.send("{0.author.mention}".format(ctx), embed=embed)


@bot.command()
async def bartali(ctx):
    embed = discord.Embed(color=0xeee657)
    embed.add_field(name="Volume 1-10", value="https://bit.ly/2GDdFdv", inline="false")
    embed.add_field(name="Volume 11-15", value="http://bit.ly/volumes11-15", inline="false")
    embed.add_field(name="Guia em vídeo do @xuxatv www.twitch.tv/xuxatv", value="https://bit.ly/xuxabartali")

    await ctx.send("{0.author.mention}".format(ctx), embed=embed)

@bot.command()
async def fps(ctx):
    embed = discord.Embed(color=0xeee657)
    embed.add_field(name="Guia de melhora de performance para o BDO", value="https://tinyurl.com/bdoperformance")
    embed.set_footer(text="Guia feito por @PandaDruj www.twitch.tv/pandadruj")

    await ctx.send("{0.author.mention}".format(ctx), embed=embed)

@bot.command()
async def buffxp(ctx):
    embed = discord.Embed(color=0xeee657)
    embed.add_field(name="200% / 600%", value="Diária no Y 200% - pode-se juntar 3x através da Alquimia Simples para obter scroll 600%", inline="false")
    embed.add_field(name="100%",value="Pergaminho XP ou Livro de Combate", inline="false")
    embed.add_field(name="100%", value="Sino", inline="false")
    embed.add_field(name="20%", value="Comida – Cron Simples", inline="false")
    embed.add_field(name="20%", value="Elixir da Fera", inline="false")
    embed.add_field(name="20%", value="Buff do Espírito Negro (lvl 50+)", inline="false")
    embed.add_field(name="3% a 15%", value="Buff do Padre", inline="false")
    embed.add_field(name="20%", value="2x Cristais de XP no Elmo", inline="false")
    embed.add_field(name="5%", value="4x Cristais HON Gervish", inline="false")
    embed.add_field(name="5%", value="4x Cristais HON Makalod", inline="false")
    embed.add_field(name="--------------------------------------------------------------------------------------------------", value="Buffs P2w abaixo", inline="false")
    embed.add_field(name="--------------------------------------------------------------------------------------------------", value="\u200b", inline="false")
    embed.add_field(name="100%", value="Livro Lua Minguante", inline="false")
    embed.add_field(name="30%", value="Pacote Econômico", inline="false")
    embed.add_field(name="10%", value="Buff da barraca (Habilidade e experiência)", inline="false")
    embed.add_field(name="10%", value="Costume de Cash", inline="false")

    await ctx.send("{0.author.mention}".format(ctx), embed=embed)

@bot.command()
async def cdw(ctx):
    embed = discord.Embed(color=0xeee657)
    embed.add_field(name="Site da CDW", value="http://cdw-app-gameguild.herokuapp.com")

    await ctx.send("{0.author.mention} https://discord.gg/5k6pQem".format(ctx), embed=embed)

@bot.command()
async def tesouros(ctx):
    embed = discord.Embed(color=0xeee657)
    embed.add_field(name="!mapa", value="Mapa")
    embed.add_field(name="!bussola", value="Bússola", inline="false")
    embed.add_field(name="!pothp", value="Pot HP")
    embed.add_field(name="!potmp", value="Pot MP")

    await ctx.send("{0.author.mention}".format(ctx), embed=embed)

@bot.command()
async def mapa(ctx):
    img = discord.File("img/mapa.jpg", filename="img/mapa.jpg")
    await ctx.send("{0.author.mention}".format(ctx), file=img)

@bot.command()
async def bussola(ctx):
    img = discord.File("img/bussola.jpg", filename="img/bussola.jpg")
    await ctx.send("{0.author.mention}".format(ctx), file=img)

@bot.command()
async def pothp(ctx):
    img = discord.File("img/pot_hp.jpg", filename="img/pot_hp.jpg")
    await ctx.send("{0.author.mention}".format(ctx), file=img)

@bot.command()
async def potmp(ctx):
    img = discord.File("img/pot_wp.jpg", filename="img/pot_wp.jpg")
    await ctx.send("{0.author.mention}".format(ctx), file=img)

@bot.command()
async def hystria(ctx):
    img = discord.File("img/hystria.png", filename="img/hystria.png")
    await ctx.send("{0.author.mention}".format(ctx), file=img)

@bot.command()
async def portais(ctx):
    img = discord.File("img/portais.png", filename="img/portais.png")
    await ctx.send("{0.author.mention}".format(ctx), file=img)

@bot.command()
async def permuta(ctx):
    embed = discord.Embed(color=0xeee657)
    embed.add_field(name="!rotas", value="Quantidade de permutas para liberar novas rotas", inline="false")
    embed.add_field(name="!barcos", value="As variações de expansão de Veleiro/Fragata disponíveis", inline="false")
    embed.add_field(name="!craftbarcos", value="Materiais para craft dos barcos", inline="false")
    embed.add_field(name="!itensmercante", value="Itens azuis do navio Mercante para se fazer a Carraca", inline="false")

    await ctx.send("{0.author.mention}".format(ctx), embed=embed)

@bot.command()
async def rotas(ctx):
    img = discord.File("img/rotasimg.png", filename="img/rotasimg.png")
    await ctx.send("{0.author.mention}".format(ctx), file=img)

@bot.command()
async def barcos(ctx):
    img = discord.File("img/vbarcos.png", filename="img/vbarcos.png")
    await ctx.send("{0.author.mention}".format(ctx), file=img)

@bot.command()
async def craftbarcos(ctx):
    await ctx.send("{0.author.mention} https://bit.ly/craftbarcos".format(ctx))

@bot.command()
async def itensmercante(ctx):
    img = discord.File("img/imgmercante.png", filename="img/imgmercante.png")
    await ctx.send("{0.author.mention}".format(ctx), file=img)

@bot.command()
async def npcmargoria(ctx):
    img = discord.File("img/mercadores.png", filename="img/mercadores.png")
    await ctx.send("{0.author.mention}".format(ctx), file=img)

@bot.command()
async def db(ctx):
    await ctx.send("{0.author.mention} http://bdocodex.com/pt".format(ctx))

@bot.command()
async def discordclasses(ctx):
    embed = discord.Embed(color=0xeee657)
    embed.add_field(name="!musa", value="Musa/Maehwa")
    embed.add_field(name="!ninja", value="Ninja/Kunoichi")
    embed.add_field(name="!ranger", value="Caçadora")
    embed.add_field(name="!sorc", value="Feiticeira")
    embed.add_field(name="!tamer", value="Domadora")
    embed.add_field(name="!valk", value="Valquíria")
    embed.add_field(name="!warrior", value="Guerreiro")
    embed.add_field(name="!wizz", value="Bruxa/Mago")
    embed.add_field(name="!zerk", value="Berserker")
    embed.add_field(name="!dk", value="Cavaleira das Trevas")
    embed.add_field(name="!striker", value="Lutador/Mística")
    embed.add_field(name="!lahn", value="Lahn")
    embed.add_field(name="!archer", value="Arqueiro")
    embed.add_field(name="!shai", value="Shai")
    embed.add_field(name="!guardian", value="Guardiã")

    await ctx.send("{0.author.mention}".format(ctx), embed=embed)

@bot.command()
async def musa(ctx):
    await ctx.send("{0.author.mention} https://discord.gg/6ThcWqx".format(ctx))

@bot.command()
async def ninja(ctx):
    await ctx.send("{0.author.mention} https://discord.gg/VSuuF5g".format(ctx))

@bot.command()
async def ranger(ctx):
    await ctx.send("{0.author.mention} https://discord.gg/J2Andmk".format(ctx))

@bot.command()
async def sorc(ctx):
    await ctx.send("{0.author.mention} https://discord.gg/GWz9SNd".format(ctx))

@bot.command()
async def tamer(ctx):
    await ctx.send("{0.author.mention} https://discord.gg/zn6puC6".format(ctx))

@bot.command()
async def valk(ctx):
    await ctx.send("{0.author.mention} https://discord.gg/XrzrZzn".format(ctx))

@bot.command()
async def warrior(ctx):
    await ctx.send("{0.author.mention} https://discord.gg/6s3ZBRN".format(ctx))

@bot.command()
async def wizz(ctx):
    await ctx.send("{0.author.mention} https://discord.gg/tsSvKsG".format(ctx))

@bot.command()
async def zerk(ctx):
    await ctx.send("{0.author.mention} https://discord.gg/83Ny223".format(ctx))

@bot.command()
async def dk(ctx):
    await ctx.send("{0.author.mention} http://discord.gg/nF6xb3g https://discord.gg/G6KfErT".format(ctx))

@bot.command()
async def striker(ctx):
    await ctx.send("{0.author.mention} https://discord.gg/fRWVwRD".format(ctx))

@bot.command()
async def lahn(ctx):
    await ctx.send("{0.author.mention} https://discord.gg/nRBXMtW".format(ctx))

@bot.command()
async def archer(ctx):
    await ctx.send("{0.author.mention} https://discord.gg/NfvbMZe".format(ctx))

@bot.command()
async def shai(ctx):
    await ctx.send("{0.author.mention} https://discord.gg/vq68zAG".format(ctx))

@bot.command()
async def guardian(ctx):
    await ctx.send("{0.author.mention} https://discord.gg/9jdEmYp".format(ctx))


bot.run(token)
