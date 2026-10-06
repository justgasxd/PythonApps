# devices.py
from file_manager import (
    read_devices, add_device_to_file, write_devices
    )

def get_next_id():
    """Leiab järgmise seadme ID."""

    device_id = 1
    devices = read_devices()
    for data in devices:
        if data[0].isdigit():
            device_id = int(data[0]) + 1

    return device_id


def add_device():
    """Lisab uue seadme inventuuri."""

    device_id = get_next_id()

    print("\nUUE SEADME LISAMINE")
    print("---------------------")

    device_type = input("Seadme tüüp: ")

    if device_type == '':
        print("Seadme tüüp peab olema sisestatud.")
        return
    
    manufacturer = input("Tootja: ")
    model = input("Mudel: ")
    room = input("Ruum: ")
    status = "Töökorras"

    device = [
        str(device_id),
        device_type,
        manufacturer,
        model,
        room,
        status
    ]

    add_device_to_file(device)

    print(f"Seade lisatud. ID: {device_id}")


def show_devices():
    """Kuvab kõik inventuuris olevad seadmed."""

    print("\nSEADMETE NIMEKIRI")
    print("-------------------")

    devices = read_devices()

    if not devices:
        print('Seadmeid pole veel lisatud.')
        return

    print("\nSorteeri seadmed:")
    print("1. Tootja järgi")
    print("2. Ruumi järgi")

    choice = input("Tee valik: ")

    if choice == "1":
        devices = sorted(devices, key=lambda device: device[2])
    elif choice == "2":
        devices = sorted(devices, key=lambda device: device[4])
    else:
        print("Vigane valik.")
        return

    number = 1

    for device in devices:
        print(f'{number}. {" | ".join(device)}')
        number = number + 1



def delete_device():
    """Kustutab valitud seadme inventuurist"""

    print("\nSEADME KUSTUTAMINE")
    print("--------------------")

    devices = read_devices()

    if not devices:
        print("Seadmeid pole veel lisatud.")
        return

    device_id = input("Sisesta seadme ID: ")

    new_devices = []
    found_device = None

    for device in devices:
        if device[0] == device_id:
            found_device = device
        else:
            new_devices.append(device)

    if found_device:
        print("Leitud seade:")
        print(" | ".join(found_device))

        confirmation = input("Kas soovid seadme kustutada? (j/e): ")

        if confirmation == "j":
            write_devices(new_devices)
            print("Seade on kustutatud")
        elif confirmation == "e":
            print("Seadet ei kustutatud.")
    else:
        print("Sellise ID-ga seadet ei leitud.")

def edit_device():
    """Muudab valitud seadme andmeid."""

    print("\nSEADME ANDMETE MUUTMINE")
    print("-------------------------")

    devices = read_devices()

    if not devices:
        print("Seadmeid pole veel lisatud.")
        return

    found = False
    device_id = input("Sisesta seadme ID: ")
    devices = read_devices()

    for data in devices:        
        if data[0] == device_id:
            found = True

            device_type = input(f"Seadme tüüp [{data[1]}]: ")
            manufacturer = input(f"Tootja [{data[2]}]: ")
            model = input(f"Mudel [{data[3]}]: ")
            room = input(f"Ruum [{data[4]}]: ")

            if device_type != "":
                data[1] = device_type
            if manufacturer != "":
                data[2] = manufacturer
            if model != "":
                data[3] = model
            if room != "":
                data[4] = room
                
            print('Vali uus staatus: ')
            print('1. Töökorras ')
            print('2. Katki')

            new_status = input('Sisesta uus staatus: ')

            if new_status == '1':
                data[5] = 'Töökorras'
            elif new_status == '2':
                data[5] = 'Katki'

    if found:
        write_devices(devices)
        print("Seadme andmed muudetud.")
    else:
        print("Sellise ID-ga seadet ei leitud.")


def search_device():
    """Otsib inventuurist seadmeid kasutaja sisestatud otsingu järgi"""

    print("\nSEADME OTSIMINE")
    print("-----------------")

    devices = read_devices()

    if not devices:
        print('Seadmeid pole veel lisatud.')
        return

    search = input('Sisesta otsing: ')

    if len(search) <= 2:
        print('Otsingu fraas on lühike.')
        return

    search = search.lower()
    found = False
    count = 0

    with open('devices.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if search in line.lower():
                print(line.strip())
                found = True
                count += 1

    if found:
        print(f'Leitud seadmeid: {count}')
    else:
        print('Seadet ei leitud.')

def search_menu():
    """Otsinug alammenüü"""
    
    while True:
        print('\nOTSING')
        print('--------')
        print('1.   Üldotsing')
        print('2.   Otsi tootja järgi')
        print('3.   Otsi ruumi järgi')
        print('0.   Mine tagasi')
        choice = input('Tee valik: ')
        if choice == '1':
            search_device()
        elif choice == '2':
            search_by_manufacturer()
        elif choice == '3':
            show_devices_by_room()
        elif choice == '0':
            return
        else:
            print('Vigane valik.')

        
def show_statistics():
    """Kuvab inventuuris olevate seadmete statistikat."""

    print('\nSTATISTIKA')
    print('------------')

    devices = read_devices()

    if not devices:
        print("Seadmeid pole veel lisatud.")
        return

    total = 0 # Kokku
    working = 0 # Töökorras
    broken = 0 # Katkti

    devices = read_devices()

    for device in devices:
        total += 1

        if device[5].lower() == 'töökorras':
            working += 1
        elif device[5].lower() == 'katki':
            broken += 1

    working_protsent = working / total * 100
    broken_protsent = broken / total * 100

    print(f'Seadmeid kokku  {total}')
    print(f'Tööorras        {working}')
    print(f'Katkised        {broken}')

    print('\n')

    print(f'Töökorras: {working_protsent}%')
    print(f'Katki: {broken_protsent}%')

def search_by_manufacturer():
    """Otsib inventuurist seadmeid tootja järgi."""

    print('\nSEADME OTSIMINE TOOTJA JÄRGI')
    print('-----------------------------')

    devices = read_devices()

    if not devices:
        print('Seadmeid pole veel lisatud.')
        return

    manufacturer = input('Sisesta tootja: ')

    if manufacturer == '':
        print('Tootja peab olema sisestatud.')
        return

    found = False

    for device in devices:
        if device[2].lower() == manufacturer.lower():
            print(" | ".join(device))
            found = True

    if not found:
        print('Selle tootja seadmeid ei leitud.')

def show_devices_by_room():
    """Kuvab inventuuris olevad seadmed ruumide kaupa."""

    print('\nSEADMETE NIMEKIRI RUUMIDE KAUPA')
    print('-------------------------------')

    devices = read_devices()

    if not devices:
        print('Seadmeid pole veel lisatud.')
        return

    room = input('Sisesta ruum: ')
    found = False

    for device in devices:
        if device[4].lower() == room.lower():
            print(' | '.join(device))
            found = True

    if not found:
        print('Selles ruumis seadmeid ei ole.')


def most_common_manufacturers():
    devices = read_devices()

    if not devices:
        print('Seadmeid pole veel lisatud.')
        return

    manufacturers = {}

    for device in devices:
        manufacturer = device[1]

        if manufacturer in manufacturers:
            manufacturers[manufacturer] += 1
        else:
            manufacturers[manufacturer] = 1

    most_common = max(manufacturers, key=manufacturers.get)
    count = manufacturers[most_common]

    print('Kõige rohkem seadmeid:')
    print(f'{most_common} - {count} seadet')


def change_status():
    devices = read_devices()
    
    if not devices:
        print('Seadmeid pole veel lisatud')
        return

    device_id = input("Sisesta seadme ID: ")

    for device in devices:
        if str(device[0]) == device_id:
            print(f"Seade: {device[1]}")
            print(f"Praegune staatus: {device[5]}")

            print("Vali uus staatus:")
            print("1. Töökorras")
            print("2. Katki")

            choice = input("Valik: ")

            if choice == "1":
                device[5] = "Töökorras"
            elif choice == "2":
                device[5] = "Katki"
            else:
                print("Vale valik.")
                return

            write_devices(devices)
            print("Staatus muudetud.")
            return

    print("Sellise ID-ga seadet ei leitud.")

    
