#-------------------------------------------------------------Импорт библиотек-------------------------------------------------------------

import disnake
from disnake.ext import commands

#-------------------------------------------------------------Интенты-------------------------------------------------------------

intents = disnake.Intents.all()
intents.members = True
intents.voice_states = True
intents.presences = True

#-------------------------------------------------------------Переменные-------------------------------------------------------------

bot = commands.Bot(command_prefix="!", help_command=None, intents=intents)

#-------------------------------------------------------------Ивент 'on ready'-------------------------------------------------------------

@bot.event
async def on_ready():
    print("Ваш бот запущен.")

#-------------------------------------------------------------Слеш команда '/oge'-------------------------------------------------------------

@bot.slash_command()
async def oge(inter: disnake.ApplicationCommandInteraction):
    emb = disnake.Embed(
        description="**Используйте навигацию ниже, чтобы выбрать *экзамен* и нужный вам *вариант***.",
        title="**Подготовка к ОГЭ**.",
        color=0x00bfff)
    await inter.response.send_message(embed = emb,
        components=[
            disnake.ui.Button(label="Информатика", style=disnake.ButtonStyle.blurple, custom_id="inf"),
            disnake.ui.Button(label="Русский", style=disnake.ButtonStyle.blurple, custom_id="rus"),
            disnake.ui.Button(label="История", style=disnake.ButtonStyle.blurple, custom_id="hist"),
            disnake.ui.Button(label="Общество", style=disnake.ButtonStyle.blurple, custom_id="obsh"),
        ]
    )

#-------------------------------------------------------------  Слеш команда 'start, ege'-------------------------------------------------------------

@bot.slash_command()
async def start(ctx):
    emb = disnake.Embed(
        description="**Спасибо, что Вы начали пользоваться ботом.\n\nЧтобы начать готовиться к Общему Государственному Экзамену пропишите - /oge\n\nЧтобы начать готовиться к Единому Государственному Экзамену пропишите - /ege**",
        color=0x12323,
        title=f"**Приветствую, {ctx.author.nick}!**"
    )
    await ctx.send(embed = emb)

@bot.slash_command()
async def ege(ctx):
    emb = disnake.Embed(
        description="**Команда находится в разработке...**",
        title="**Ошибка!**",
        color=0x12323
    )
    await ctx.send(embed = emb)

#-------------------------------------------------------------Ответ по нажатию на кнопку 1-------------------------------------------------------------

@bot.listen("on_button_click")
async def informatic(inter: disnake.MessageInteraction):
    if inter.component.custom_id not in ["inf", "rus", "hist", "obsh", "5", "6", "7", "8", "9", "10"]:
        return
    
#-------------------------------------------------------------Первая кнопка-------------------------------------------------------------

    if inter.component.custom_id == "inf":
        emb = disnake.Embed(
            description="**Выберите номер варианта снизу**",
            title="**Вы выбрали информатику**",
            color=0x00bfff)     
        await inter.response.send_message(embed = emb,
            components=[
                disnake.ui.Button(label="1", style=disnake.ButtonStyle.blurple, custom_id="infvar1"),
                disnake.ui.Button(label="2", style=disnake.ButtonStyle.blurple, custom_id="infvar2"),
                disnake.ui.Button(label="3", style=disnake.ButtonStyle.blurple, custom_id="infvar3"),
                disnake.ui.Button(label="4", style=disnake.ButtonStyle.blurple, custom_id="infvar4"),
                disnake.ui.Button(label="5", style=disnake.ButtonStyle.blurple, custom_id="infvar5")            
            ]
        )

#------------------------------------------------------------Вторая кнопка-------------------------------------------------------------

    if inter.component.custom_id == "rus":
        emb = disnake.Embed(
            title="**Вы выбрали русский язык**",
            description="**Выберите номер варианта снизу**",
            color=0xfff5ee)
        await inter.response.send_message(embed = emb,
          components=[
                disnake.ui.Button(label="1", style=disnake.ButtonStyle.blurple, custom_id="rus1"),
                disnake.ui.Button(label="2", style=disnake.ButtonStyle.blurple, custom_id="rus2"),
                disnake.ui.Button(label="3", style=disnake.ButtonStyle.blurple, custom_id="rus3"),
                disnake.ui.Button(label="4", style=disnake.ButtonStyle.blurple, custom_id="rus4"),
                disnake.ui.Button(label="5", style=disnake.ButtonStyle.blurple, custom_id="rus5")                
            ]
        )

#-------------------------------------------------------------Третья кнопка-------------------------------------------------------------

    if inter.component.custom_id == "hist":
        emb = disnake.Embed(
            title="**Вы выбрали историю**",
            description="**Выберите номер варианта снизу**",
            color=0xc9a0dc
        )
        await inter.response.send_message(embed = emb,
          components=[
                disnake.ui.Button(label="1", style=disnake.ButtonStyle.blurple, custom_id="histvariant1")                           
            ]
        )
#-------------------------------------------------------------Четвертая кнопка-------------------------------------------------------------

    if inter.component.custom_id == "obsh":
        emb = disnake.Embed(
            title="**Вы выбрали общество**",
            description="**Выберите номер варианта снизу**",
            color=0xafeeee
        )
        await inter.response.send_message(embed = emb,
          components=[
                disnake.ui.Button(label="1", style=disnake.ButtonStyle.blurple, custom_id="obshvariant1"),           
            ]
        )                                 
#-------------------------------------------------------------Пятая кнопка-------------------------------------------------------------

    if inter.component.custom_id == "5":
        await inter.response.send_message("5")

    if inter.component.custom_id == "6":
        await inter.response.send_message("")

    if inter.component.custom_id == "7":
        await inter.response.send_message("")

    if inter.component.custom_id == "8":
        await inter.response.send_message("")

    if inter.component.custom_id == "9":
        await inter.response.send_message("")

    if inter.component.custom_id == "10":
        await inter.response.send_message("")

#-------------------------------------------------------------Ответ по нажатию на кнопку 2-------------------------------------------------------------

@bot.listen("on_button_click")
async def chyto(inter: disnake.MessageInteraction):
    if inter.component.custom_id not in ["infvar1", "infvar2", "infvar3", "infvar4", "infvar5", "rus1", "rus2", "rus3", "rus4", "rus5", "histvariant1", "obshvariant1"]:
        return

#-------------------------------------------------------------Варианты русский-------------------------------------------------------------

    if inter.component.custom_id == "rus1":
        emb = disnake.Embed(
            title="**Вы выбрали первый вариант**",
            description="**Выберите номер задания ниже**",
            color=0xafeeee)    

        await inter.response.send_message(embed = emb,
            components=[
                disnake.ui.Button(label="4-6", style=disnake.ButtonStyle.blurple, custom_id="zadrus1"),
                disnake.ui.Button(label="7-9", style=disnake.ButtonStyle.blurple, custom_id="zadrus2"),
                disnake.ui.Button(label="Текст", style=disnake.ButtonStyle.blurple, custom_id="zadrus3"),
                disnake.ui.Button(label="10-12", style=disnake.ButtonStyle.blurple, custom_id="zadrus4"),
            ]
        )

    if inter.component.custom_id == "rus2":
        emb = disnake.Embed(
            title="**Вы выбрали второй вариант**",
            description="**Выберите номер задания ниже**",
            color=0xafeeee)            
        await inter.response.send_message(embed = emb,
            components=[
                disnake.ui.Button(label="4-6", style=disnake.ButtonStyle.blurple, custom_id="zadrus5"),
                disnake.ui.Button(label="7-9", style=disnake.ButtonStyle.blurple, custom_id="zadrus6"),
                disnake.ui.Button(label="Текст", style=disnake.ButtonStyle.blurple, custom_id="zadrus7"),
                disnake.ui.Button(label="10-12", style=disnake.ButtonStyle.blurple, custom_id="zadrus8"),
            ]
        )


    if inter.component.custom_id == "rus3":
        emb = disnake.Embed(
            title="**Вы выбрали третий вариант**",
            description="**Выберите номер задания ниже**",
            color=0xafeeee)  
        await inter.response.send_message(embed = emb,
            components=[
                disnake.ui.Button(label="4-6", style=disnake.ButtonStyle.blurple, custom_id="zadrus9"),
                disnake.ui.Button(label="7-9", style=disnake.ButtonStyle.blurple, custom_id="zadrus10"),
                disnake.ui.Button(label="Текст", style=disnake.ButtonStyle.blurple, custom_id="zadrus11"),
                disnake.ui.Button(label="10-12", style=disnake.ButtonStyle.blurple, custom_id="zadrus12"),
            ]
        )


    if inter.component.custom_id == "rus4":
        emb = disnake.Embed(
            title="**Вы выбрали четвертый вариант**",
            description="**Выберите номер задания ниже**",
            color=0xafeeee) 
        await inter.response.send_message(embed = emb,
            components=[
                disnake.ui.Button(label="4-6", style=disnake.ButtonStyle.blurple, custom_id="zadrus13"),
                disnake.ui.Button(label="7-9", style=disnake.ButtonStyle.blurple, custom_id="zadrus14"),
                disnake.ui.Button(label="Текст", style=disnake.ButtonStyle.blurple, custom_id="zadrus15"),
                disnake.ui.Button(label="10-12", style=disnake.ButtonStyle.blurple, custom_id="zadrus16"),
            ]
        )

    if inter.component.custom_id == "rus5":
        emb = disnake.Embed(
            title="**Вы выбрали первый вариант**",
            description="**Выберите номер задания ниже**",
            color=0xafeeee)
        await inter.response.send_message(embed = emb,
            components=[
                disnake.ui.Button(label="4-6", style=disnake.ButtonStyle.blurple, custom_id="zadrus17"),
                disnake.ui.Button(label="7-9", style=disnake.ButtonStyle.blurple, custom_id="zadrus18"),
                disnake.ui.Button(label="Текст", style=disnake.ButtonStyle.blurple, custom_id="zadrus19"),
                disnake.ui.Button(label="10-12", style=disnake.ButtonStyle.blurple, custom_id="zadrus20"),
            ]
        ) 
#-------------------------------------------------------------Варианты история-------------------------------------------------------------

    if inter.component.custom_id == "histvariant1":
        emb = disnake.Embed(
            title="**Вы выбрали первый вариант**",
            description="**Выберите номер задания ниже**",
            color=0xafeeee)
        await inter.response.send_message(embed = emb,
            components=[
                disnake.ui.Button(label="1-3", style=disnake.ButtonStyle.blurple, custom_id="his1"),
                disnake.ui.Button(label="4-6", style=disnake.ButtonStyle.blurple, custom_id="his2"),
                disnake.ui.Button(label="7", style=disnake.ButtonStyle.blurple, custom_id="his3"),
                disnake.ui.Button(label="8", style=disnake.ButtonStyle.blurple, custom_id="his4"),
                disnake.ui.Button(label="9", style=disnake.ButtonStyle.blurple, custom_id="his5"),
                disnake.ui.Button(label="10-12", style=disnake.ButtonStyle.blurple, custom_id="his6"),
                disnake.ui.Button(label="13-14", style=disnake.ButtonStyle.blurple, custom_id="his7"),
                disnake.ui.Button(label="15-18", style=disnake.ButtonStyle.blurple, custom_id="his8"),
                disnake.ui.Button(label="19-22", style=disnake.ButtonStyle.blurple, custom_id="his9"),
                disnake.ui.Button(label="23-24", style=disnake.ButtonStyle.blurple, custom_id="his10"),
            ]
        ) 

#-------------------------------------------------------------Варианты общество-------------------------------------------------------------

    if inter.component.custom_id == "obshvariant1":
        emb = disnake.Embed(
            title="Вы выбрали первый вариант",
            description="**Выберите номер задания ниже**",
            color=0xafeeee)
        await inter.response.send_message(embed = emb,
            components=[
                disnake.ui.Button(label="1-4", style=disnake.ButtonStyle.blurple, custom_id="obsh1"),
                disnake.ui.Button(label="5-8", style=disnake.ButtonStyle.blurple, custom_id="obsh2"),
                disnake.ui.Button(label="9-11", style=disnake.ButtonStyle.blurple, custom_id="obsh3"),
                disnake.ui.Button(label="12-14", style=disnake.ButtonStyle.blurple, custom_id="obsh4"),
                disnake.ui.Button(label="15-17", style=disnake.ButtonStyle.blurple, custom_id="obsh5"),
                disnake.ui.Button(label="18-20", style=disnake.ButtonStyle.blurple, custom_id="obsh6"),

            ]
        )

#-------------------------------------------------------------Варианты информатика-------------------------------------------------------------

    if inter.component.custom_id == "infvar1":
        emb = disnake.Embed(
            title="**Вы выбрали первый вариант**",
            description="**Выберите номер задания ниже**",
            color=0xafeeee)
        await inter.response.send_message(embed = emb,
            components=[
                disnake.ui.Button(label="1-3", style=disnake.ButtonStyle.blurple, custom_id="inf11"),
                disnake.ui.Button(label="4-5", style=disnake.ButtonStyle.blurple, custom_id="inf12"),
                disnake.ui.Button(label="6", style=disnake.ButtonStyle.blurple, custom_id="inf13"),
                disnake.ui.Button(label="7-10", style=disnake.ButtonStyle.blurple, custom_id="inf14")
            ]
        )

    if inter.component.custom_id == "infvar2":
        emb = disnake.Embed(
            title="**Вы выбрали второй вариант**",
            description="**Выберите номер задания ниже**",
            color=0xafeeee)
        await inter.response.send_message(embed = emb,
            components=[
                disnake.ui.Button(label="1-3", style=disnake.ButtonStyle.blurple, custom_id="inf21"),
                disnake.ui.Button(label="4-5", style=disnake.ButtonStyle.blurple, custom_id="inf22"),
                disnake.ui.Button(label="6", style=disnake.ButtonStyle.blurple, custom_id="inf23"),
                disnake.ui.Button(label="7-10", style=disnake.ButtonStyle.blurple, custom_id="inf24")

            ]
        )

    if inter.component.custom_id == "infvar3":
        emb = disnake.Embed(
            title="**Вы выбрали третий вариант**",
            description="**Выберите номер задания ниже**",
            color=0xafeeee)
        await inter.response.send_message(embed = emb,
            components=[
                disnake.ui.Button(label="1-3", style=disnake.ButtonStyle.blurple, custom_id="inf31"),
                disnake.ui.Button(label="4-5", style=disnake.ButtonStyle.blurple, custom_id="inf32"),
                disnake.ui.Button(label="6", style=disnake.ButtonStyle.blurple, custom_id="inf33"),
                disnake.ui.Button(label="7-10", style=disnake.ButtonStyle.blurple, custom_id="inf34"),

            ]
        )

    if inter.component.custom_id == "infvar4":
        emb = disnake.Embed(
            title="**Вы выбрали четвертый вариант**",
            description="**Выберите номер задания ниже**",
            color=0xafeeee)
        await inter.response.send_message(embed = emb,
            components=[
                disnake.ui.Button(label="1-3", style=disnake.ButtonStyle.blurple, custom_id="inf41"),
                disnake.ui.Button(label="4-5", style=disnake.ButtonStyle.blurple, custom_id="inf42"),
                disnake.ui.Button(label="6", style=disnake.ButtonStyle.blurple, custom_id="inf43"),
                disnake.ui.Button(label="7-10", style=disnake.ButtonStyle.blurple, custom_id="inf44"),

            ]
        )

    if inter.component.custom_id == "infvar5":
        emb = disnake.Embed(
            title="**Вы выбрали пятый вариант**",
            description="**Выберите номер задания ниже**",
            color=0xafeeee)
        await inter.response.send_message(embed = emb,
            components=[
                disnake.ui.Button(label="1-3", style=disnake.ButtonStyle.blurple, custom_id="inf51"),
                disnake.ui.Button(label="4-5", style=disnake.ButtonStyle.blurple, custom_id="inf52"),
                disnake.ui.Button(label="6", style=disnake.ButtonStyle.blurple, custom_id="inf53"),
                disnake.ui.Button(label="7-10", style=disnake.ButtonStyle.blurple, custom_id="inf54"),

            ]
        )

#-------------------------------------------------------------Ответ по нажатию на кнопку 3-------------------------------------------------------------

@bot.listen("on_button_click")
async def chydasda(inter: disnake.MessageInteraction):

#-------------------------------------------------------------Русский задания с вариантов-------------------------------------------------------------

    if inter.component.custom_id not in ["zadrus1", "zadrus2", "zadrus3", "zadrus4", "zadrus5", "zadrus6", "zadrus7", "zadrus8", "zadrus9", "zadrus10", "zadrus11", "zadrus12", "zadrus13", "zadrus14", "zadrus15", "zadrus16", "zadrus17", "zadrus18", "zadrus19", "zadrus20", "his1", "his2", "his3", "his4", "his5", "his6", "his7", "his8", "his9", "his10", "obsh1", "obsh2", "obsh3", "obsh4", "obsh5", "obsh6" "inf11", "inf12", "inf13", "inf14", "inf21", "inf22", "inf23", "inf24", "inf31", "inf32", "inf33", "inf34", "inf41", "inf42", "inf43", "inf44", "inf51", "inf52", "inf53", "inf54"]:
        return 
     
    if inter.component.custom_id == "zadrus1":
        file = disnake.File("screenshots/rus11.png", filename="rus11.png")  
        await inter.response.send_message(file = file)
                                           
    if inter.component.custom_id == "zadrus2":
        file = disnake.File("screenshots/rus12.png", filename="rus12.png")   
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "zadrus3":
        file = disnake.File("screenshots/rus13.png", filename="rus13.png")             
        await inter.response.send_message(file = file)
                                          
    if inter.component.custom_id == "zadrus4":
        file = disnake.File("screenshots/rus14.png", filename="rus14.png") 
        await inter.response.send_message(file = file)   

#-------------------------------------------------------------Русский задания с вариантов-------------------------------------------------------------

    if inter.component.custom_id == "zadrus5":
        file = disnake.File("screenshots/rus21.png", filename="rus21.png")  
        await inter.response.send_message(file = file)
                                           
    if inter.component.custom_id == "zadrus6":
        file = disnake.File("screenshots/rus22.png", filename="rus22.png")   
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "zadrus7":
        file = disnake.File("screenshots/rus23.png", filename="rus23.png")             
        await inter.response.send_message(file = file)
                                          
    if inter.component.custom_id == "zadrus8":
        file = disnake.File("screenshots/rus24.png", filename="rus24.png") 
        await inter.response.send_message(file = file)

#-------------------------------------------------------------Русский задания с вариантов-------------------------------------------------------------

    if inter.component.custom_id == "zadrus9":
        file = disnake.File("screenshots/rus31.png", filename="rus31.png")  
        await inter.response.send_message(file = file)
                                           
    if inter.component.custom_id == "zadrus10":
        file = disnake.File("screenshots/rus32.png", filename="rus32.png")   
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "zadrus11":
        file = disnake.File("screenshots/rus33.png", filename="rus33.png")             
        await inter.response.send_message(file = file)
                                          
    if inter.component.custom_id == "zadrus12":
        file = disnake.File("screenshots/rus34.png", filename="rus34.png") 
        await inter.response.send_message(file = file)  

#-------------------------------------------------------------Русский задания с вариантов-------------------------------------------------------------

    if inter.component.custom_id == "zadrus13":
        file = disnake.File("screenshots/rus41.png", filename="rus41.png")  
        await inter.response.send_message(file = file)
                                           
    if inter.component.custom_id == "zadrus14":
        file = disnake.File("screenshots/rus42.png", filename="rus42.png")   
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "zadrus15":
        file = disnake.File("screenshots/rus43.png", filename="rus43.png")             
        await inter.response.send_message(file = file)
                                          
    if inter.component.custom_id == "zadrus16":
        file = disnake.File("screenshots/rus44.png", filename="rus44.png") 
        await inter.response.send_message(file = file)

#-------------------------------------------------------------Русский задания с вариантов-------------------------------------------------------------

    if inter.component.custom_id == "zadrus17":
        file = disnake.File("screenshots/rus51.png", filename="rus51.png")  
        await inter.response.send_message(file = file)
                                           
    if inter.component.custom_id == "zadrus18":
        file = disnake.File("screenshots/rus52.png", filename="rus52.png")   
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "zadrus19":
        file = disnake.File("screenshots/rus53.png", filename="rus53.png")             
        await inter.response.send_message(file = file)
                                          
    if inter.component.custom_id == "zadrus20":
        file = disnake.File("screenshots/rus54.png", filename="rus54.png") 
        await inter.response.send_message(file = file)  

#-------------------------------------------------------------История задания-------------------------------------------------------------

    if inter.component.custom_id == "his1":
        file = disnake.File("screenshots/hist1.png", filename="hist1.png") 
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "his2":
        file = disnake.File("screenshots/hist2.png", filename="hist2.png") 
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "his3":
        file = disnake.File("screenshots/hist3.png", filename="hist3.png") 
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "his4":
        file = disnake.File("screenshots/hist4.png", filename="hist4.png") 
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "his5":
        file = disnake.File("screenshots/hist5.png", filename="hist5.png") 
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "his6":
        file = disnake.File("screenshots/hist6.png", filename="hist6.png") 
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "his7":
        file = disnake.File("screenshots/hist7.png", filename="hist7.png") 
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "his8":
        file = disnake.File("screenshots/hist8.png", filename="hist8.png") 
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "his9":
        file = disnake.File("screenshots/hist9.png", filename="hist9.png") 
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "his10":
        file = disnake.File("screenshots/hist10.png", filename="hist10.png") 
        await inter.response.send_message(file = file)
        
#-------------------------------------------------------------Задания общество-------------------------------------------------------------

    if inter.component.custom_id == "obsh1":
        file = disnake.File("screenshots/obsh1.png", filename="obsh1.png") 
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "obsh2":
        file = disnake.File("screenshots/obsh2.png", filename="obsh2.png") 
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "obsh3":
        file = disnake.File("screenshots/obsh3.png", filename="obsh3.png") 
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "obsh4":
        file = disnake.File("screenshots/obsh4.png", filename="obsh4.png") 
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "obsh5":
        file = disnake.File("screenshots/obsh5.png", filename="obsh5.png") 
        await inter.response.send_message(file = file)
        
    if inter.component.custom_id == "obsh6":
        file = disnake.File("screenshots/obsh6.png", filename="obsh6.png") 
        await inter.response.send_message(file = file)

#-------------------------------------------------------------Задания информатика-------------------------------------------------------------

    if inter.component.custom_id == "inf11":
        file = disnake.File("screenshots/inf11.png", filename="inf11.png")  
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "inf12":
        file = disnake.File("screenshots/inf12.png", filename="inf12.png")  
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "inf13":
        file = disnake.File("screenshots/inf13.png", filename="inf13.png")  
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "inf14":
        file = disnake.File("screenshots/inf14.png", filename="inf14.png")  
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "inf21":
        file = disnake.File("screenshots/inf21.png", filename="inf21.png")  
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "inf22":
        file = disnake.File("screenshots/inf22.png", filename="inf22.png")  
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "inf23":
        file = disnake.File("screenshots/inf23.png", filename="inf23.png")  
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "inf24":
        file = disnake.File("screenshots/inf24.png", filename="inf24.png")  
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "inf31":
        file = disnake.File("screenshots/inf31.png", filename="inf31.png")  
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "inf32":
        file = disnake.File("screenshots/inf32.png", filename="inf32.png")  
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "inf33":
        file = disnake.File("screenshots/inf33.png", filename="inf33.png")  
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "inf34":
        file = disnake.File("screenshots/inf34.png", filename="inf34.png")  
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "inf41":
        file = disnake.File("screenshots/inf41.png", filename="inf41.png")  
        await inter.response.send_message(file = file)

    if inter.component.custom_id == "inf42":
        file = disnake.File("screenshots/inf42.png", filename="inf42.png")  
        await inter.response.send_message(file = file)   

    if inter.component.custom_id == "inf43":
        file = disnake.File("screenshots/inf43.png", filename="inf43.png")  
        await inter.response.send_message(file = file) 

    if inter.component.custom_id == "inf44":
        file = disnake.File("screenshots/inf44.png", filename="inf44.png")  
        await inter.response.send_message(file = file) 

    if inter.component.custom_id == "inf51":
        file = disnake.File("screenshots/inf51.png", filename="inf51.png")  
        await inter.response.send_message(file = file) 

    if inter.component.custom_id == "inf52":
        file = disnake.File("screenshots/inf52.png", filename="inf52.png")  
        await inter.response.send_message(file = file) 

    if inter.component.custom_id == "inf53":
        file = disnake.File("screenshots/inf53.png", filename="inf53.png")  
        await inter.response.send_message(file = file) 

    if inter.component.custom_id == "inf54":
        file = disnake.File("screenshots/inf54.png", filename="inf54.png")  
        await inter.response.send_message(file = file) 

#-------------------------------------------------------------   Отработка   -------------------------------------------------------------
        
@bot.slash_command()
async def hello(ctx):
    emb = disnake.Embed(
        title=f"**Рад познакомиться, {ctx.author.nick}!**",
        description="Желаю тебе удачи!",
        color=0xdde
        )
    file = disnake.File("screenshots/hello.png", filename='hello.png')
    await ctx.send(embed = emb)
    await ctx.send(file = file)

#-------------------------------------------------------------Запуск бота-------------------------------------------------------------

@bot.event
async def on_slash_command_error(ctx, error):
    await ctx.send(f'Произошла ошибка: {error}')

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'Произошла ошибка: {error}')

bot.run('nope :3')
