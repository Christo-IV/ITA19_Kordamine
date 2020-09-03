class Artist:

    """ Artisti klass:

    p_nimi (str) = Artisti nimi
    albumid (obj) = Artisti albumid

    """

    def __init__(self, p_nimi):
        self.nimi = p_nimi
        self.albumid = []

    def lisa_albumi(self, p_album):
        self.albumid.append((p_album))