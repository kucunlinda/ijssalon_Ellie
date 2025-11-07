from algemene_functies import mijn_functie_2


def aanbieding_1(smaak, prijs, korting):
    korting = prijs - prijs*korting
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro.")
aanbieding_1("aardbei", 4, 0.1)
def inkomsten_totaal(inkomsten):
    totaal = sum(inkomsten)
    bedrag = totaal * 0.09
    tekst = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    return (tekst)
print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345]))
def laag_en_hoog(mijn_lijst):
    Extrema = [max(mijn_lijst),min(mijn_lijst)]
    return Extrema
laag_en_hoog([220, 430, 125, 160, 205, 90, 345])
def gemiddelde(mijn_lijst):
    gemiddelde = sum(mijn_lijst) / len(mijn_lijst)
    tekst = f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
    return tekst
print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
print(meervoudig([220, 430, 125, 160, 205, 90, 345]))
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print(combinatie([220, 430, 125, 160, 205, 90, 345]))