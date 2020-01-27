# Subnet Calculator App:
# TODO Fix the issue with Class A and Class B networks (to increment other octets, when the last octet has reached 255)
# TODO Better comments and documentation


def convert_to_decimal(x):
    #TODO Optimize if 0 is reached before the last bit, or if octet = 0:
    # x = 192           #Bit value
    first_num = 0       #128
    second_num = 0      #64
    third_num = 0       #32
    fourth_num = 0      #16
    fifth_num = 0       #8
    sixth_num = 0       #4
    seventh_num = 0     #2
    eight_num = 0       #1
    if x - 128 >= 0:
        first_num = 1
        x -= 128
    if x - 64 >= 0:
        second_num = 1
        x -= 64
    if x - 32 >= 0:
        third_num = 1
        x -= 32
    if x - 16 >= 0:
        fourth_num = 1
        x -= 16
    if x - 8 >= 0:
        fifth_num = 1
        x -= 8
    if x - 4 >= 0:
        x -= 4
        sixth_num = 1
    if x - 2 >= 0:
        seventh_num = 1
        x -= 2
    if x - 1 >= 0:
        eight_num = 1

    return (str(first_num) + str(second_num) + str(third_num) + str(fourth_num) + str(fifth_num) + str(sixth_num)
            + str(seventh_num) + str(eight_num))


ip_addr = input()               # 192.168.0.1
mask = int(input())             # 24
#include_decimal = bool(input())
wildcard_mask = ""
network_addr = ""
broadcast_addr = ""
#host_min = ""
#host_max = ""
#total_hosts = 0
# power_var is used to calculate the total usable host addresses in a subnet
#power_var = 0




# Split IP Address in octets
ip_address = ip_addr.split(sep='.')
first_octet = int(ip_address[0])
second_octet = int(ip_address[1])
third_octet = int(ip_address[2])
fourth_octet = int(ip_address[3])
# Check type:
print(type(first_octet))
# Print octets - TESTING
print("TEST OUTPUT FOR OCTETS")
print(first_octet)
print(second_octet)
print(third_octet)
print(fourth_octet)
print("TEST OUTPUT over")
print()


# Deal with Subnet Mask
# if
print("IP Address:")
print(ip_addr)
print(f"Subnet mask:")
print(f"DECIMAL REPRESENTATION - /{mask}")

#



# WILDCARD MASK = 255.255.255.255 - subnet mask
# /30 example:
# Mask = 255.255.255.252
# Wildcard = 0.0.0.3


# Printing Decimal representation:
print("Decimal representation:")
print(convert_to_decimal(first_octet), end=".")
print(convert_to_decimal(second_octet), end=".")
print(convert_to_decimal(third_octet), end=".")
print(convert_to_decimal(fourth_octet))




# Calculate total usable host addresses:
power_var = 32 - mask                   # variable to get the power used to calculate the total and usable addresses
# first_host_addresses = 2 ** power_var - tova go vadim ot 256
total_hosts = 2 ** power_var            # total addresses in a subnet
usable_hosts = total_hosts - 2          # usable host addresses in the subnet



# Calculate network address and available subnets:
# We create a list with all available network addresses
network_address_list = []               # a list of all network/subnet IDs is defined if it's needed for future use
for i in range(0, 255, total_hosts):
    network_address_list.append(i)

print(network_address_list)
max_subnets = len(network_address_list)
print(f"max subnets: {max_subnets}")
#print(network_address_list)


# Find the network address from the network_address_list
for each_address in network_address_list:
    if fourth_octet >= each_address:
        network_addr = str(first_octet) + '.' + str(second_octet) + '.' + str(third_octet) + '.' + str(each_address)
    else:
        break



# Get First Host, Last Host and Broadcast Addresses:
host_min = str(first_octet) + '.' + str(second_octet) + '.' + str(third_octet) + '.' + str(each_address + 1)
host_max = str(first_octet) + '.' + str(second_octet) + '.' + str(third_octet) + '.' + str(each_address + usable_hosts)
broadcast_addr = str(first_octet) + '.' + str(second_octet) + '.' + str(third_octet) + '.' \
                 + str(each_address + usable_hosts + 1)



# PRINT RESULTS:

print(f"Network Address: {network_addr}")
print(f"First host: {host_min}")
print(f"Last host: {host_max}")
print(f"Broadcast Addr: {broadcast_addr}")
print(f"Usable hosts: {usable_hosts}")



#if include_decimal == "Yes":
    # Print decimal conversion from the IP address
#    print()






