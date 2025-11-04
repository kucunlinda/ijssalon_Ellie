prijzen = { 
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
aanbieding = round(prijzen["aardbei"]* 0.8, 1)
#print(aanbieding)
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"
reclame_tekst3 = (reclame_tekst.upper())
reclame_tekst4 = reclame_tekst3.split()
#print(reclame_tekst4)
for el in reclame_tekst4:
    if len(el) > 5:
        print(el.upper()) 
    else:
     print(el.lower())