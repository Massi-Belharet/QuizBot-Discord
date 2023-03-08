
"""
projet fait par:

Massinissa BELHARET
Mamadou Atigou BAH
HACHICHA Soumaya

"""




import discord
import os
import asyncio
from dotenv import load_dotenv

intents = discord.Intents.all()
intents.messages = True
intents.members = True
intents.message_content = True
intents.typing = True
client = discord.Client(intents=intents)


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')






@client.event
async def on_ready():
    print("Le bot est prêt !")


@client.event
async def on_member_join(member):
    general_channel = client.get_channel(1044971841380425790)
    await general_channel.send("Bienvenue sur le serveur ! ")


quiz = False
aide = False
point = 0
qst = 0
stp=0
secondint = 0

@client.event
async def on_message(message):
    global quiz
    global point
    global qst
    global aide
    global stp
    global secondint

    if message.author == client.user:
        return

    msg = message.content.lower()


    # présentation du jeu:
    if "!hello" in msg:
        if stp == 0:
            await message.channel.send("https://media.giphy.com/media/qMcqXbEg8obDy/giphy.gif")
            await message.channel.send("ça vous dit d'aller à la recherche d'un trésor égaré dans le monde depuis des années,ce trésor en question appartient à des pirates qui l'ont caché dans une ile juste avant de périr dans un naufrage causé par une Tempête !")
            await message.channel.send("tapez **oui** Pour Commencer l'adventure!! ")
            stp = stp + 1
    elif "oui" in msg:
        if stp == 1:
            await message.channel.send("le trésor se trouve dans ce catacombe")
            await message.channel.send("https://www.walksinsiderome.com/fr/wp-content/uploads/2020/05/1.jpg")
            await message.channel.send("Attention :warning:  malheureusement les pirates avaient installés des pièges mortel dans tout le catacombe histoire de protéger leurs trésor, ainsi pour les désactivés vous dévez repondre à une serie de questions durant **5 minutes**, chaque bonne reponse désactive un piège et il vous faut avoir au minimum **70 Points** pour désactiver tout les pièges.")
            await message.channel.send("À chaque fois vous utilisez un indice,vous perdrez six points.")
            await message.channel.send("Avant de commencer, lancez le temps avec  **!timer** et puis tappez **!quiz** pour lancer le quiz.")
            stp = stp + 1
            return
    # commande pour lancer le temps:
    if msg == "!timer" and stp ==2:
        secondes = 300
        secondint = int(secondes)
        msg_2 = await message.channel.send(f"Timer: {secondes}")
        stp = stp + 1
        while True:
            secondint -= 1
            if secondint == 0:
                await msg_2.edit(content="Ended!")
                quiz = False
                aide = False
                stp = 0
                qst = 0
                point = 0
                break
            await msg_2.edit(content=f"**Timer**: {secondint} Secondes")
            await asyncio.sleep(1)
        await message.channel.send(f"{message.author.mention}, le Temps est Terminer!")
        await message.channel.send("Pour relancer le jeu à nouveau, utilisez la commande **!hello**")
    # commande pour lancer le quiz:
    if msg == "!quiz" and quiz == False:
        if stp==3 and qst==0:
            await message.channel.send("🚀Ok, voici un petit quiz pour toi(Utilisez la commande **!quiz end** pour terminer le quiz)")
            await message.channel.send("Pour voir ton score, utilisez la commande **!point**")
            await message.channel.send("=====================================")
            # poser la 1ére question:
            await message.channel.send("💬 1- Quelle est la console de jeu la plus vendue de tous les temps ?")
            await message.channel.send("------------------------------------")
            await message.channel.send("**Réponse 1:**  PS2 \n **Réponse 2:**  Nintendo DS \n **Réponse 3:**  Game Boy")
            qst = qst + 1
            aide = False
            quiz = True
            return
    # proposer un indice si l'utilisateur a inséré une mauvaise réponse:
    elif (msg == "nintendo ds" or msg == "game boy") and quiz == True and aide == False:
        if qst == 1 and msg != "!point" and msg != "!quiz end":
            await message.channel.send("Mauvaise Réponse")
            await message.channel.send("si vous voulez avoir un indice, tapez **indice 1**")
    # lancement de l'indice de la 1ére question:
    elif msg == "indice 1" and quiz == True and aide == False:
        aide = True
        if aide == True and qst == 1:
            await message.channel.send("la console est faite par une société japonaise en 2000.")
            aide = False
            point = point + - 6
    # poser la 2éme question si l'utilisateur a inséré la bonne réponse:
    if msg == "ps2" and quiz == True:
        if qst == 1:
            point = point + 10
            await message.channel.send("**Bonne Réponse👍!**")
            await message.channel.send("https://media.giphy.com/media/73tSz7Zzz68FrK66wh/giphy.gif")
            await message.channel.send("=============================")
            await message.channel.send("💬 2- Quelle partie est le cerveau de l'ordinateur ?")
            await message.channel.send("------------------------------------")
            await message.channel.send("**Réponse 1:**  RAM \n **Réponse 2:**  Processeur \n **Réponse 3:**  Disque Dur")
            qst = qst + 1
            aide = False
    # proposer un indice si l'utilisateur a inséré une mauvaise réponse:
    elif (msg == "ram" or msg == "disque dur") and quiz == True and aide == False:
        if qst == 2 and msg != "!point" and msg != "!quiz end":
            await message.channel.send("Mauvaise Réponse")
            await message.channel.send("si vous voulez avoir un indice, tapez **indice 2**")
    # lancement de l'indice de la 2éme question:
    elif msg == "indice 2" and quiz == True and aide == False:
        aide = True
        if aide == True and qst == 2:
            await message.channel.send("C'est un composant présent dans de nombreux dispositifs électroniques qui exécute les instructions machine des programmes informatiques.")
            aide = False
            point = point + - 6
    # poser la 3éme question si l'utilisateur a inséré la bonne réponse:
    if msg =="processeur" and quiz == True:
        if qst == 2:
            point = point + 10
            await message.channel.send("**Bonne Réponse👍!**")
            await message.channel.send("http://www.hi-tech-news.fr/wp-content/uploads/2021/01/Processeur-0.jpg")
            await message.channel.send("=============================")
            await message.channel.send("💬 3- Quel est le jeu vidéo le plus vendu de tous les temps ?")
            await message.channel.send("------------------------------------")
            await message.channel.send("**Réponse 1:**  GTA V \n **Réponse 2:**  PUBG \n **Réponse 3:**  Minecraft")
            qst = qst + 1
            aide = False
    ##########################
    elif (msg == "gta v" or msg == "pubg") and quiz == True and aide == False:
        if qst == 3 and msg != "!point" and msg != "!quiz end":
            await message.channel.send("Mauvaise Réponse")
            await message.channel.send("si vous voulez avoir un indice, tapez **indice 3**")
    ##########################
    elif msg == "indice 3" and quiz == True and aide == False:
        aide = True
        if aide == True and qst == 3:
            await message.channel.send("le jeu video permet de construire divers bâtiments à l'aide de cubes dans un monde en 3D.")
            aide = False
            point = point + - 6
    # poser la 4éme question si l'utilisateur a inséré la bonne réponse:
    if msg == "minecraft" and quiz == True:
        if qst == 3:
            point = point + 10
            await message.channel.send("**Bonne Réponse👍!**")
            await message.channel.send("https://media.giphy.com/media/BljlTfIli47x6/giphy.gif")
            await message.channel.send("=============================")
            await message.channel.send("💬 4- Quel est le langage de balisage conçu pour représenter les pages web ?")
            await message.channel.send("------------------------------------")
            await message.channel.send("**Réponse 1:**  HTML \n **Réponse 2:**  CSS \n **Réponse 3:**  Javascript")
            qst = qst + 1
            aide = False
    ##########################
    elif (msg == "css" or msg == "javascript") and quiz == True and aide == False:
        if qst == 4 and msg != "!point" and msg != "!quiz end":
            await message.channel.send("Mauvaise Réponse")
            await message.channel.send("si vous voulez avoir un indice, tapez **indice 4**")
    ##########################
    elif msg == "indice 4" and quiz == True and aide == False:
        aide = True
        if aide == True and qst == 4:
            await message.channel.send("Ce langage permet d’écrire de l’hypertexte, et de structurer sémantiquement une page web.")
            aide = False
            point = point + - 6
    # poser la 5éme question si l'utilisateur a inséré la bonne réponse:
    if msg =="html" and quiz == True:
        if qst == 4:
            point = point + 10
            await message.channel.send("**Bonne Réponse👍!**")
            await message.channel.send("https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif")
            await message.channel.send("=============================")
            await message.channel.send("💬 5- Quelle est la fonction qui permet de choisir de façon aleatoire un nombre en python ?")
            await message.channel.send("------------------------------------")
            await message.channel.send("**Réponse 1:**  index \n **Réponse 2:**  random \n **Réponse 3:**  randint")
            qst = qst + 1
            aide = False
    ##########################
    elif (msg == "count" or msg == "random") and quiz == True and aide == False:
        if qst == 5 and msg != "!point" and msg != "!quiz end":
            await message.channel.send("Mauvaise Réponse")
            await message.channel.send("si vous voulez avoir un indice, tapez **indice 5**")
    ##########################
    elif msg == "indice 5" and quiz == True and aide == False:
        aide = True
        if aide == True and qst == 5:
            await message.channel.send("cette fonction se trouve dans le module random, et elle simule le tirage au hasard d'un entier entre deux entiers.")
            aide = False
            point = point + - 6
    # poser la 6éme question si l'utilisateur a inséré la bonne réponse:
    if msg == "randint" and quiz == True:
        if qst == 5:
            point = point + 10
            await message.channel.send("**Bonne Réponse👍!**")
            await message.channel.send("https://th.bing.com/th/id/R.def6620ad12ffabeb33065a9f87f434c?rik=%2b8CkSCWrXT5cnQ&pid=ImgRaw&r=0")
            await message.channel.send("=============================")
            await message.channel.send("💬 6- Qui est le createur de système d’exploitation 'Windows' ?")
            await message.channel.send("------------------------------------")
            await message.channel.send("**Réponse 1:**  Bill Gates \n **Réponse 2:**  Jeff Bezos \n **Réponse 3:**  Mark Zuckerberg")
            qst = qst + 1
            aide = False
    ##########################
    elif (msg == "jeff Bezos" or msg == "mark zuckerberg") and quiz == True and aide == False:
        if qst == 6 and msg != "!point" and msg != "!quiz end":
            await message.channel.send("Mauvaise Réponse")
            await message.channel.send("si vous voulez avoir un indice, tapez **indice 6**")
    ##########################
    elif msg == "indice 6" and quiz == True and aide == False:
        aide = True
        if aide == True and qst == 6:
            await message.channel.send("Il est connu pour être le cofondateur de Microsoft en 1975 et son principal actionnaire jusqu’en 2014.")
            aide = False
            point = point + - 6
    # poser la 7éme question si l'utilisateur a inséré la bonne réponse:
    if msg == "bill gates" and quiz == True:
        if qst == 6:
            point = point + 10
            await message.channel.send("**Bonne Réponse👍!**")
            await message.channel.send("https://media.giphy.com/media/l0K4mbH4lKBhAPFU4/giphy.gif")
            await message.channel.send("=============================")
            await message.channel.send("💬 7-A qui appartient Tesla ?")
            await message.channel.send("------------------------------------")
            await message.channel.send("**Réponse 1:**  Steve Jobs \n **Réponse 2:**  Elon musk \n **Réponse 3:**  Jeff Bezos")
            qst = qst + 1
            aide = False
    ##########################
    elif (msg == "jeff Bezos" or msg == "steve jobs") and quiz == True and aide == False:
        if qst == 7 and msg != "!point" and msg != "!quiz end":
            await message.channel.send("Mauvaise Réponse")
            await message.channel.send("si vous voulez avoir un indice, tapez **indice 7**")
    ##########################
    elif msg == "indice 7" and quiz == True and aide == False:
        aide = True
        if aide == True and qst == 7:
            await message.channel.send("C'est le président-directeur général de la société astronautique SpaceX,e t l'homme le plus riche du monde actuellement.")
            aide = False
            point = point + - 6
    # poser la 8ème question si l'utilisateur a inséré la bonne réponse:
    if msg == "elon musk" and quiz == True:
        if qst == 7:
            point = point + 10
            await message.channel.send("**Bonne Réponse👍!**")
            await message.channel.send("https://media.giphy.com/media/duKV1YBPhDtd9efnrR/giphy.gif")
            await message.channel.send("=============================")
            await message.channel.send("💬 8-C'est quoi le jeu de l'année 2020 ?")
            await message.channel.send("------------------------------------")
            await message.channel.send("**Réponse 1:**  The Last of Us Part 2 \n **Réponse 2:**  League of Legends \n **Réponse 3:**  Fortnite")
            qst = qst + 1
            aide = False
    ##########################
    elif (msg == "league of legends" or msg == "fortnite") and quiz == True and aide == False:
        if qst==8 and msg != "!point" and msg !="quiz end":
           await message.channel.send("mauvaise reponse")
           await message.channel.send("si vous voulez avoir un indice taper **indice 8**")
    elif  msg == "indice 8" and quiz == True and aide == False:
        aide = True
        if aide == True and qst == 8 :
          await message.channel.send("C'est un jeu vidéo d’action-aventure, Développé par Naughty Dog et édité par Sony.")
          aide = False
          point = point + - 6
   # poser la 9ème question si l'utilisateur a inséré la bonne réponse:
    if msg == "the last of us part 2" and quiz == True:
      if qst ==8 :
         point = point + 10
         await message.channel.send("**Bonne Réponse👍!**")
         await message.channel.send("https://media.giphy.com/media/UrsOTbx6xh20IXChwR/giphy.gif")
         await message.channel.send("=============================")
         await message.channel.send("💬 9-Quelle entreprise de jeux vidéo publie la série 'Far Cry' ?")
         await message.channel.send("------------------------------------")
         await message.channel.send("**Réponse 1:**  Activision \n **Réponse 2:**  Epic Games \n **Réponse 3:**  Ubisoft")
         qst = qst + 1
         aide = False
     ##########################
    elif (msg == "epic games" or msg == "activision") and quiz == True and aide == False:
        if qst == 9 and msg != "!point" and msg != "quiz end":
          await message.channel.send("mauvaise reponse ")
          await message.channel.send("si vous voulez avoir un indice tapez **indice 9**")
    elif msg == "indice 9"  and quiz == True and aide == False:
        aide = True
        if aide == True and qst == 9 :
            await message.channel.send("C'est une entreprise française de développement de jeux vidéo, elle a développée aussi la serie 'Assassin's Creed'.")
            aide = False
            point = point + - 6
      # poser la 10ème question si l'utilisateur a inséré la bonne réponse:
    if msg == "ubisoft" and quiz == True :
       if qst ==9:
         point = point + 10
         await message.channel.send("**Bonne Réponse👍!**")
         await message.channel.send("https://media.tenor.com/8LjYPixPIjwAAAAC/ubisoft-ubisoft-forward.gif")
         await message.channel.send("💬 10- Qui a gagné la coupe du monde 2002 ?")
         await message.channel.send("------------------------------------")
         await message.channel.send("**Réponse 1:**  France \n **Réponse 2:**  Brésil \n **Réponse 3:**  Espagne")
         qst = qst + 1
         aide = False
    ##########################
    elif (msg == "france" or msg == "espagne") and quiz == True and aide == False:
        if qst == 10 and msg != "!point" and msg != "quiz end":
          await message.channel.send("mauvaise reponse")
          await message.channel.send("si vous voulez avoir un indice tapez **indice 10**")
    elif msg == "indice 10"  and quiz == True:
        aide = True
        if aide == True and qst == 10 :
          await message.channel.send("la langue officielle de ce pays est le portugais ")
          aide = False
          point = point + - 6
    if msg == "brésil" and quiz == True:
       if qst == 10:
         point = point + 10
         await message.channel.send("**Bonne Réponse👍!**")
         await message.channel.send("https://media.giphy.com/media/kgsqn9gCVAQ3YM3C2f/giphy.gif")
         aide = False
         quiz = False
    # afficher le score total après la fin de quiz:
    if qst == 10 and quiz == False:
        await message.channel.send(f"Vous avez: ** {point}/100** Points")
        await message.channel.send("=============================")
        if point >=70:
            await message.channel.send("Vous avez terminé le quiz avec succès ✅ ")
            await message.channel.send("vous avez reussi, vous avez désactiver tout les pièges! felicitation !")
            await message.channel.send("voici votre trésor vous le meriter")
            await message.channel.send("https://th.bing.com/th/id/R.6404ce72cb03d73eb0307e5fbcf92e52?rik=GogCPyi%2fs9uKJA&pid=ImgRaw&r=0&sres=1&sresct=1")
            await message.channel.send("Merci d'avoir assisté à cette aventure, Si jamais vous voulez recommencé cette aventure veuillez taper la commande **!hello** ")
        else:
            await message.channel.send("le quiz est terminé !")
            await message.channel.send("Vous avez echoué à trouver le trésor ❌")
            await message.channel.send("Merci d'avoir assisté à cette aventure, Si jamais vous voulez recommencé cette aventure veuillez taper la commande **!hello** ")
        qst = 0
        point = 0
        stp = 0
        secondint = 0
    # commande pour afficher le score:
    if "!point" in msg and quiz == True:
        if point <0:
            await message.channel.send(f"Actuellement votre score est:** 0** Pts")
        else:
            await message.channel.send(f"Actuellement votre score est:** {point}** Pts")
    # commande pour arrêter le quiz à tout moment:
    if msg == "!quiz end" and quiz==True and secondint != 0:
        quiz=False
        aide=False
        stp=0
        qst=0
        point=0
        secondint = 0
        await message.channel.send("Au revoir 👋")
        await message.channel.send("Pour relancer le jeu à nouveau, utilisez la commande **!hello**")


client.run("DISCORD_TOKEN")