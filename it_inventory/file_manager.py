# file_manager.py
FILE_NAME = 'devices.csv'

def read_devices():
    """Loeb andmid failid"""

    devices = []

    try:
        with open(FILE_NAME, 'r', encoding='-utf8') as f:
            for line in f:
                data = line.strip().split(';')
                devices.append(data)
    except FileNotFoundError:
        pass

    return devices


def add_device_to_file(device):
    """Lisab seadme faili"""
    with open(FILE_NAME, 'a', encoding='utf-8') as f:
        f.write(';'.join(device) + '\n')



def write_devices(devices):
    """Kirjutab seadmed faili"""

    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        for device in devices:
            f.write(';'.join(device) + '\n')