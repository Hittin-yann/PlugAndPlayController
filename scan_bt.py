import bluetooth
import sys
import time
import threading

# Variable globale pour contrôler l'animation
stop_animation = False

def animate_text():
    i = 1
    while not stop_animation:  # Boucle pour l'animation
        sys.stdout.write(f"\r[*] Recherche des périphériques Bluetooth classiques{'.' * i}")
        sys.stdout.flush()
        time.sleep(0.5)

        i += 1
        if i > 3:  # Réinitialiser i pour garder l'animation dans un cycle de 1 à 3
            i = 1
            if not stop_animation:
                sys.stdout.write("\r\033[K")
                sys.stdout.flush()

try:
    while True:
        # Confirmation
        reponse = input("Souhaitez-vous lancer le scan Bluetooth ? (o/n) : ").strip().lower()
        if reponse != "o":
            print("Annulé par l'utilisateur.")
            exit()

        # Réinitialiser l'indicateur d'arrêt de l'animation
        stop_animation = False

        # Démarrer l'animation dans un thread séparé
        animation_thread = threading.Thread(target=animate_text)
        animation_thread.start()

        # Recherche des appareils Bluetooth
        devices = bluetooth.discover_devices(duration=8, lookup_names=True)

        # Arrêter l'animation
        stop_animation = True
        animation_thread.join()  # Attendre que le thread d'animation se termine
        print("\n")

        if not devices:
            print("Aucun périphérique détecté.")
        else:
            print(f"[+] {len(devices)} périphérique(s) détecté(s) :\n")
            for addr, name in devices:
                print(f" - Nom : {name}")
                print(f"   MAC : {addr}\n")

except KeyboardInterrupt:
    print("\nArrêt du scan.")