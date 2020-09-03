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
    albumid = []
    artistid = []

    prev_artist = ""
    prev_album = ""
    prev_laul = ""

    for line in file:
        artist, albumi_pealkiri, ilmumis_aasta, laulu_pealkiri = line.split("\t")

        if artist != prev_artist:
            artistid.append(Artist(artist))
            with artistid[len(artistid)-1] as viimne_artist:
                viimne_artist.lisa_albumi(Album(albumi_pealkiri, ilmumis_aasta, viimne_artist))
                viimne_artist.albumid[viimne_artist].lisa
        else:
            pass

        if albumi_pealkiri != prev_album:
            albumid.append(Album(albumi_pealkiri, ilmumis_aasta, Artist(artist)))
            albumid[len(albumid)-1].lisa_laul(Laul(laulu_pealkiri, artistid[len(artistid)-1]))
        else:
            albumid[len(albumid) - 1].lisa_laul(Laul(laulu_pealkiri, artistid[len(artistid) - 1]))

        prev_artist = artist
        prev_album = albumi_pealkiri
        prev_laul = laulu_pealkiri

for album in albumid:
    print(album.pealkiri + ":\n" + album.artist.nimi)
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
