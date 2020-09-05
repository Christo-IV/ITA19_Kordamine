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

# Kõikide objektide hulgast (l_artistid, l_albumid, l_laulud) kindlate objektide otsimine
def otsing(p_otsitav_märksõna):
    tulemused = [[], [], []]
    p_otsitav_märksõna = str(p_otsitav_märksõna).lower()
    n = 0
    for e_laul in l_laulud:
        if p_otsitav_märksõna in e_laul.pealkiri.lower():
            tulemused[0].append(e_laul)
        else:
            pass
    for e_album in l_albumid:
        if p_otsitav_märksõna in e_album.pealkiri.lower() or p_otsitav_märksõna in str(e_album.aasta):
            tulemused[1].append(e_album)
        else:
            pass
    for e_artist in l_artistid:
        if p_otsitav_märksõna in e_artist.nimi.lower():
             tulemused[2].append(e_artist)
        else:
             pass
    return tulemused

# Artist, Album & Laul objektide tegemine ja kindlatesse listidesse lisamine
with open("albumid.txt", encoding="utf-8") as file:
    l_artistid = []  # (obj) List kus on kõik "Artist" objektid
    l_albumid = []  # (obj) List kus on kõik "Album" objektid
    l_laulud = []  # (obj) List kus on kõik "Laul" objektid

    for line in file:
        artist, albumi_pealkiri, ilmumis_aasta, laulu_pealkiri = line.strip("\n").split("\t")
        try:
            if artist != l_artistid[-1].nimi:
                l_artistid.append(Artist(artist))
                l_albumid.append(Album(albumi_pealkiri, ilmumis_aasta, l_artistid[-1]))
                l_artistid[-1].lisa_album(l_albumid[-1])

            elif l_artistid[-1].albumid[-1].pealkiri != albumi_pealkiri:
                l_albumid.append(Album(albumi_pealkiri, ilmumis_aasta, l_artistid[-1]))
                l_artistid[-1].lisa_album(l_albumid[-1])
            else:
                pass
        except IndexError:
            l_artistid.append(Artist(artist))
            l_albumid.append(Album(albumi_pealkiri, ilmumis_aasta, l_artistid[-1]))
            l_artistid[-1].lisa_album(l_albumid[-1])

        l_laulud.append(Laul(laulu_pealkiri, l_artistid[-1], l_albumid[-1]))
        l_artistid[-1].albumid[-1].lisa_laul(l_laulud[-1])

# Kindlate tulemuste/objektide otsimine ja nende väljastamine
otsitav = input("Otsing: ")
for e_grupp in otsing(otsitav):
    try:
        if type(e_grupp[0]) == Laul:
            print("Laulud:")
            for nr, e_laul in enumerate(e_grupp, 1):
                print("\t%s. '%s' --- %s (%s (%s))" % (nr, e_laul.pealkiri, e_laul.artist.nimi, e_laul.album.pealkiri, str(e_laul.album.aasta)))
        if type(e_grupp[0]) == Album:
            print("Albumid:")
            for nr, e_album in enumerate(e_grupp, 1):
                print("\t%s. %s (%s)" % (nr, e_album.pealkiri, e_album.aasta))
        if type(e_grupp[0]) == Artist:
            print("Artistid:")
            for nr, e_artist in enumerate(e_grupp, 1):
                print("\t%s. %s:" % (nr, e_artist.nimi))
                for nr2, e_album2 in enumerate(e_artist.albumid, 1):
                    print("\t\t%s. %s (%s)" % (nr2, e_album2.pealkiri, e_album2.aasta))
    except IndexError:
        continue