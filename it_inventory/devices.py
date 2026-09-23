# devices.py
def get_next_id():
    """Leiab järgmise seadme ID"""
    device_id = 1

    try:
        with open('devices.csv', 'r', encoding='utf-8') as f:
            for line in f: 
                data = line.strip().split(';')

                if data[0].isdigit():
                    device_id = int(data[0]) + 1
    except FileNotFoundError:
        pass

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

    with open('devices.csv', 'a', encoding='utf-8') as file:
        file.write(f'{device_id};{device_type};{manufacturer};{model};{room};{status}\n')


    print(f'Seade lisatud. ID: {device_id}')



def show_devices():

    """Kuvab kõik inventuuris olevad seadmed"""
    print('\nSEADMETE NIMEKIRI')
    print('-------------------')

    try: 
        with open('devices.csv', 'r', encoding='utf-8') as f:
            for line in f:
                data = line.strip().split(';')

                print(f'{" | ".join(data)}')
    except FileNotFoundError:
        print('Seadmeid pole veel lisatud.')

def delete_device():
    """Kustutab valitud seade inventuurist"""

    print('\nSEADME KUSTUTAMINE')
    print('-------------------')

    device_id = input('Sisesta seadme ID: ')

    lines = []
    found = False

    try:
        with open('devices.csv', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print('Seadmeid ei ole veel lisatud')
        return

    with open('devices.csv', 'w', encoding='utf-8') as f:
        for line in lines:
            data = line.strip().split(';')

            if data[0] == device_id:
                found = True
            else:
                f.write(line)
    if found:
        print('Seade kustutatud')
    else:
        print('Sellise ID-ga seadet ei leitud')


def edit_device():
    """Muudab valitud seadme andmeid."""

    print('\nSEADME ANDMETE MUUTMINE')
    print('-------------------------')

    found = False
    device_id = input('Sisesta seadme ID: ')

    try:
        with open('devices.csv', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print('Seadmeid ei ole veel lisatud')
        return

    with open('devices.csv', 'w', encoding='utf-8') as f:
        for line in lines:
            data = line.strip().split(';')
            if data[0] == device_id:
                found = True

                device_type = input(f'Seadme tüüp [{data[1]}]: ')
                manufacturer = input(f'Tootja [{data[2]}]: ')
                model = input(f'Mudel [{data[3]}]: ')
                room = input(f'Ruum [{data[4]}]: ')
                status = input(f'Staatus [{data[5]}]: ')

                if device_type == '':
                    device_type = data[1]
                if manufacturer == '':
                    manufacturer = data[2]
                if model == '':
                    model = data[3]
                if room == '':
                    room = data[4]
                if status == '':
                    status = data[5]

                f.write(f'{device_id};{device_type};{manufacturer};{model};{room};{status}\n')
            else:
                f.write(line)
    if found:
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
                    