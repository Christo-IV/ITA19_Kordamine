class Laul:
    """ Klass laul

    Klassi omadused (Attributes):
    p_pealkiri (str) - Laulu pealkiri
    p_artist (obj) - Laulu artist
    p_albumi (obj) - "Album" objekt milles laul on
    """

    def __init__(self, p_pealkiri, p_artist, p_album=None):
        self.pealkiri = p_pealkiri
        self.artist = p_artist
        self.album = p_album