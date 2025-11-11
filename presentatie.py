def presenteer(mijn_dict):
    for k, v in mijn_dict.items():
        print (k, ":" , v)
    print (20 * "=")
    tot = sum(mijn_dict.values())
    print("totaal", ":", tot, "euro")

presenteer({ 
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
})