# Задание 1
print('Задание 1')
with open("devices.txt", "r") as file:
    for line in file:
        print(line.strip())
# Задание 2
print('Задание 2')
with open("devices.txt", "r") as file:
    for line in file:
        if line.strip():
            print(line.strip())
# Задание 3
print('Задание 3')
list_devices = []
with open("devices.txt", "r") as file:
    for line in file:
        list_devices.append(line.strip())
print(list_devices)

# Задание 4
print('Задание 4')
with open("devices.txt", "r+") as file:
    content = file.readlines()
    file.seek(0)
    file.write("New start line\n")
    file.writelines(content)
    file.write("\nNew end line\n")
with open("devices.txt", "r") as file:
    print(file.read())

# Задание 5
print('Задание 5')
vlan_data = []
with open("show_vlan.txt", "r") as file:
    for line in file:
        if "VLAN" in line:
            parts = line.split()
            vlan_data.append((parts[0], parts[1]))
print(vlan_data)

# Задание 6
print('Задание 6')
with open("show_arp.txt", "r") as file:
    for line in file:
        parts = line.split()  
    
        if len(parts) >= 4:
            ip_addr = parts[1]  
            mac_addr = parts[3] 
            print(f"IP: {ip_addr}, MAC: {mac_addr}")


print('Задание 7')

with open("show_arp.txt", "r") as file:
    for line in file: 
        parts = line.split()  
        if len(parts) >= 4:
            ip_addr = parts[1] 
            mac_addr = parts[3]  
            if ip_addr == "10.220.88.1":
                print(f"IP/MAC шлюза по умолчанию: IP = {ip_addr}, MAC = {mac_addr}")
                break  
            if ip_addr == "10.220.88.30":
                print(f"Arista 3 IP/MAC is: IP = {ip_addr}, MAC = {mac_addr}")
                break 
print('Задание 8')
with open("show_lldp_neighbors_detail.txt", "r") as file:
    for line in file:  
        if "System Name" in line: 
            system_name = line.split(":")[1].strip() 
        if "Port id" in line:  
            port_id = line.split(":")[1].strip()  
        if "System Name" in line and "Port id" in line:  
            break  
print(f"Имя системы: {system_name}, ID Порта: {port_id}")

# Задание 9
print('Задание 9')
import json
from pprint import pprint

with open("interface-config.json", "r") as file:
    json_text = file.read()  

print(f"Тип переменной json_text: {type(json_text)}")

print("Содержимое json_text:")
print(json_text)

json_data = json.loads(json_text)

print(f"\nТип переменной json_data: {type(json_data)}")

print("\nСодержимое json_data:")
pprint(json_data)

# Задание 10
print('Задание 10')
import json
from pprint import pprint

with open("interfaces.json", "r") as file:
    json_data = json.load(file)  

if "ietf-interfaces:interfaces" in json_data:
    interfaces = json_data["ietf-interfaces:interfaces"].get("interface", [])
    
    for interface in interfaces:
        name = interface.get("name", "N/A") 
        ipv4 = interface.get("ietf-ip:ipv4", {}).get("address", [{}])  
        ip = ipv4[0].get("ip", "N/A") 
        netmask = ipv4[0].get("netmask", "N/A")  
        print(f"Интерфейс: {name}, IP-адрес: {ip}, Маска: {netmask}")
else:
    print("Ключ 'ietf-interfaces:interfaces' отсутствует в JSON.")

#Задание 11
print('Задание 11')
import json
from pprint import pprint  

with open("interfaces.json", "r") as file:
    json_data = json.load(file)  

if "ietf-interfaces:interfaces" in json_data:
    interfaces = json_data["ietf-interfaces:interfaces"].get("interface", [])

    pprint(interfaces) 
else:
    print("Ключ 'ietf-interfaces:interfaces' отсутствует в JSON.")
    
#Задание 12
print('Задание 12')
import yaml 

with open("yaml_int1.yml", "r") as file: 
    yaml_data = yaml.safe_load(file)  
print(yaml_data)  

#Задание 13
print('Задание 13')
import yaml
from pprint import pprint

with open("lab11_2_yaml.yml", "r") as file:
    data = yaml.safe_load(file)

print("Результат с использованием print:")
print(data)

print("\nРезультат с использованием pprint:")
pprint(data)