# main.py
from devices import add_device, show_devices, delete_device, edit_device, search_device

while True: 
    print('\nIT SEADMETE INVENTUUR')
    print('---------------------')
    print('1.  Lisa seade')
    print('2.  Näita seadmeid')
    print('3.  Kustuta seade') # Kustuta
    print('4.  Muuda seadet')
    print('5.  Otsi seade') # Muuda
    print('0.  Välju')

    choice = input('Vali tegevus: ')

    if choice == "1": # Lisab
        add_device()
    elif choice == "2": # Näitab
        show_devices()
    elif choice == "3": # Kustutab
        delete_device()
    elif choice == "4": # Muudab
        edit_device()
    elif choice == "5": # Otsib
        search_device()
    elif choice == "0": # Lõpetab
        print('Programm lõpetas töö')
        break
    else:
        print('Vale valik!')


    
