class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrizione(self):
        return f"{self.marca} {self.modello}, Anno: {self.anno}"
    
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, serbatoio):
        super().__init__(marca, modello, anno)
        self.serbatoio = serbatoio

    def descrizione_serbatoio(self):
        return f"{self.descrizione()}, Serbatoio: {self.serbatoio} litri"
