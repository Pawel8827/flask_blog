from datetime import datetime
import socket, ipaddress, shutil


now = datetime.now()
today = now.strftime("%Y-%m-%d-%H-%M-%S")
source = "signum_podpis"  #nazwa folderu który kopiujemy na dysk c komputera



# nazwy plików 
plik = open('Wszystkie urzadzenia sieci '+ today + '.txt', 'w', encoding= 'utf-8')
file_name = open('Status_operacji' + today + '.txt','w', encoding= 'utf-8')


class skan():
    def is_port_open(ip: str, port: int) -> bool:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0


    ports = [
        443,
        139
    ]

    for ip in ipaddress.ip_network('10.148.8.0/24'):
        print(f'Sprawdzam adres ip {ip}')
        for port in ports:
            if is_port_open(str(ip), port):
                if port == 139:
                    nazwa= socket.gethostbyaddr(str(ip))
                    plik.write(f'Adress IP: {ip} to komputer' + '\n') 
                    print(f'Adress IP: {ip} to komputer o nazwie {nazwa[0]} porcie: {port}')
                    destination = f"//{ip}/c$/{source}"
                    
                    try:
                        shutil.copytree(source, destination)
                        print("Zakończone powodzeniem.")
                        aaa =  "Zakończone powodzeniem."
                        
                    
                    # If source and destination are same
                    except shutil.SameFileError:
                        print("Source and destination represents the same file.")
                        aaa =  "Source and destination represents the same file."
                    
                    # If there is any permission issue
                    except PermissionError:
                        print("Permission denied.")
                        aaa =  "Permission denied."
                    
                    # For other errors
                    except:
                        print("Error occurred while copying file.")
                        aaa = "Error occurred while copying file."

                    file_name.write(f'Adress IP: {ip} to komputer {nazwa[0]}, status operacji: {aaa}' + '\n')                   
                elif port == 443:
                    plik.write(f'Adress IP: {ip} to drukarka' + '\n')
                    print(f'Adress IP: {ip} to drukarka: {port}')

                
skan()
