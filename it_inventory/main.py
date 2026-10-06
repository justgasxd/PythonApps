from devices import (
    add_device, show_devices, delete_device,
    edit_device, search_device, show_statistics,
    search_by_manufacturer, show_devices_by_room,
    most_common_manufacturers, change_status, search_menu
    )

def main():
    while True:
        print('\nIT SEADMETE INVENTUUR')
        print('---------------------')
        print('1.   Lisa seade')
        print('2.   Näita seadmeid')
        print('3.   Kustuta seade') # Kustuta
        print('4.   Muuda seadet') # Muuda
        print('5.   Otsi seadet') # Otsi
        print('6.   Statistika') # Statistika)
        print('7.   Näita Kõige sagedamini esinev tootja')
        print('8.   Vaheta staatus')
        print('0.   Välju')

        choice = input('Vali tegevus: ')

        if choice == '1':
            add_device()
        elif choice == '2':
            show_devices()
        elif choice == '3': # Kustuta
            delete_device()
        elif choice == '4': # Muuda
            edit_device()
        elif choice == '5': # Otsi
            search_menu()
        elif choice == '6': # Statistika
            show_devices_by_room()
        elif choice == '7':
            most_common_manufacturers()
        elif choice == '8':
            change_status()
        elif choice == '0':
            print('Programm lõpetas töö')
            break
        else:
            print('Vale valik!')


if __name__ == '__main__':
    main()
    