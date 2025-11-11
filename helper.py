def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()
decoreer(tekst="")

def fooi_pp(b, p):
    #if b == 0:
    #    return "Het bedrag per persoon is 0 ."

    #else:

    bedrag_pp = b/p
    return (f"Het bedrag per persoon is {bedrag_pp}.")
'''
# Vraag eerst om b
b = int(input("Welk bedrag zit er in de fooienpot? "))

# Vraag alleen om p als b niet 0 is
if b != 0:
    p = int(input("Over hoeveel mensen moet de pot verdeeld worden? "))
    print(fooi_pp(b, p))

else:
    print(fooi_pp(b, 1))  # p=1 of gewoon geen verdeling nodig


def fooi_pp(bedrag, personen):
    try:
        bedrag_pp = bedrag / personen
    except Exception:
        bedrag_pp = "??"
    return f"Het bedrag per persoon is {bedrag_pp} euro"

b = int(input("Welk bedrag zit er in de fooienpot? "))
p = int(input("Over hoeveel mensen moet de pot verdeeld worden? "))
print(fooi_pp(b, p))
a = 10
def dubbel():
    global a
    a = 2 * a
    return a
print(dubbel())
try:
    print(10/0)
except:
    print("0/10")
'''
def onderstreep(tekst=""):
    uit = []
    teken = len(tekst) * "="
    uit.append(tekst)
    uit.append(teken)
    return uit
def som(tel_op):
    totaal = sum(tel_op.values())
    return {"totaal":totaal}
