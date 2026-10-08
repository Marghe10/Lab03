import csv
from strumento import Strumento

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome=nome
        self.responsabile=responsabile
        self.strumenti = []

    #def set_nome_responsabile(self, nuovo_responsabile):
    #    self.nome=nuovo_responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO

        with open(file_path, 'r', encoding='utf-8') as file:
            lettore=csv.reader(file)
            for riga in lettore:
                id_strumento = riga[0].strip()
                tipo = riga[1].strip()
                marca = riga[2].strip()
                anno = int(riga[3])
                valore = float(riga[4])

                strumento = Strumento(id_strumento, tipo, marca, anno, valore )
                self.strumenti.append(strumento)


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        ultimo_strumento = self.strumenti[-1]
        # print(f"Ultimo strumento: {ultimo_strumento}")
        id_ultimo_strumento = ultimo_strumento.id_strumento
        # print(f"id_ultimo_strumento: {id_ultimo_strumento}")
        solo_numero = int(id_ultimo_strumento[1:])
        # print(f"solo_numero: {solo_numero}")
        nuovo_id = "S"+str(solo_numero+1)
        # print(f"nuovo_id: {nuovo_id}")

        nuovo_strumento = Strumento(nuovo_id, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(nuovo_strumento)
        return nuovo_strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
