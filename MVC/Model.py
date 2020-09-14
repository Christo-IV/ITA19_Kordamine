class Model:
    def __init__(self, p_elemendid):
        self.elemendid = p_elemendid

    def lisa_element(self, p_elemendid):
        self.elemendid.append(p_elemendid)

    def loe_elemendid(self):
        return self.elemendid

    def loe_element(self, p_nimetus):
        for element in self.elemendid:
            if p_nimetus in element:
                return element
            else:
                return {}

    def kustuta_element(self, p_nimetus):
        self.elemendid.remove(p_nimetus)

    def muuda_element(self, p_mida, p_milleks):
        for element in self.elemendid:
            if p_mida in element or p_mida in element.values():
                element