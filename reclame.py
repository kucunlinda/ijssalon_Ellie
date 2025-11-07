def aanbieding_1(smaak, prijs, korting):
    korting = prijs - prijs*korting
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro.")
aanbieding_1("aardbei", 4, 0.1)
def inkomsten_totaal(inkomsten):
    totaal = sum(inkomsten)
    bedrag = totaal * 0.09
    tekst = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    return print(tekst)
inkomsten_totaal([220, 430, 125, 160, 205, 90, 345])
def laag_en_hoog(mijn_lijst):
    Extrema = [max(mijn_lijst),min(mijn_lijst)]
    return print(Extrema)
laag_en_hoog([220, 430, 125, 160, 205, 90, 345])
def gemiddelde(mijn_lijst):
    gemiddelde = sum(mijn_lijst) / len(mijn_lijst)
    tekst = f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
    return print(tekst)
gemiddelde([220, 430, 125, 160, 205, 90, 345])
def meervoudig(invoer_lijst):
    return print(laag_en_hoog(invoer_lijst))
meervoudig([220, 430, 125, 160, 205, 90, 345])
