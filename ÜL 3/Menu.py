from laul import Laul
from Album import Album
from Artist import Artist

# Albumite nimekirja lugemine ja väljastamine
"""
def valjasta_koik():
    with open("albumid.txt", encoding="utf-8") as file:
        previous_album = ""
        for line in file:
            artist, albumi_p, aasta, laulu_p = line.split("\t")
            if albumi_p != previous_album:
                print("\n" + albumi_p, "(" + aasta + "):")
            else:
                pass
            print(artist, "-", laulu_p, end="")
            previous_album = albumi_p
    return
"""
# valjasta_koik()


#Üldine otsing (otsitakse tulemusi "l_artistid", "l_albumid" ja "l_laulud" listidest ja väljastatakse tulemused konsooli
def ul_otsing(p_otsitav):
    """

     :param p_otsitav_märksõna:
     :return:

    tulemused[0] (obj) - Kõik "Laul" objektid
    tulemused[1] (obj) - Kõik "Album" objektid
    tulemused[2] (obj) - Kõik "Artist" objektid

    """
    tulemused = [[], [], []]

    # Otsimine
    p_otsitav = str(p_otsitav).lower()
    for e_laul in l_laulud:
        if p_otsitav in e_laul.nimi.lower():
            tulemused[0].append(e_laul)
        else:
            pass
    for e_album in l_albumid:
        if p_otsitav in e_album.nimi.lower() or p_otsitav in str(e_album.aasta):
            tulemused[1].append(e_album)
        else:
            pass
    for e_artist in l_artistid:
        if p_otsitav in e_artist.nimi.lower():
             tulemused[2].append(e_artist)
        else:
             pass

    #Väljastamine konsooli
    for e_grupp in tulemused:
        try:
            if type(e_grupp[0]) == Laul:
                print("[Laulud]:")
                for nr, e_laul in enumerate(e_grupp, 1):
                    e_laul.valjasta(nr)
                print() # Et paremini eraldada gruppe

            elif type(e_grupp[0]) == Album:
                print("[Albumid]:")
                for nr, e_album in enumerate(e_grupp, 1):
                    e_album.valjasta(nr)
                print() # Et paremin eraldada gruppe

            elif type(e_grupp[0]) == Artist:
                print("[Artistid]:")
                for nr, e_artist in enumerate(e_grupp, 1):
                    e_artist.valjasta(nr)
        except IndexError:  # Kui ei leitud otsingu ajal (näitkes) ühtegi laulu siis läheb järgmise gruppi juurde
            continue

# Kategooriline otsing (otsib tulemusi ainult kindlast listist ("l_artistid", "l_albumid" või "l_laulud"))
def kat_otsing(p_list, p_otsitav):
    listid = [l_artistid, l_albumid, l_laulud]
    jrk = 1
    for thing in listid[int(p_list)-1]:
        try:
            if p_otsitav in str(thing.aasta):
                thing.valjasta(jrk)
                jrk += 1
            else:
                raise AttributeError("Otsitav pole number")
        except AttributeError:
            if p_otsitav.lower() in thing.nimi.lower():
                thing.valjasta(jrk)
                jrk += 1
            else:
                pass


# Artist, Album & Laul objektide tegemine ja kindlatesse listidesse lisamine
with open("albumid.txt", encoding="utf-8") as file:
    l_artistid = []  # (obj) List kus on kõik "Artist" objektid
    l_albumid = []  # (obj) List kus on kõik "Album" objektid
    l_laulud = []  # (obj) List kus on kõik "Laul" objektid

    l_art_nimed = []  # (str) List kus on kõikide "Artist" objektide nimed sees

    for line in file:
        artist, albumi_pealkiri, ilmumis_aasta, laulu_pealkiri = line.strip("\n").split("\t")

        if artist not in l_art_nimed:
            l_artistid.append(Artist(artist))
            l_art_nimed.append(artist)
            l_albumid.append(Album(albumi_pealkiri, ilmumis_aasta, l_artistid[-1]))
            l_artistid[-1].lisa_album(l_albumid[-1])

        elif l_artistid[l_art_nimed.index(artist)].albumid[-1].nimi != albumi_pealkiri:
            l_albumid.append(Album(albumi_pealkiri, ilmumis_aasta, l_artistid[-1]))
            l_artistid[l_art_nimed.index(artist)].lisa_album(l_albumid[-1])
        else:
            pass

        l_laulud.append(Laul(laulu_pealkiri, l_artistid[-1], l_albumid[-1]))
        l_artistid[-1].albumid[-1].lisa_laul(l_laulud[-1])

# Üldine otsing
#while True:
    #ul_otsing(input("Otsing: "))

# Kategooriline otsing / Suunatud otsing
while True:
    print("\nKategooria:")
    print("\t1. Artistid")
    print("\t2. Albumid")
    print("\t3. Laulud")

    kat_otsing(input("Nr: "), input("Otsing: "))

