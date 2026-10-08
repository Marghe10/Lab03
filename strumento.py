class Strumento:

    def __init__(self, id_strumento, tipo, marca, anno, valore):
        self.id_strumento = id_strumento
        self.tipo = tipo
        self.marca = marca
        self.anno = anno
        self.valore = valore

    def __str__(self):
        stringa_strumento = f"Tipo: {self.tipo} - Marca: {self.marca} - Anno: {self.anno} - Valore: {self.valore}"
        return stringa_strumento
