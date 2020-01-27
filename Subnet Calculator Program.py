# Subnet Calculator App:
# TODO Fix the issue with Class A and Class B networks (to increment other octets, when the last octet has reached 255)
# if last octet > 255 ---> last octet / 255
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
#wildcard_mask = ""
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
#print("IP Address:")
print(f"IP Address: {ip_addr}/{mask}")
#print(f"Subnet mask:")
# TODO Get the decimal form of the mask - Example: 24 -> 255.255.255.0
#print(f"DECIMAL REPRESENTATION - /{mask}")

# Get Decimal mask
# Giving all mask octets the max value of 255, then check where mask bits are taken from to see which octets to decrease
first_oct_m = 255
second_oct_m = 255
third_oct_m = 255
fourth_oct_m = 255
# target_oct - variable to get the mask value for a single octet if mask has variable subnet length
#target_oct = 0
mask_power_value = mask % 8
target_oct = 2 ** (8 - mask_power_value)


if mask >= 24:
    fourth_oct_m = 256 - target_oct
elif mask >= 16:
    third_oct_m = 256 - target_oct
    fourth_oct_m = 0
elif mask >= 8:
    second_oct_m = 256 - target_oct
    third_oct_m = 0
    fourth_oct_m = 0
elif mask < 8:
    # TODO: Add error handling
    print("Incorrect mask:")




#print("DECIMAL MASK:")
decimal_mask = str(first_oct_m) + '.' + str(second_oct_m) + '.' + str(third_oct_m) + '.' + str(fourth_oct_m)
print(f"MASK: {decimal_mask} - /{mask}")
#print(decimal_mask)

# TODO Get wildcard mask
# WILDCARD MASK = 255.255.255.255 - subnet mask
# /30 example:
# Mask = 255.255.255.252
# Wildcard = 0.0.0.3
wildcard_mask = str(255 - first_oct_m) + '.' + str(255 - second_oct_m) + '.' + str(255 - third_oct_m) + '.' \
                + str(255 - fourth_oct_m)

print(f"WILDCARD: {wildcard_mask}")


# Printing Decimal representation for the input IP ADDRESS:
#if include_decimal == "Yes":
    # Print decimal conversion from the IP address
#    print()

# TODO: Move this decimal stuff after each printed element (network address, first/last host address etc.
#  - use bool to ask if it is to be included
print("Decimal representation:")
print(convert_to_decimal(first_octet), end=".")
print(convert_to_decimal(second_octet), end=".")
print(convert_to_decimal(third_octet), end=".")
print(convert_to_decimal(fourth_octet))




# Calculate total usable host addresses:
power_var = 32 - mask                   # variable to get the power used to calculate the total and usable addresses
total_hosts = 2 ** power_var            # total addresses in a subnet
# usable host addresses in a subnet are the total addresses - network and broadcast addresses
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
    # TODO: check this loop again, it takes the next value of each_address - "off by one issue"
    # Example to test:
    # IP Address: 192.168.0.200/28
    # MASK: 255.255.255.240 - /28
    # WILDCARD: 0.0.0.15
    # Decimal representation:
    # 11000000.10101000.00000000.11001000
    # [0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240]
    # max subnets: 16
    # Network Address: 192.168.0.192    - correct
    # First host: 192.168.0.209         - INCORRECT (uses 208 from the list)
    # Last host: 192.168.0.222          - INCORRECT (uses 208 for the calculations)
    # Broadcast Addr: 192.168.0.223     - INCORRECT (uses 208 from the list)
    # Usable hosts: 14
    if fourth_octet >= each_address:
        network_addr = str(first_octet) + '.' + str(second_octet) + '.' + str(third_octet) + '.' + str(each_address)
    else:
        break



# Get First Host, Last Host and Broadcast Addresses:
# TODO It is currently incorrect:
# "each_address" gets incremented by the loop above and always the biggest network address is used for the calculations
# to either add host_min, host_max and broadcast_addr in the for loop above or:
# to store network_addr in list instead of a string and use index to get it's last element for the calculations below
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






