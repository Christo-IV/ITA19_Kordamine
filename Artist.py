class Artist:

    """ Artisti klass:

    p_nimi (str) - Artisti nimi
    albumid (obj) - Artisti albumid

    valjasta() - Valjastab kõik objekti omaduste väärtused

    """

    def __init__(self, p_nimi):
        self.nimi = p_nimi
        self.albumid = []

    def lisa_album(self, p_album):
        self.albumid.append(p_album)

    def valjasta(self, p_indents, p_jrk):
        p_indents = "\t" * p_indents
        print(p_indents + str(p_jrk) + ". " + self.nimi + ":")
        for nr, album in enumerate(self.albumid, 1):
            print(p_indents + "\t%s. %s (%s)" % (str(nr), album.nimi, str(album.aasta)))
