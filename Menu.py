from laul import Laul
from Album import Album
from Artist import Artist

# Albumite nimekirja lugemine
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


# valjasta_koik()

with open("albumid.txt", encoding="utf-8") as file:
    l_albumid = []  # (obj) List kus on kõik "Album" objektid sees
    l_artistid = []  # (obj) List kus on kõik "Artist" objektid

    for line in file:
        artist, albumi_pealkiri, ilmumis_aasta, laulu_pealkiri = line.split("\t")
        try:
            if artist != l_artistid[-1].nimi:
                l_artistid.append(Artist(artist))
                l_artistid[-1].albumid.append(Album(albumi_pealkiri, ilmumis_aasta, l_artistid[-1]))

            elif l_artistid[-1].albumid[-1].pealkiri != albumi_pealkiri:
                l_artistid[-1].albumid.append(Album(albumi_pealkiri, ilmumis_aasta, l_artistid[-1]))
            else:
                pass
        except IndexError:
            l_artistid.append(Artist(artist))
            l_artistid[-1].albumid.append(Album(albumi_pealkiri, ilmumis_aasta, l_artistid[-1]))
        l_artistid[-1].albumid[-1].lisa_laul(Laul(laulu_pealkiri, l_artistid[-1]))

for e_artist in l_artistid:
    print(e_artist.nimi + ":")
    for e_album in e_artist.albumid:
        print("\t" + e_album.pealkiri, "(" + e_album.aasta + "):")
        for nr, e_laul in enumerate(e_album.laulud):
            print("\t\t" + str(nr) +". "+ e_laul.pealkiri.strip("\n"))
    print()