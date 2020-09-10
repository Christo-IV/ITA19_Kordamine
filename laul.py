class Laul:
    """ Klass laul

    Klassi omadused (Attributes):
    p_pealkiri (str) - Laulu pealkiri
    p_artist (obj) - Laulu artist
    p_albumi (obj) - "Album" objekt milles laul on

    valjasta() - Valjastab kõik objekti omaduste väärtused

    """

    def __init__(self, p_nimi, p_artist, p_album=None):
        self.nimi = p_nimi
        self.artist = p_artist
        self.album = p_album

    def valjasta(self, p_indents, p_jrk):
        p_indents = "\t" * p_indents
        print(p_indents + "%s. '%s' - %s (%s (%s))" %
              (str(p_jrk), self.nimi, self.artist.nimi, self.album.nimi, str(self.album.aasta)))