class Album():
    """ Albumi klass:

    Klassi omadused (Attributes):
    p_pealkiri (str) = Albumi pealkiri
    p_aaasta (int) = Albumi ilmumis aasta
    p_artist (str) = Albumi koostaja
    laulud (obj) = Albumis olevad laulud

    """
    def __init__(self, p_pealkiri, p_aasta, p_koostaja):
        self.pealkiri = p_pealkiri
        self.aasta = p_aasta
        self.artist = p_koostaja
        self.laulud = []

    def lisa_laul(self, p_laul):
        self.laulud.append(p_laul)