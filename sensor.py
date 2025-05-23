"""Autogenerierte Sensor-Datei für KWB TCP Heizung"""

import logging
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_entities, discovery_info=None):
    return

async def async_setup_entry(hass, config_entry, async_add_entities):
    host = hass.data["kwb_tcp"]["host"]
    port = hass.data["kwb_tcp"]["port"]
    sensors = []

    sensors.append(KwbSensor0(host, port))
    sensors.append(KwbSensor1(host, port))
    sensors.append(KwbSensor2(host, port))
    sensors.append(KwbSensor3(host, port))
    sensors.append(KwbSensor4(host, port))
    sensors.append(KwbSensor5(host, port))
    sensors.append(KwbSensor6(host, port))
    sensors.append(KwbSensor7(host, port))
    sensors.append(KwbSensor8(host, port))
    sensors.append(KwbSensor9(host, port))
    sensors.append(KwbSensor10(host, port))
    sensors.append(KwbSensor11(host, port))
    sensors.append(KwbSensor12(host, port))
    sensors.append(KwbSensor13(host, port))
    sensors.append(KwbSensor14(host, port))
    sensors.append(KwbSensor15(host, port))
    sensors.append(KwbSensor16(host, port))
    sensors.append(KwbSensor17(host, port))
    sensors.append(KwbSensor18(host, port))
    sensors.append(KwbSensor19(host, port))
    sensors.append(KwbSensor20(host, port))
    sensors.append(KwbSensor21(host, port))
    sensors.append(KwbSensor22(host, port))
    sensors.append(KwbSensor23(host, port))
    sensors.append(KwbSensor24(host, port))
    sensors.append(KwbSensor25(host, port))
    sensors.append(KwbSensor26(host, port))
    sensors.append(KwbSensor27(host, port))
    sensors.append(KwbSensor28(host, port))
    sensors.append(KwbSensor29(host, port))
    sensors.append(KwbSensor30(host, port))
    sensors.append(KwbSensor31(host, port))
    sensors.append(KwbSensor32(host, port))
    sensors.append(KwbSensor33(host, port))
    sensors.append(KwbSensor34(host, port))
    sensors.append(KwbSensor35(host, port))
    sensors.append(KwbSensor36(host, port))
    sensors.append(KwbSensor37(host, port))

    sensors.append(KwbAlarmSensor(host, port))
    async_add_entities(sensors)


class KwbSensor0(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Anlage Aus/Ein"
        self._address = 2300
        self._unit = ""
        self._scale = 1.0
        self._description = '0 = Aus\n1 = Ein'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor1(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Kesseltemperatur Soll 1"
        self._address = 2301
        self._unit = "°C"
        self._scale = 1.0
        self._description = None
        self._datatype = "int"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor2(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Alarme beheben"
        self._address = 2302
        self._unit = ""
        self._scale = 1.0
        self._description = '0 = Aus\n1 = Ein'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor3(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Puffer 0 Temperatur Maximum"
        self._address = 2307
        self._unit = "°C"
        self._scale = 1.0
        self._description = None
        self._datatype = "int"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor4(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Puffer 0 Temperatur Minimum"
        self._address = 2308
        self._unit = "°C"
        self._scale = 1.0
        self._description = None
        self._datatype = "int"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor5(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Puffer 0 Programm"
        self._address = 2309
        self._unit = ""
        self._scale = 1.0
        self._description = '0 = Zeitprogramm\n1 = Temperatur\n2 = Aus\n3 = Handbetrieb'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor6(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Kesselanforderung"
        self._address = 2334
        self._unit = ""
        self._scale = 1.0
        self._description = '0 = Aus\n1 = Ein'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor7(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Betriebsstunden"
        self._address = 2336
        self._unit = "h"
        self._scale = 1.0
        self._description = None
        self._datatype = "int"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor8(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Kesselleistung"
        self._address = 2338
        self._unit = "%"
        self._scale = 1.0
        self._description = None
        self._datatype = "int"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor9(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Kesselstatus"
        self._address = 2339
        self._unit = ""
        self._scale = 1.0
        self._description = '0 = Aus\n1 = Bereitschaft\n2 = Zünden Warten\n3 = Zünden\n4 = Betrieb\n5 = Abstellen\n6 = Störung'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor10(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Rauchgastemperatur"
        self._address = 2346
        self._unit = "°C"
        self._scale = 1.0
        self._description = None
        self._datatype = "float"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor11(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Kesseltemperatur"
        self._address = 2347
        self._unit = "°C"
        self._scale = 1.0
        self._description = None
        self._datatype = "float"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor12(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Rücklauftemperatur"
        self._address = 2348
        self._unit = "°C"
        self._scale = 1.0
        self._description = None
        self._datatype = "float"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor13(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Motor Brandschutzklappe"
        self._address = 2358
        self._unit = ""
        self._scale = 1.0
        self._description = '0 = Aus\n1 = Ein'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor14(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Motor Reinigung"
        self._address = 2359
        self._unit = ""
        self._scale = 1.0
        self._description = '0 = Aus\n1 = Ein'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor15(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Zündung Heizung"
        self._address = 2361
        self._unit = ""
        self._scale = 1.0
        self._description = '0 = Aus\n1 = Ein'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor16(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Mischer Rücklaufanhebung"
        self._address = 2362
        self._unit = ""
        self._scale = 1.0
        self._description = '0 = Aus\n1 = Auf\n2 = Zu'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor17(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Zündung Gebläse"
        self._address = 2367
        self._unit = ""
        self._scale = 1.0
        self._description = '0 = Aus\n1 = Ein'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor18(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Motor Drehrost"
        self._address = 2368
        self._unit = ""
        self._scale = 1.0
        self._description = '0 = Aus\n1 = Ein'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor19(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Kessel Solltemperatur"
        self._address = 2392
        self._unit = "°C"
        self._scale = 1.0
        self._description = None
        self._datatype = "int"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor20(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Status Raumaustragung"
        self._address = 2403
        self._unit = ""
        self._scale = 1.0
        self._description = '0 =Aus\n1 = Öffnet\n2 = Steht\n3 = Füllt\n4 = Füllt \n5 = Steht\n6 = Füllt'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor21(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Überfüllschutz Raumaustragung"
        self._address = 2408
        self._unit = ""
        self._scale = 1.0
        self._description = '0 = Aus\n1 = Ein'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor22(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Boiler 0  Temperatur"
        self._address = 2434
        self._unit = "°C"
        self._scale = 0.1
        self._description = None
        self._datatype = "float"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor23(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Boiler 0  Pumpe"
        self._address = 2435
        self._unit = ""
        self._scale = 1.0
        self._description = '0 = Aus\n1 = Ein'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor24(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "HK0 Außentemperatur"
        self._address = 2436
        self._unit = "°C"
        self._scale = 0.1
        self._description = None
        self._datatype = "float"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor25(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "HK0 Raumtemperatur"
        self._address = 2437
        self._unit = "°C"
        self._scale = 0.1
        self._description = None
        self._datatype = "float"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor26(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "HK0 Vorlauftemperatur"
        self._address = 2438
        self._unit = "°C"
        self._scale = 0.1
        self._description = None
        self._datatype = "float"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor27(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "HK0 Pumpe"
        self._address = 2439
        self._unit = ""
        self._scale = 1.0
        self._description = '0 = Aus\n1 = Ein'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor28(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Puffer 0 Temperatur 1"
        self._address = 2440
        self._unit = "°C"
        self._scale = 1.0
        self._description = None
        self._datatype = "float"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor29(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Puffer 0 Temperatur 2"
        self._address = 2441
        self._unit = "°C"
        self._scale = 1.0
        self._description = None
        self._datatype = "float"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor30(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "HK1 Außentemperatur"
        self._address = 2442
        self._unit = "°C"
        self._scale = 0.1
        self._description = None
        self._datatype = "float"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor31(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "HK1 Raumtemperatur"
        self._address = 2443
        self._unit = "°C"
        self._scale = 0.1
        self._description = None
        self._datatype = "float"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor32(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "HK1 Vorlauftemperatur"
        self._address = 2444
        self._unit = "°C"
        self._scale = 0.1
        self._description = None
        self._datatype = "float"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor33(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "HK1 Pumpe"
        self._address = 2445
        self._unit = ""
        self._scale = 1.0
        self._description = '0 = Aus\n1 = Ein'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor34(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "HK2 Außentemperatur"
        self._address = 2446
        self._unit = "°C"
        self._scale = 0.1
        self._description = None
        self._datatype = "float"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor35(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "HK2 Raumtemperatur"
        self._address = 2447
        self._unit = "°C"
        self._scale = 0.1
        self._description = None
        self._datatype = "float"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor36(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "HK2 Vorlauftemperatur"
        self._address = 2448
        self._unit = "°C"
        self._scale = 0.1
        self._description = None
        self._datatype = "float"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None

class KwbSensor37(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "HK2 Pumpe"
        self._address = 2449
        self._unit = ""
        self._scale = 1.0
        self._description = '0 = Aus\n1 = Ein'
        self._datatype = "status"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        attrs = {}
        if self._description:
            attrs["Status Info"] = self._description
        return attrs if attrs else None


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result = client.read_holding_registers(address=self._address, count=1)
            if not result.isError():
                raw = result.registers[0]
                if self._datatype == "float":
                    self._state = raw * self._scale
                else:
                    self._state = int(raw)
            else:
                self._state = None
            client.close()
        except Exception as e:
            _LOGGER.error(f"[{self._name}] Modbus-Fehler: {e}")
            self._state = None


class KwbAlarmSensor(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "KWB Aktive Alarme"
        self._state = None
        self._active_alarms = []

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return "Alarm" if self._active_alarms else "OK"

    @property
    def should_poll(self):
        return True

    @property
    def extra_state_attributes(self):
        return {
            "aktive_alarme": self._active_alarms
        }


@property
def device_info(self):
    return {
        "identifiers": {("kwb_tcp", "kwb_tcp_device")},
        "name": "KWB TCP Heizung",
        "manufacturer": "KWB",
        "model": "Modbus TCP"
    }

    def update(self):
        from pymodbus.client import ModbusTcpClient
        import logging
        _LOGGER = logging.getLogger(__name__)
        alarm_texts = {"0": "Die Regelung ist nicht vollst\u00e4ndig eingestellt!", "1": "Speicherbaustein ist defekt!", "2": "Elektronischer Defekt an den digitalen Eing\u00e4ngen!", "3": "Die Uhrzeit muss neu eingestellt werden!", "4": "Das Wartungsintervall ist abgelaufen. Verst\u00e4ndigen Sie den Kundendienst!", "5": "Sicherheitsthermostat! \u00dcberhitzung des Kessels!", "6": "Hauptantriebsmotor ist \u00fcberhitzt!", "7": "Die Z\u00fcndung funktioniert nicht!", "8": "Der Brennstoffbunker ist leer! Bitte nachf\u00fcllen!", "9": "Defekter Triac bei Hauptantrieb oder Raumaustragungsantrieb!", "10": "Die R\u00fccklaufanhebung funktioniert nicht!", "11": "Raumaustragungsmotor 1 ist \u00fcberhitzt!", "12": "Brandschutzklappe \u00f6ffnet nicht!", "13": "Temperaturanstieg im Brennstoffvorrat. Feueralarm!", "14": "Die Elektronik hat 70\u00b0C!", "15": "Der Rauchgasf\u00fchler fehlt oder ist defekt!", "16": "Der R\u00fccklauff\u00fchler fehlt oder ist defekt!", "17": "Der Kesself\u00fchler fehlt oder ist defekt!", "18": "Brandschutzklappe schlie\u00dft nicht!", "19": "Der Wasserbeh\u00e4lter der Notl\u00f6scheinrichtung ist leer! Bedienungsanleitung beachten.", "20": "Die Glutbettf\u00fchlerelektronik ist defekt!", "21": "Die Glutbettf\u00fchlerelektronik ist falsch montiert!", "22": "Hauptantriebsmotor ist \u00fcberlastet!", "23": "Der Brennstoffbeh\u00e4lter ist leer. Bitte nachf\u00fcllen!", "24": "Der \u00dcberf\u00fcllschutzschalter der Raumaustragung 1 ist offen!", "25": "Der Raumaustragungsmotor 1 ist \u00fcberlastet!", "26": "Ein Motor der Zusatzraumaustragung ist \u00fcberlastet!", "27": "Ein Motor der Zusatzraumaustragung ist \u00fcberhitzt!", "28": "Ein \u00dcberf\u00fcllschutzschalter der Zusatzraumaustragung ist offen!", "29": "Der Deckel vom Aschebeh\u00e4lter ist offen!", "186": "Netzwerkfehler am Kesselmodul!", "187": "Netzwerkfehler am Kesselmodul 2!", "238": "Fehler im Heizkreisnetz!", "239": "Der Kesself\u00fchler am Zweitkessel fehlt oder ist defekt!", "240": "Der Unterdruck im Brennraum kann nicht geregelt werden!", "241": "Der Unterdrucksensor ist defekt!", "242": "Der Sauerstoffsensor fehlt oder ist defekt!", "243": "Temperaturanstieg im Aschebeh\u00e4lter!", "244": "Kalibrierungsfehler der Lambdasonde.", "245": "Die Versorgung am Raumaustragungsmodul ist unterbrochen!", "246": "Defekter Triac am Raumaustragungsmodul!", "247": "Netzwerkfehler am Raumaustragungsmodul!", "248": "Das Kontrollintervall istabgelaufen.", "249": "Die Kaminkehrerfunktion ist aktiv", "250": "Platinenrevision und Anlagennummer sind nicht kompatibel", "251": "Der Not Ausschalter ist gedr\u00fcckt!", "252": "Konfigurationsfehler! Letzte Sicherung aktiviert!", "253": "Unterschreitung der Puffertemperatur", "254": "Der Saugbeh\u00e4lter ist leer!", "255": "Fehler GSM Modul!"}
        addresses = [2315, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323, 2324, 2325, 2326, 2327, 2328, 2329, 2330]
        try:
            client = ModbusTcpClient(self._host, port=self._port)
            client.connect()
            result_texts = []
            for i, addr in enumerate(addresses):
                result = client.read_holding_registers(address=addr, count=1)
                if not result.isError():
                    val = result.registers[0]
                    for bit in range(16):
                        if val & (1 << bit):
                            alarm_id = i * 16 + bit
                            txt = alarm_texts.get(str(alarm_id), f"Alarm {alarm_id}")
                            result_texts.append(f"{alarm_id}: {txt}")
            self._active_alarms = result_texts
            client.close()
        except Exception as e:
            _LOGGER.error(f"[Alarme] Modbus-Fehler: {e}")
            self._active_alarms = []
