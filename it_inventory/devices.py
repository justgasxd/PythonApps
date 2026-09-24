# devices.py
from file_manager import read_devices, add_device_to_file, write_devices

def get_next_id():
    """Leiab järgmise seadme ID"""
    device_id = 1
    devices = read_devices()
    for data in devices:
        if data[0].isdigit():
            device_id = int(data[0]) + 1

    return device_id


def add_device():
    """Lisab uue seadme inventuuri"""

    device_id = get_next_id()

    print('\nUUE SEADME LISAMINE')
    print('---------------------')

    device_type = input('Seadme tüüp: ')
    manufacturer = input('Tootja: ')
    model = input('Mudel: ')
    room = input('Ruum: ')
    status = 'Töökorras'

    device = [str(device_id),device_type,manufacturer,model,room,status]
    add_device_to_file(device)

    print(f'Seade lisatud. ID: {device_id}')



def show_devices():

    """Kuvab kõik inventuuris olevad seadmed"""
    print('\nSEADMETE NIMEKIRI')
    print('-------------------')

    devices = read_devices()

    if not devices:
        print('Seadmeid pole veel lisatud.')
        return

    for device in devices:
        print(' | '.join(device))

def delete_device():
    """Kustutab valitud seade inventuurist"""

    print('\nSEADME KUSTUTAMINE')
    print('-------------------')

    device_id = input('Sisesta seadme ID: ')

    devices = read_devices()
    new_devices = []
    found = False

    for device in devices:
        if device[0] == device_id:
            found = True
        else:
            new_devices.append(device)

    if found:
        write_devices(new_devices)
        print('Seade on kustutatud')
    else:
        print('Sellise ID-ga seadet ei leitud')



def edit_device():
    """Muudab valitud seadme andmeid."""

    print('\nSEADME ANDMETE MUUTMINE')
    print('-------------------------')

    found = False
    device_id = input('Sisesta seadme ID: ')
    devices = read_devices()

    for data in devices:
        if data[0] == device_id:
            found = True

            device_type = input(f'Seadme tüüp [{data[1]}]: ')
            manufacturer = input(f'Tootja [{data[2]}]: ')
            model = input(f'Mudel [{data[3]}]: ')
            room = input(f'Ruum [{data[4]}]: ')
            status = input(f'Staatus [{data[5]}]: ')

            if device_type != '':
                data[1] = device_type
            if manufacturer != '':
                data[2] = manufacturer
            if model != '':
                data[3] = model
            if room != '':
                data[4] = room
            if status != '':
                data[5] = status

                
    if found:
        write_devices(devices)
        print('Seadme andmed muudetud.')
    else:
        print('Sellise ID-ga seadet ei leitud.')

def search_device():
    """Otsib invetnuuris seadmeid kasutaja sisestatud otsingu järgi"""

    print('\nSEADME OTSIMINE')
    print('-----------------')

    search = input('Sisesta otsing: ')
    #kontrolli otsingu pikkust
    if len(search) <= 2: # 3+ otsib
        return

    search = search.lower()
    found = False

    try:
        with open('devices.csv', 'r', encoding='utf-8') as f:
            for line in f:
                if search in line.lower():
                    print(line.strip()) # Rida failis ilma reavahetuseta
                    found = True
                    
        if not found:
            print('Seadet ei leitud.')
    except FileNotFoundError:
        print('Seadmeid pole veel lisatud')
                    