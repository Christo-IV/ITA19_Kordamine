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
    l_albumid = []
    l_artistid = []
    prev_artists = ""
    prev_albums = ""
    prev_laul = ""


    for line in file:
        artist, albumi_pealkiri, ilmumis_aasta, laulu_pealkiri = line.split("\t")

        if artist not in prev_artists:
            l_artistid.append(Artist(artist))
            with l_artistid[len(l_artistid)-1] as viimne_artist:
                viimne_artist.lisa_albumi(Album(albumi_pealkiri, ilmumis_aasta, viimne_artist))
                viimne_artist.albumid[len(viimne_artist.albumid)-1].lisa_laul(Laul(laulu_pealkiri, viimne_artist))
        else:
            with l_artistid[len(l_artistid) - 1] as viimne_artist:
                if albumi_pealkiri not in prev_albums:
                    viimne_artist.lisa_albumi(Album(albumi_pealkiri, ilmumis_aasta, viimne_artist).lisa_laul(Laul(laulu_pealkiri, viimne_artist)))
                    #viimne_artist.albumid[len(viimne_artist.albumid)-1].lisa_laul(Laul(laulu_pealkiri, viimne_artist))
                else:
                    viimne_artist.albumid[len(viimne_artist.albumid) - 1].lisa_laul(Laul(laulu_pealkiri, viimne_artist))

        prev_artists += artist
        prev_albums += albumi_pealkiri
        prev_laul = laulu_pealkiri

for e_artist in l_artistid:  # Võtab iga artisti objekti, mis on l_artistid listis
    print(e_artist.nimi)
    print("ARTISITD:", e_artist)
    for e_album in e_artist.albumid:  # Võtab iga albumi objekti, mis on e_artisti objekti "albumid" omaduse listis
        print("\t" + e_album.pealkiri, "(" + e_album.aasta + "):")
        print("\tALBUMID:", e_artist.albumid)
        for nr, e_laul in enumerate(e_album.laulud):  # Võtab ja nummerdab iga laulu objekti, mis on e_album objekti "laulud" omaduse listis
            print("\t\t" + str(nr+1) + ". " + e_laul.pealkiri)
            print("\t\tLAULUD:", e_album.laulud)
    break

"""
# Laulu objektid
laul_1 = Laul("Journey to the West", "Elijah Nang")
laul_2 = Laul("Sleeping on the Susuki Grasslands", "Elijah Nang")
laul_3 = Laul("Kumite", "Elijah Nang")
laul_4 = Laul("Kenjutsu water style", "Elijah Nang")


# Albumite loomine
album_1 = Album("Gajin", 2019, "MoMo")
album_2 = Album("Bushido", 2019, "MoMo")

# Laulude albumitesse lisamine
# Album 1
album_1.lisa_laul(laul_1)
album_1.lisa_laul(laul_2)

# Album 2
album_2.lisa_laul(laul_3)
album_2.lisa_laul(laul_4)

# Artisti klassi tesimine
artist = Artist("Elijah Nang")
artist.lisa_albumi(album_1)
artist.lisa_albumi(album_2)

for album in artist.albumid:
    print(album.pealkiri + ":")
    for laul in album.laulud:
        print(laul.artist, "-", laul.pealkiri)
    print()
"""
