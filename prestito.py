class Prestito:
    def __init__(self, data, id_strumento, cognome_allievo, id_prestito):
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo
        self.id_prestito = id_prestito

    def __str__(self):
        stringa_prestito = f"data prestito: {self.data} -id strumento prestato: {self.id_prestito} - cognome allievo: {self.cognome_allievo} - id prestito: {self.id_prestito} "
        return stringa_prestito