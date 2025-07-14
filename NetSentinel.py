import subprocess

def banner():
    print("""
===========================================
|         Cyber Automation CLI Tool       |
|             by NetSentinel              |
|       ⚠️ Authorized Use Only ⚠️        |
===========================================
""")

def menu():
    print("""
[1] Scan local network (ping sweep)
[2] Launch Metasploit
[3] Launch SQLMap (guided)
[4] Launch Burp Suite
[5] Launch Airgeddon
[6] Launch Hashcat (guided)
[7] Launch Medusa (guided)
[8] Launch Modbus Client (guided)
[9] Exit
""")

def scan_local_network():
    subnet = input("Enter subnet (e.g., 192.168.1.0/24): ")
    subprocess.call(f"nmap -sn {subnet}", shell=True)

def launch_metasploit():
    subprocess.call("msfconsole", shell=True)

def launch_sqlmap():
    url = input("Target URL: ")
    cookies = input("Cookies (optional): ")
    params = input("Parameters to test (e.g., id, user): ")
    level = input("Level (1-5): ")
    command = f"sqlmap -u \"{url}\""
    if cookies:
        command += f" --cookie=\"{cookies}\""
    command += f" -p {params} --level={level} --batch --dump"
    print(f"\nRunning command:\n{command}\n")
    subprocess.call(command, shell=True)

def launch_burp():
    subprocess.call("burpsuite", shell=True)

def launch_airgeddon():
    subprocess.call("airgeddon", shell=True)

def launch_hashcat():
    hash_file = input("Path to hash file: ")
    wordlist = input("Path to dictionary (wordlist): ")
    hash_mode = input("Hash type (0=MD5, 1000=NTLM, 1800=SHA512crypt, etc.): ")
    command = f"hashcat -m {hash_mode} {hash_file} {wordlist} --force"
    print(f"\nRunning command:\n{command}\n")
    subprocess.call(command, shell=True)

def launch_medusa():
    ip = input("Target IP: ")
    service = input("Service (e.g., ssh, ftp, http): ")
    user_list = input("Path to user list file: ")
    pass_list = input("Path to password list file: ")
    threads = input("Number of threads (default 4): ") or "4"
    command = f"medusa -h {ip} -U {user_list} -P {pass_list} -M {service} -t {threads}"
    print(f"\nRunning command:\n{command}\n")
    subprocess.call(command, shell=True)

def launch_modbus():
    ip = input("Modbus target IP: ")
    port = input("Port (default 502): ") or "502"
    unit_id = input("Unit ID (default 1): ") or "1"
    function = input("Function (e.g., read_coils, read_holding_registers): ")
    start = input("Starting address: ")
    count = input("Number of coils/registers: ")
    
    command = f"modbus-cli -t tcp -a {ip} -p {port} -u {unit_id} {function} {start} {count}"
    print(f"\nRunning command:\n{command}\n")
    subprocess.call(command, shell=True)

def main():
    while True:
        banner()
        menu()
        choice = input("Choose an option: ")

        if choice == '1':
            scan_local_network()
        elif choice == '2':
            launch_metasploit()
        elif choice == '3':
            launch_sqlmap()
        elif choice == '4':
            launch_burp()
        elif choice == '5':
            launch_airgeddon()
        elif choice == '6':
            launch_hashcat()
        elif choice == '7':
            launch_medusa()
        elif choice == '8':
            launch_modbus()
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
