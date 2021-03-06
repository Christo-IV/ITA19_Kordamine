class Album:
    """ Albumi klass:

    Klassi omadused (Attributes):
    p_pealkiri (str) - Albumi pealkiri
    p_aasta (int) - Albumi ilmumis aasta
    p_artist (obj) - Albumi tegija
    laulud (obj) - Albumis olevad laulud

    valjasta() - Valjastab kõik objekti omaduste väärtused

    """

    def __init__(self, p_nimi, p_aasta, p_artist):
        self.nimi = p_nimi
        self.aasta = int(p_aasta)
        self.artist = p_artist
        self.laulud = []

    def lisa_laul(self, p_laul):
        self.laulud.append(p_laul)

    def valjasta(self, p_jrk):
        print("\t%s. %s (%s) - %s" % (str(p_jrk), self.nimi, str(self.aasta), self.artist.nimi))
