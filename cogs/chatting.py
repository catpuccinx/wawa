import discord
import random
from discord.ext import commands

class chatting(commands.Cog): 
    def __init__(self, client):
        self.client = client
# If you want to create a Event in a Cog you must have this decorator #
    @commands.Cog.listener()
    async def on_message(self, message): # self must be first argument that every function inside a class takes. #
        print("responses loaded!")
        message.content = message.content.lower()
        if message.author == self.client.user:
            return
        if self.client.user.mentioned_in(message):
            risposte = random.choice(risposte_ping)
            await message.channel.send(risposte)

        if message.content == "hello":
            rispostehello = random.choice(risposte_hello)
            await message.channel.send(rispostehello)
        elif message.content == "helo":
            rispostehello = random.choice(risposte_hello)
            await message.channel.send(rispostehello)
        elif message.content == "ciao":
            rispostehello = random.choice(risposte_hello)
            await message.channel.send(rispostehello)
        elif message.content == "halo":
            rispostehello = random.choice(risposte_hello)
            await message.channel.send(rispostehello)

        elif message.content == "ti voglio bene":
            tivogliobene = random.choice(ancheio)
            await message.channel.send(tivogliobene)

        elif "grazie" in message.content.lower():
            prego = random.choice(nonce)
            await message.channel.send(prego)        

        elif "???" in message.content.lower():
            await message.channel.send("🤷🏻‍♀️")        

        elif ":3" in message.content.lower():
            await message.chanel.send (":3")

        elif "stfu" in message.content.lower():
            await message.channel.send("thats rude bruh")

        elif "problem" in message.content.lower():
            await message.channel.send("not my problem. that's just not my problem~ 🤷🏻‍♀️")        

        elif message.content == "english or spanish?":
            spanish = random.choice(english)
            await message.channel.send(spanish)

        elif message.content == "the first one to move is gay":
            await message.channel.send("🧍‍♀️")

        elif message.content == "lol":
            await message.add_reaction("😂")
        
        elif message.content == "lmao":
            await message.add_reaction("🤣")

        elif message.content == "come stai?":
            rispostecomestai = random.choice(risposte_comestai)
            await message.channel.send(rispostecomestai)
        elif message.content == "come va?":
            rispostecomestai = random.choice(risposte_comestai)
            await message.channel.send(rispostecomestai)
        elif message.content == "tutto bene?":
            rispostecomestai = random.choice(risposte_comestai)
            await message.channel.send(rispostecomestai)

        elif message.content == "sto bene":
            stobene = random.choice(sto_bene)
            await message.channel.send(stobene)

        elif message.content == "sto male":
            stomale = random.choice(sto_male)
            await message.channel.send(stomale)

        elif message.content == "Mi fa piacere":
            grazie = random.choice(thankyou)
            await message.channel.send(grazie)
        elif message.content == "ne sono felice":
            grazie = random.choice(thankyou)
            await message.channel.send(grazie)

        elif message.content == "che fai?":
            hobbies = random.choice(attività)
            await message.channel.send(hobbies)

    # keywords, one respons #
        elif "duck" in message.content.lower():
            await message.channel.send("QUACK")

        elif "quack" in message.content.lower():
            await message.channel.send("QUACK")

        elif "eheh" in message.content.lower():
            await message.channel.send("'hehe' 'te nandayo? **SLAP**")

        elif "gay" in message.content.lower():
            await message.channel.send("molto da antony devo dire")

        elif "geheh" in message.content.lower():
            await message.channel.send("pretty snake!")

        elif "porco" in message.content.lower():
            await message.channel.send("Dio!")
        
        elif "hahaha" in message.content.lower():
            ridicazzo = random.choice(cazzoridi)
            await message.channel.send(ridicazzo)

        elif "<3" in message.content.lower():
            await message.channel.send("<3")

        elif "anto" in message.content.lower():
            await message.channel.send("è gay")

        elif "rin" in message.content.lower():
            await message.channel.send("è molto gay")

        elif "..." in message.content.lower():
            await message.channel.send("-cit edo")

        elif "hewwo" in message.content.lower():
            await message.channel.send("awooo!")

        elif "uwu" in message.content.lower():
            await message.channel.send("OWO")

        elif "xD" in message.content.lower():
            await message.channel.send("XD")

        elif "pog" in message.content.lower():
            await message.channel.send("guarda, nemmeno troppo")

        elif "rip" in message.content.lower():
            await message.channel.send("“O Dio, onnipotente ed eterno, Signore dei vivi e dei morti, pieno di misericordia verso tutte le tue creature, concedi il perdono e la pace a tutti i nostri fratelli defunti, perché immersi nella tua beatitudine ti lodino senza fine. Per Cristo nostro Signore. Amen. “")

        elif "twinning" in message.content.lower():
            await message.channel.send("va bene, però non come le torri eh")

        elif "bruh" in message.content.lower():
            await message.channel.send("bruh 🤪🤣😎👌🏽👌🏽🔥🔥")

        elif "fame" in message.content.lower():
            await message.channel.send("Hai fame? Ti consiglio questo video: https://www.youtube.com/watch?v=WprwPtvNp0o")

        elif "bastardo" in message.content.lower():
            await message.channel.send("Dio")

        elif ":D" in message.content.lower():
            await message.channel.send(":D")

        elif "puttana" in message.content.lower():
            await message.channel.send("la madonna")

        elif "no tu" in message.content.lower():
            await message.channel.send("no tu")

        elif "fottiti" in message.content.lower():
            await message.channel.send("no tu")

        elif "gasp" in message.content.lower():
            await message.channel.send("😮")

        elif "bella bro" in message.content.lower():
            await message.channel.send("ciao fra")

        elif "scusa" in message.content.lower():
            await message.channel.send("vai tra")

        elif "qualcosa" in message.content.lower():
            await message.channel.send("sto cazzo")

        elif "come butta?" in message.content.lower():
            await message.channel.send("tutto apposto fra, tu?")

        elif ":c" in message.content.lower():
            await message.channel.send("no sad allowed **slaps**")

        elif "devo studiare" in message.content.lower():
            await message.channel.send("sfigatx")

        elif "ao" in message.content.lower():
            await message.channel.send("ao??")

        elif "vabbè" in message.content.lower():
            await message.channel.send("nono, scusami non piangere")
  
        elif "ti amo" in message.content.lower():
            await message.channel.send("io ti amo <@327563231444992000>!")

        elif "wheeze" in message.content.lower():
            await message.channel.send("si ma respira amo")

        elif "sto cazzo" in message.content.lower():
            await message.channel.send("tua madre")
        
        elif "datti fuoco" in message.content.lower():
            await message.channel.send("modera le parole bro")

        elif "aiuto" in message.content.lower():
            await message.channel.send("118")

        else: # What should happen if none of the cases above were met.
            return

nonce = [
    "prego", 
    "non c'è di che",
]

ancheio = [
    "anche io", 
    "grazie",
    "👍🏻",
]

english = [
    "english", 
    "spanish",
]

Gorillaz = [
    "Gorillaz",
    "Murdoc",
    "2D",
    "2doc",
]

glace = [
    "test"
]

attività = [
    "sto imparando cose nuove, ma è un segreto!",
    "guardo dei video online...",
    "sto giocando a Ni No Kuni!",
]

thankyou = [
    "Grazie!"
]

sto_bene = [
    "mi fa piacere sentirlo", 
    "ne sono felice", 
    "oh, come mai?"
]

sto_male = [
    "mi dispiace tanto",
    "mi dispiace tanto, spero che si risolve presto",
    "oh, nel caso noi siamo qui!"
    "se possiamo fare qualcosa per aiutarti, non esitare a chiedere"
]

risposte_hello = [
    "Hello.", 
    "Hi.", 
    "Yo.", 
    "Ciao.", 
    "Sup.", 
    "Salut.", 
    "こんにちは.",
    "Grüß dich.",
    "Hola.",
    "Zdravo.",
    "γειά σου.",
    "Hallo.",
    "Hej.",
    "Olá!",
    "Ahoj.",
    "Namasté.",
    "Привет.",
    "Xin chào.",
    "你好.",
    "رحبا."
    ]
# ____________________________________________

cazzoridi = [
    "cazzo ridi?", 
    "che cosa hai da ridere >:c", 
    "perchè ridi? non ho capito..."
]

# ____________________________________________
risposte_comestai = [ 
    "Fatti i cazzi tua.", 
    "Non è giornata.", 
    "Tutto bene, tu?", 
    "Non troppo bene", 
    "Si va avanti", 
    "Molto bene!", 
    "Va tutto bene", 
    "Una meraviglia.",
    "Benissimo, mai stata meglio!",
    "Da Dio!",
    "Alla grande!",
    "Niente male", 
    "Non c'è male",
    "Non mi posso lamentare", 
    "Non mi lamento", 
    "Tutto ok",
    "Sto così e così",
    "Insomma",
    "Non molto bene",  
    "Sono stata meglio",
    "Ho visto giorni migliori",
    "Da cani",
    "da schifo",
    "uno schifo", 
    "voglio morire",
    "Niente di speciale",
    "Niente di che",
    "Il solito",
    "sempre le stesse cose",
    "tutto uguale" ]

risposte_ping = [
"...ao?", 
"Hai dimenticato i comandi..?",
"uhm, credo che hai sbagliato.",
"sono occupata adesso.", 
"aspetta...", 
"no", 
"ciao glace", 
"ciao edo", 
"come stai?",
"non direi proprio..", 
"ti voglio tanto bene snake!", 
"hai rotto il cazzo", 
"dimmi", 
"okay 👍🏻",
"sono fiera di <@327563231444992000>", #glace
"sono fiera di <@252736234982604800>", #edo
"sono fiera di <@957656313666613258>", #rin
"sono fiera di <@731717697301381178>", #catra
"mammt.",
]

async def setup(client): 
    await client.add_cog(chatting(client))