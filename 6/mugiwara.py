import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="md", help_command=None, intents=disnake.Intents.all())

@bot.event
async def on_ready():
    print(f"Бот {bot.user} присоединился к команде")

@bot.slash_command()
async def arone(ctx):
    emb = disnake.Embed(
        title="Сборник One Piece",
        color=0x9932cc,
        description="В ван писе существует множество арок:"
    
    )

    emb.add_field(name=":one: Начало приключений мугивар, 1-30 ep.", value="Начало приключенний Луффи, новые товарищи. Филлерные серии отсутствуют", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":two: Арлонг Парк, 31-44 ep.", value="Новый антогонист, история картогрофа Нами. Филлеры: 46-47", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":three: Логтаун, 48-53 ep.", value="История острова. Последняя арка в Ист Блю. Филлеры: 61", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":four: Реверс Маунтин и Виски Пик, 62-67 ep.", value="Новое путешествие команды мугивар. Филлеры: 68-69", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":five: Литл Гарден и Острова Драм, 70-91 ep.", value="Маленькая арка, но очень важная. Филлеры отсутствуют", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":six: Алабаста, 92-130 ep.", value="Арка алабаста или война в алабасте. Новый противник мугивар и новые накама. Филлеры: 101", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":seven: Джая и Скайпия, 144-195 ep.", value="Покорение небесного острова и встреча с новыми антогонистами", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":eight: Water 7, 229-263 ep.", value="Новый накаме мугивар. Плотник Френки и секретная организация CP9", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":nine: Эниес Лобби, 264-312 ep.", value="CP9 и история нового накаме", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":one: :zero: Триллер Барк, 337-381 ep.", value="Трагичная история острова. Новый антогонист Шичибукай и новый накаме. Филлеры: 354", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":one: :two: Архипелаг Саубоди, 385-405 ep.", value="Что происходит с командой, если её разделить?", inline=False) 

    emb.set_author(name = bot.user.name, icon_url = bot.user.avatar.url)

    await ctx.send(embed = emb)

@bot.slash_command()
async def artwo(ctx):
    emb = disnake.Embed(
        title="Сборник One Piece, часть два",
        color=0x9932cc,
        description="В ван писе существует множество арок:"
    )
    
    emb.add_field(name=":one: :three: Амазон Лили и Импел Даун, 408-452 ep.", value="Легендарная тюрьма Импел Даун, где заточён брат Луффи и остров женщин Амазон Лили. Филлер: 421", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":one: :four: Маринфорд, 457-489 ep.", value="Легендарный пират и спасение сына короля пиратов", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":one: :five: После войны, 490-516 ep.", value="Последствия войны с белоусом. Худшее поколение", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":one: :six: Остров Рыболюдей и возвращение на Саубоди, 517-574 ep.", value="Возвращение команды мугивар и новые путешествия. Филлеры: 520", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":one: :seven: Панк Хазард, 579-625 ep.", value="Доктор Клаус и тайна острова Панк Хазард", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":one: :eight: Дресс Роуз, 629-746", value="", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":one: :nine: Дзо / Зоя, 751-779 ep.", value="", inline=False)
    emb.add_field(name="", value="", inline=False)
    emb.add_field(name=":two: :zero: Пирожный остров, 783-877 ep.", value="", inline=False)
    emb.set_author(name = bot.user.name, icon_url = bot.user.avatar.url)

    await ctx.send(embed = emb)

bot.run("MTEwNjk4MDk5ODIyNDI4MTY2Mw.Gn5SXR.Dmfl_B_AC7JezEMeJxwUMWUuA16PIiBgNV-7uY")
