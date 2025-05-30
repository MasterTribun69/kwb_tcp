🔍 Projektbeschreibung

Diese benutzerdefinierte Home Assistant Integration erlaubt die Überwachung und Steuerung einer KWB Heizanlage über Modbus TCP. Die Integration liest Daten aus einer definierten Registerliste aus und stellt sie als Sensoren, Zahlenfelder und Auswahlfelder in Home Assistant bereit.

📁 Projektstruktur

kwb_tcp/
├── translations/
│   ├── de.json
│   └── en.json
├── __init__.py
├── base_sensor.py
├── config_flow.py
├── const.py
├── coordinator.py
├── manifest.json
├── number.py
├── README.md
├── registers.py
├── select.py
└── sensor.py

📚 Installation

Repository klonen oder ZIP herunterladen

git clone https://github.com/<username>/kwb_tcp.git

Ordner kopieren:
Den Ordner kwb_tcp in das Home Assistant Verzeichnis config/custom_components/ legen:

/config/custom_components/kwb_tcp/

Home Assistant neustarten.

Integration über "Einstellungen > Integrationen" hinzufügen.

📊 Features

Automatische Erkennung aller Register gemäß registers.py

int und float Register als number

status Register mit value_map als select

Nur lesbare Register als Sensoren

Fehlererkennung bei Modbus-Verbindung oder ungültigen Werten

Alarme (als kombinierter Statussensor)

👷 Konfiguration

Beim Hinzufügen der Integration müssen folgende Werte angegeben werden:

IP-Adresse der KWB Anlage

Port (Standard: 502)

🌐 Lokalisierung

Die Dateien in translations/ stellen die UI-Texte für Deutsch (de.json) und Englisch (en.json) bereit. Neue Sprachen können leicht ergänzt werden.

✉️ Fehler & Feedback

Fehler können gerne als GitHub-Issue gemeldet werden. Bitte Protokollauszüge oder Screenshots beilegen.

🚀 Zukünftige Erweiterungen

Write-Unterstützung für weitere Typen

Automatische Skalenerkennung

Konfigurierbare Bereichszuordnung ("area")

WebUI über SVG oder Lovelace

📖 Lizenz

MIT License

✍️ Beispiel für configuration.yaml (nur für manuelle Einbindung)

logger:
  default: info
  logs:
    custom_components.kwb_tcp: debug

