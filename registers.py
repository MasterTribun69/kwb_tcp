
from .const import TEMP_CELSIUS, PERCENTAGE

REGISTER_DEFINITIONS = {
    "Anlage Aus/Ein": {
        "address": 2300,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 = Aus\n1 = Ein",
        "writable": True,
        "value_map": {
            0: "Aus",
            1: "Ein"
        }
        
    },
    "Kesseltemperatur Soll 1": {
        "address": 2301,
        "type": "int",
        "scale": 1.0,
        "unit": "°C",
        "description": None
    },
    "Alarme beheben": {
        "address": 2302,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 = Aus\n1 = Ein",
        "writable": True,
        "value_map": {
            0: "Aus",
            1: "Ein"
        }
    },
    "Puffer 0 Temperatur Maximum": {
        "address": 2307,
        "type": "int",
        "scale": 1.0,
        "unit": "°C",
        "description": None,
        "writable": True
    },
    "Puffer 0 Temperatur Minimum": {
        "address": 2308,
        "type": "int",
        "scale": 1.0,
        "unit": "°C",
        "description": None,
        "writable": True
    },
    "Puffer 0 Programm": {
        "address": 2309,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 = Zeitprogramm\n1 = Temperatur\n2 = Aus\n3 = Handbetrieb",
        "value_map": {
            0: "Zeitprogramm",
            1: "Temperatur",
            2: "Aus",
            3: "Handbetrieb"
        }
    },
    "Kesselanforderung": {
        "address": 2334,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 = Aus\n1 = Ein",
        "value_map": {
            0: "Aus",
            1: "Ein"
        }
    },
    "Betriebsstunden": {
        "address": 2336,
        "type": "float",
        "scale": 1.0,
        "unit": "h",
        "description": None
    },
    "Kesselleistung": {
        "address": 2338,
        "type": "int",
        "scale": 1.0,
        "unit": "%",
        "description": None
    },
    "Kesselstatus": {
        "address": 2339,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 = Aus\n1 = Bereitschaft\n2 = Zünden Warten\n3 = Zünden\n4 = Betrieb\n5 = Abstellen\n6 = Störung",
        "value_map": {
            0: "Aus",
            1: "Bereitschaft",
            2: "Zünden Warten",
            3: "Zünden",
            4: "Betrieb",
            5: "Abstellen",
            6: "Störung"
        }
    },
    "Rauchgastemperatur": {
        "address": 2346,
        "type": "float",
        "scale": 1.0,
        "unit": "°C",
        "description": None
    },
    "Kesseltemperatur": {
        "address": 2347,
        "type": "float",
        "scale": 1.0,
        "unit": "°C",
        "description": None
    },
    "Rücklauftemperatur": {
        "address": 2348,
        "type": "float",
        "scale": 1.0,
        "unit": "°C",
        "description": None
    },
    "Motor Brandschutzklappe": {
        "address": 2358,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 = Aus\n1 = Ein",
        "value_map": {
            0: "Aus",
            1: "Ein"
        }
    },
    "Motor Reinigung": {
        "address": 2359,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 = Aus\n1 = Ein",
        "value_map": {
            0: "Aus",
            1: "Ein"
        }
    },
    "Zündung Heizung": {
        "address": 2361,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 = Aus\n1 = Ein",
        "value_map": {
            0: "Aus",
            1: "Ein"
        }
    },
    "Mischer Rücklaufanhebung": {
        "address": 2362,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 = Aus\n1 = Auf\n2 = Zu",
        "value_map": {
            0: "Aus",
            1: "Auf",
            2: "Zu"
        }
    },
    "Zündung Gebläse": {
        "address": 2367,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 = Aus\n1 = Ein",
        "value_map": {
            0: "Aus",
            1: "Ein"
        }
    },
    "Motor Drehrost": {
        "address": 2368,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 = Aus\n1 = Ein",
        "value_map": {
            0: "Aus",
            1: "Ein"
        }
    },
    "Kessel Solltemperatur": {
        "address": 2392,
        "type": "int",
        "scale": 1.0,
        "unit": "°C",
        "description": None
    },
    "Status Raumaustragung": {
        "address": 2403,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 =Aus\n1 = Öffnet\n2 = Steht\n3 = Füllt\n4 = Füllt \n5 = Steht\n6 = Füllt",
        "value_map": {
            0: "Aus",
            1: "Öffnet",
            2: "Steht",
            3: "Füllt",
            4: "Füllt",
            5: "Steht",
            6: "Füllt"
        }
    },
    "Überfüllschutz Raumaustragung": {
        "address": 2408,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 = Aus\n1 = Ein",
        "value_map": {
            0: "Aus",
            1: "Ein"
        }
    },
    "Boiler 0  Temperatur": {
        "address": 2434,
        "type": "float",
        "scale": 0.1,
        "unit": "°C",
        "description": None
    },
    "Boiler 0  Pumpe": {
        "address": 2435,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 = Aus\n1 = Ein",
        "value_map": {
            0: "Aus",
            1: "Ein"
        }
    },
    "HK0 Außentemperatur": {
        "address": 2436,
        "type": "float",
        "scale": 0.1,
        "unit": "°C",
        "description": None
    },
    "HK0 Raumtemperatur": {
        "address": 2437,
        "type": "float",
        "scale": 0.1,
        "unit": "°C",
        "description": None
    },
    "HK0 Vorlauftemperatur": {
        "address": 2438,
        "type": "float",
        "scale": 0.1,
        "unit": "°C",
        "description": None
    },
    "HK0 Pumpe": {
        "address": 2439,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 = Aus\n1 = Ein",
        "value_map": {
            0: "Aus",
            1: "Ein"
        }
    },
    "Puffer 0 Temperatur 1": {
        "address": 2440,
        "type": "float",
        "scale": 1.0,
        "unit": "°C",
        "description": None
    },
    "Puffer 0 Temperatur 2": {
        "address": 2441,
        "type": "float",
        "scale": 1.0,
        "unit": "°C",
        "description": None
    },
    "HK1 Außentemperatur": {
        "address": 2442,
        "type": "float",
        "scale": 0.1,
        "unit": "°C",
        "description": None
    },
    "HK1 Raumtemperatur": {
        "address": 2443,
        "type": "float",
        "scale": 0.1,
        "unit": "°C",
        "description": None
    },
    "HK1 Vorlauftemperatur": {
        "address": 2444,
        "type": "float",
        "scale": 0.1,
        "unit": "°C",
        "description": None
    },
    "HK1 Pumpe": {
        "address": 2445,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 = Aus\n1 = Ein",
        "value_map": {
            0: "Aus",
            1: "Ein"
        }
    },
    "HK2 Außentemperatur": {
        "address": 2446,
        "type": "float",
        "scale": 0.1,
        "unit": "°C",
        "description": None
    },
    "HK2 Raumtemperatur": {
        "address": 2447,
        "type": "float",
        "scale": 0.1,
        "unit": "°C",
        "description": None
    },
    "HK2 Vorlauftemperatur": {
        "address": 2448,
        "type": "float",
        "scale": 0.1,
        "unit": "°C",
        "description": None
    },
    "HK2 Pumpe": {
        "address": 2449,
        "type": "status",
        "scale": 1.0,
        "unit": None,
        "description": "0 = Aus\n1 = Ein",
        "value_map": {
            0: "Aus",
            1: "Ein"
        }
    }
}

ALARM_REGISTER_BASE = 2315
ALARM_REGISTER_COUNT = 16

ALARM_TEXTS = {
    1000: "Die Regelung ist nicht vollständig eingestellt!",
    1001: "Speicherbaustein ist defekt!",
    1002: "Elektronischer Defekt an den digitalen Eingängen!",
    1003: "Die Uhrzeit muss neu eingestellt werden!",
    1004: "Das Wartungsintervall ist abgelaufen. Verständigen Sie den Kundendienst!",
    1005: "Sicherheitsthermostat! Überhitzung des Kessels!",
    1006: "Hauptantriebsmotor ist überhitzt!",
    1007: "Die Zündung funktioniert nicht!",
    1008: "Der Brennstoffbunker ist leer! Bitte nachfüllen!",
    1009: "Defekter Triac bei Hauptantrieb oder Raumaustragungsantrieb!",
    1010: "Die Rücklaufanhebung funktioniert nicht!",
    1011: "Raumaustragungsmotor 1 ist überhitzt!",
    1012: "Brandschutzklappe öffnet nicht!",
    1013: "Temperaturanstieg im Brennstoffvorrat. Feueralarm!",
    1014: "Die Elektronik hat 70°C!",
    1015: "Der Rauchgasfühler fehlt oder ist defekt!",
    1016: "Der Rücklauffühler fehlt oder ist defekt!",
    1017: "Der Kesselfühler fehlt oder ist defekt!",
    1018: "Brandschutzklappe schließt nicht!",
    1019: "Der Wasserbehälter der Notlöscheinrichtung ist leer! Bedienungsanleitung beachten.",
    1020: "Die Glutbettfühlerelektronik ist defekt!",
    1021: "Die Glutbettfühlerelektronik ist falsch montiert!",
    1022: "Hauptantriebsmotor ist überlastet!",
    1023: "Der Brennstoffbehälter ist leer. Bitte nachfüllen!",
    1024: "Der Überfüllschutzschalter der Raumaustragung 1 ist offen!",
    1025: "Der Raumaustragungsmotor ist überlastet!",
    1026: "Ein Motor der Zusatzraumaustragung ist überlastet!",
    1027: "Ein Motor der Zusatzraumaustragung ist überhitzt!",
    1028: "Ein Überfüllschutzschalter der Zusatzraumaustragung ist offen!",
    1029: "Der Deckel vom Aschebehälter ist offen!",
    1030: "Der Vorlauffühler von Heizkreis Nr 0 fehlt oder ist defekt!",
    1031: "Der Raumfühler am Heizkreis Nr 0 fehlt oder ist defekt!",
    1032: "Der Außenfühler am Heizkreis Nr 0 fehlt oder ist defekt!",
    1033: "Der Vorlauffühler von Heizkreis Nr 1 fehlt oder ist defekt!",
    1034: "Der Raumfühler am Heizkreis Nr 1 fehlt oder ist defekt!",
    1035: "Der Außenfühler am Heizkreis Nr 1 fehlt oder ist defekt!",
    1036: "Der Vorlauffühler von Heizkreis Nr 2 fehlt oder ist defekt!",
    1037: "Der Raumfühler am Heizkreis Nr 2 fehlt oder ist defekt!",
    1038: "Der Außenfühler am Heizkreis Nr 2 fehlt oder ist defekt!",
    1135: "Der Fühler am Boiler Nr 0 fehlt oder ist defekt!",
    1136: "Der Fühler am Boiler Nr 1 fehlt oder ist defekt!",
    1152: "Der Fühler 1 vom Puffer Nr 0 fehlt oder ist defekt!",
    1153: "Der Fühler 2 vom Puffer Nr 0 fehlt oder ist defekt!",
    1186: "Netzwerkfehler am Kesselmodul!",
    1187: "Netzwerkfehler am Kesselmodul 2!",
    1188: "Netzwerkfehler am Heizkreismodul Nr 0!",
    1189: "Netzwerkfehler am Heizkreismodul Nr 1!",
    1204: "Netzwerkfehler am digitalen Fernbediengerät Nr 0!",
    1205: "Netzwerkfehler am digitalen Fernbediengerät Nr 1!",
    1206: "Netzwerkfehler am digitalen Fernbediengerät Nr 2!",
    1238: "Fehler im Heizkreisnetz!",
    1239: "Der Kesselfühler am Zweitkessel fehlt oder ist defekt!",
    1240: "Der Unterdruck im Brennraum kann nicht geregelt werden!",
    1241: "Der Unterdrucksensor ist defekt!",
    1242: "Der Sauerstoffsensor fehlt oder ist defekt!",
    1243: "Temperaturanstieg im Aschebehälter!",
    1244: "Kalibrierungsfehler der Lambdasonde.",
    1245: "Die Versorgung am Raumaustragungsmodul ist unterbrochen!",
    1246: "Defekter Triac am Raumaustragungsmodul!",
    1247: "Netzwerkfehler am Raumaustragungsmodul!",
    1248: "Das Kontrollintervall istabgelaufen.",
    1249: "Die Kaminkehrerfunktion ist aktiv",
    1250: "Platinenrevision und Anlagennummer sind nicht kompatibel",
    1251: "Der Not Ausschalter ist gedrückt!",
    1252: "Konfigurationsfehler! Letzte Sicherung aktiviert!",
    1253: "Unterschreitung der Puffertemperatur",
    1254: "Der Saugbehälter ist leer!",
    1255: "Fehler GSM Modul!",
    # ggf. weiter bis 255 ergänzen
}
