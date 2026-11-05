import random

choices = ["kivi", "paber", "käärid"]
name = input("Sisesta oma nimi: ")

while True:
    # --- Statistika ---
    player_wins = 0
    computer_wins = 0
    last = ""
    total = 0

    try:
        fail = open("rps_results.csv", "r", encoding="utf-8")
        for rida in fail:
            osad = rida.strip().split(",")
            if osad[0] == name:
                last = rida.strip()
            if int(osad[1]) > int(osad[2]):
                player_wins += 1
            else:
                computer_wins += 1
            total += 1
        fail.close()
    except FileNotFoundError:
        pass

    print("Mänge kokku:", total)
    print("Mängija võite:", player_wins, "Arvuti võite:", computer_wins)
    if last != "":
        print("Sinu viimane mäng:", last)

    # --- Mäng ---
    player = 0
    computer = 0
    voorud = 0

    while voorud < 5:
        choice = input("Vali kivi, paber või käärid: ")
        if choice not in choices:
            print("Vigane valik!")
            continue

        computer_choice = random.choice(choices)

        if choice == computer_choice:
            print("Sina:", choice + ". Arvuti:", computer_choice + ". Viik, mängime uuesti.")
            continue

        voorud += 1

        if (choice == "kivi" and computer_choice == "käärid") or \
           (choice == "paber" and computer_choice == "kivi") or \
           (choice == "käärid" and computer_choice == "paber"):
            player += 1
            print("Sina:", choice + ". Arvuti:", computer_choice + ". Vooru võitsid sina!", end=" ")
        else:
            arvuti += 1
            print("Sina:", choice + ". Arvuti:", computer_choice + ". Vooru võitis arvuti!", end=" ")
        print("Seis: sina", player, ", arvuti", computer)

    # --- Tulemus ---
    if player > computer:
        winner = name
    else:
        winner = "Arvuti"

    print("Mäng läbi! Sina:", player, "Arvuti:", computer, "Võitja:", winner)

    # --- Salvestame faili (lisame lõppu) ---
    file = open("rps_results.csv", "a", encoding="utf-8")
    file.write(name + "," + str(player) + "," + str(computer) + "," + winner + "\n")
    file.close()

    # --- Uus mäng? ---
    vastus = input("Kas soovid uut mängu? (jah/ei): ")
    if vastus != "jah":
        break