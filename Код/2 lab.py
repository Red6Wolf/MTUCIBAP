ip_list=[
    '10.1.1.1',
    '10.1.1.2',
    '10.1.1.3',
    '10.1.1.4',
    '10.1.1.5'
]

#1
print("Задание 1")
print("Первый элемент:", ip_list[0])
print("Последний элемент:", ip_list[-1])

#2
print("Задание 2") 
ip_list.append('10.1.1.6') 
ip_list.extend(['10.1.1.55', '10.1.1.66'])  

new_ip = ["172.16.1.1", "172.16.1.2", "172.16.1.3"]  
ip_list += new_ip  
print(ip_list)  

print("Второй элемент", ip_list[1])  
print("Предпоследний элемент", ip_list[-2]) 

ip_list.pop(0) 
ip_list.pop(-1)  

ip_list[0] = '2.2.2.2'  
print("Первый обновленный", ip_list[0])  
print("Новый обновленный", ip_list)  


#3
print("Задание 3")  
import random  

acl_list = [random.randint(1, 119) for i in range(10)] 
print("Сгенерированый список", acl_list) 

acl_list.sort()  # Сортировка списка.
print("Отсортированный список", acl_list) 

first_element = acl_list.pop(0)  
last_element = acl_list.pop(-1)  
acl_list.insert(0, last_element) 
acl_list.append(first_element)  
print("С заменой первого и последнего эллемента", acl_list) 

acl_list.reverse() 
print("Список после реверса .reverse", acl_list)  

acl_list = acl_list[::-1]  
print("Реверс при помощи среза", acl_list) 

mid_index = len(acl_list) // 2  

acl_list1 = acl_list[:mid_index]  
acl_list2 = acl_list[mid_index:]  
print('Первая половина списка', acl_list1)  
print('Вторая половина списка', acl_list2)  

#4
print('Задание 4')  
user_input = input('Введите данные:') 
list3 = [user_input]  
print(list3)  

len_list3 = len(list3)  
x = '1'  #
count_x = sum(item.count(x) for item in list3)  
print('Длинна списка', len_list3) 
print('Сколько 1 в списке:', count_x)  

#Задание 5
print('Задание 5')  
ip_list = [  
    '10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.2',
    '10.1.1.3', '10.1.1.1', '10.1.1.1', '10.1.1.2'
]

ip_addr_unique = set(ip_list)  
print('Уникальные ip-адреса:', ip_addr_unique) 

ip_sorted = sorted(ip_addr_unique)  
print('Отсортированный список уникалов', ip_sorted)  

len_iplist = len(ip_addr_unique) 
print('Количество уникальных ip адресов', len_iplist)  
#6
print("Задание 6")  

import random 

vlan_mos = [random.randint(1, 10) for i in range(8)]
vlan_kursk = [random.randint(1, 15) for i in range(10)]
vlan_novosib = [random.randint(1, 20) for i in range(15)]

print("Созданные списки VLAN:",
      "\nМосква:", vlan_mos,
      "\nКурск:", vlan_kursk,
      "\nНовосибирск:", vlan_novosib)

unique_vlans_mos = len(set(vlan_mos))
print("Количество уникальных VLAN в Москве:", unique_vlans_mos)

set_vlan_mos = set(vlan_mos)
set_vlan_kursk = set(vlan_kursk)
set_vlan_novosib = set(vlan_novosib)

print("Множество VLAN Москвы:", set_vlan_mos)
print("Множество VLAN Курска:", set_vlan_kursk)
print("Множество VLAN Новосибирска:", set_vlan_novosib)

common_vlans_mos_kursk = set_vlan_mos.intersection(set_vlan_kursk)
print("Общие VLAN между Москвой и Курском:", common_vlans_mos_kursk)

common_vlans_all = set_vlan_mos.intersection(set_vlan_kursk, set_vlan_novosib)
print("Общие VLAN во всех трех городах:", common_vlans_all)

unique_vlans_novosib = set_vlan_novosib - set_vlan_mos.union(set_vlan_kursk)
print("Уникальные VLAN в Новосибирске:", unique_vlans_novosib)

# Задание 7
print('Задание 7')  

device = {  
    'ip': '10.10.10.12', 
    'username': 'user',  
    'password': 'pass',  
}

print('Пароль устройства:', device['password']) 

device_key = list(device.keys()) 
device_value = list(device.values()) 

print('Ключи устройства:', device_key)  
print('Значения устройства:', device_value)

add_config = { 
    'device_type': 'huawei',  
    'session_log': 'output.txt',  
}

device.update(add_config) 
print('Обновленный словарь устройства:', device)  

# Задание 8
print('Задание 8')  

show_version = "   *0 CISCO881-SEC-K9 FTX0000038X   "  

show_version = show_version.strip()  

parts = show_version.split()  
model = parts[1]  
serial_number = parts[2] 

contains_cisco = 'cisco' in show_version.lower() .
contains_881 = '881' in model  

print(f"Серийный номер: {serial_number}, Модель устройства: {model}")

# Задание 9
print('Задание 9')  

mac1 = "Internet 10.220.88.29 94 5254.abbe.5b7b ARPA FastEthernet4"
mac2 = "Internet 10.220.88.30 3 5254.ab71.e119 ARPA FastEthernet4"
mac3 = "Internet 10.220.88.32 231 5254.abc7.26aa ARPA FastEthernet4"

def extract_mac_ip(mac_entry):
    parts = mac_entry.split()  
    ip_address = parts[1] 
    mac_address = parts[3]  
    return ip_address, mac_address  

print(f"{'IP Address':<20} {'MAC Address':<20}")
print("-" * 40) 


for mac in [mac1, mac2, mac3]:  
    ip, mac_addr = extract_mac_ip(mac)  
    print(f"{ip:<20} {mac_addr:<20}")  

# Задание 10
print('Задание 10')  

ip_input = input("Введите IP-адрес: ")  

octets = ip_input.split('.')  

for i, octet in enumerate(octets, start=1):  
    decimal_value = int(octet)  
    binary_value = bin(decimal_value)[2:]  
    hex_value = hex(decimal_value)  
    print(f"Octet {i}: {decimal_value} (Decimal), 0b{binary_value} (Binary), {hex_value} (Hexadecimal)")
