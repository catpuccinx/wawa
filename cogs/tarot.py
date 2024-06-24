import random
from discord.ext import commands

class Divinazione(commands.Cog):

    @commands.Cog.listener()
    async def on_ready(self):
        print("tarots loaded!")

    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def consiglio(self, ctx, *, question):
        arcani_maggiori = [
        "Il Matto (dritto) : Segui la voce del tuo core. Cerca di ragionare. ",
        "Il Matto (rovescio): Non riesci a vincere la tua paura. Non è tutto perduto",
        "Il Bagatto (dritto): Approfitta delle tue doti naturali",
        "Il Bagatto (rovescio): Sei passivo. Dipendi troppo dagli altri.",
        "La Papessa (dritto): Sviluppa la tua intuizione e avrai successo.",
        "La Papessa (rovescio): Ritrova te stesso.",
        "L'Imperatrice (dritto): Una persona amica ti aiuta.",
        "L'Imperatrice (rovescio): Cerca uno scopo.",
        "L'Imperatore (dritto): Confida nella tua energia e rischia. Ottimi risultati.",
        "L'Imperatore (rovescio): Sei immaturo. Ormai è tempo di cambiare.",
        "Il Papa (dritto): Cercati un maestro. Fatti trovare da un maestro.",
        "Il Papa (rovescio): Sei intollerante. Non sei solo.",
        "Gli Amanti (dritto): Una nuova storia d'amore in arrivo.",
        "Gli Amanti (rovescio): Separazione dubbiosa.",
        "Il Carro (dritto): Se sei pronto per il grande passo, vai.",
        "Il Carro (rovescio): Fermati, stai andando verso l'abisso.",
        "La Giustizia (dritto): Il giusto viene sempre ripagato.",
        "La Giustizia (rovescio): Se non cambi non vincerai mai.",
        "L'Eremita (dritto): Rifletti su ciò che stai facendo. Guarda dove vai.",
        "L'Eremita (rovescio): Hai perso la strada. Forse sei ancora in tempo.",
        "La Ruota della Fortuna (dirtto): Sfrutta il momento favorevole, vai avanti.",
        "La Ruota della Fortuna (rovescio): Non hai uno scopo nè una meta. Inventati qualcosa.",
        "La Forza (dritto): Vinci il tuo dolore e la tua rabbia. Puoi farcela.",
        "La Forza (rovescio): Cambia la tua vita o non ce la farai mai.",
        "L'Appeso (dritto): Abbandonati ai tuoi desideri ma non lasciarti soffocare da essi.",
        "L'Appeso (rovescio): È una fatica inutile se non ci metti più convinzione.",
        "La Morte (dritto): Butta via ciò che ti impedisce di vivere, reagisci.",
        "La Morte (rovescio): Sei in serio pericolo. La soluazione esiste, trovala.",
        "La Temperanza (dritto): Guarda dentro di te.",
        "La Temperanza (rosvescio): Stai sprecando la tua vita. Trova le energie necessarie.",
        "Il Diavolo (dritto): Sviluppa ogni desiderio più recondito ma non esagerare.",
        "Il Diavolo (rovescio): Rischia di più se vuoi uscire dalla tua depressione.",
        "La Torre (dritto): Lascia che tutto cada, solo così potrai ricominciare.",
        "La Torre (rovescio): Hai rivoltato la tua vita.",
        "Le Stelle (dritto): È il momento di realizzare le tue idee, prove."
        "Le Stelle (rovescio): Sei sfortunato ma hai ancora una possibilità.",
        "La Luna (dritto): Analizza i tuoi sogni. Ti forniranno soluzioni.",
        "La Luna (rovescio): Parlano di te, hanno ragione? Analizzati.",
        "Il Sole (dritto): I tuoi progetti si realizzano. Attendi fiducioso.",
        "Il Sole (rovescio): Sei cieco, ma puoi rimediare. Guardati intorno. Il sole c'è anche quando è coperto.",
        "Il Giudizio (dritto): Liberati dalle tue inibizioni. Puoi ancora farcela.",
        "Il Giudizio (rovescio): Ti lascierà mai puoi ancora convincerla.",
        "Il Mondo (dritto): Non ti fermare, puoi realizzare tutto quello che vuoi.",
        "Il Mondo (rovescio): Stai perdendo tutto cioè che possiedi, rifletti.",
        ]

        arcani_siono = [
        "Il Matto: Si, vai buttati!",
        "Il Bagatto: Si.",
        "La Papessa: Si, ma usa la testa.",
        "L'Imperatrice: Si ma convinto eh.",
        "L'Imperatore: Si, devi. Non hai scelta.",
        "Il Papa: Forse si, con la giusta guida.",
        "Gli Amanti: Forse.",
        "Il Carro: Forse, però è una decisione troppo affrettata, rifletti.",
        "La Giustizia: Rifletti più se è giusto o meno.",
        "L'Eremita: No.",
        "La Ruota della Fortuna: Aspetta e spera.",
        "La Forza: Si.",
        "L'Appeso: Si, non puoi fare altro.",
        "La Morte: No, è il momento di cambiare.",
        "La Temperanza: Si, ci sei quasi.",
        "Il Diavolo: No, prima smetti e meglio è.",
        "La Torre: Assolutamente No!",
        "Le Stelle: Si, hai una opportunità.",
        "La Luna: No, troppe cose che non sai.",
        "Il Sole: Assolutamente Si!",
        "Il Giudizio: No.",
        "Il Mondo: Si.",
        ]

        await ctx.send(f"{ctx.author.mention}, i tarocchi ti consigliano: {random.choice(arcani_maggiori)} La risposta è: {random.choice(arcani_siono)}")

async def setup(client): 
    await client.add_cog(Divinazione(client))