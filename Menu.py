from laul import Laul
from Album import Album
from Artist import Artist

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