import csv

from prestito import Prestito
from strumento import Strumento
from operator import attrgetter

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome=nome
        self.responsabile=responsabile
        self.strumenti = []
        self.prestiti=[]

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
        strumenti_ordinati=sorted(self.strumenti, key=attrgetter("marca"))
        print(strumenti_ordinati)
        return strumenti_ordinati

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        # controllo se lo strumento è presente nella lista self.strumenti[]
        id_strumento_da_prestare = id_strumento
        cognome_allievo=cognome_allievo
        data_prestito=data
        strumento_trovato=False
        for x in self.strumenti:
            if x.id_strumento == id_strumento_da_prestare:
                strumento_trovato=True
                print(f"trovato strumento: Id strumento: {x.id_strumento} tipo: {x.tipo}")
                break
        if not strumento_trovato: # è come dire if strumento==False
            raise Exception("Strumento non presente del deposito")

        # controllo se lo strumento è già in prestito scorrendo gli elementi della lista prestiti
        for s in self.prestiti:
            if s.id_strumento == id_strumento_da_prestare:
                raise Exception("Lo strumento è già in prestito")

        numero_prestito = int(len(self.prestiti)) + 1
        id_prestito = "P" + str(numero_prestito)

        nuovo_prestito=Prestito(data_prestito, id_strumento_da_prestare, cognome_allievo, id_prestito)
        self.prestiti.append(nuovo_prestito)
        return nuovo_prestito


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        for a in self.prestiti:
            if a.id_prestito == id_prestito:
                self.prestiti.remove(a)

        raise Exception("Prestito non trovato")