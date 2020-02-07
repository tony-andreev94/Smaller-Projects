# Subnet Calculator App:
# TODO Better comments and documentation


def convert_to_decimal(x):
    # TODO Optimize if 0 is reached before the last bit:
    # x = 192           #Bit value
    first_num = 0       # 128
    second_num = 0      # 64
    third_num = 0       # 32
    fourth_num = 0      # 16
    fifth_num = 0       # 8
    sixth_num = 0       # 4
    seventh_num = 0     # 2
    eight_num = 0       # 1
    if x == 0:
        return (str(first_num) + str(second_num) + str(third_num) + str(fourth_num) + str(fifth_num) + str(sixth_num)
                + str(seventh_num) + str(eight_num))
    else:
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


# IP address input:
while True:
    ip_address_input = input("Enter an IP address: ")  # 192.168.0.1
    # Check if the IP Address input is valid:
    # it is checked that 4 octets are typed in,
    # link-local IPv4 APIPA addresses, loopback addresses and well-known multicast addresses are not accepted
    ip_octet = ip_address_input.split('.')
    if (len(ip_octet) == 4) and (1 <= int(ip_octet[0]) <= 223) and (int(ip_octet[0]) != 127) and (
            int(ip_octet[0]) != 169 or int(ip_octet[1]) != 254) and (
            0 <= int(ip_octet[1]) <= 255 and 0 <= int(ip_octet[2]) <= 255 and 0 <= int(ip_octet[3]) <= 255):
        # If the input is valid the loop is stopped and the program continues
        break
    else:
        print("The IP address is not valid!")
        continue

# Subnet mask input:
while True:
    mask = int(input("Enter mask: /"))  # 24
    # Check validity
    if 8 <= mask <= 30:
        # Mask is valid.
        break
    else:
        print("The mask is not valid!")
        continue

# Ask if decimal output should be included:
while True:
    include_dec = input("Print decimal representation(yes/no)?")
    if include_dec == 'yes' or include_dec == 'Yes':
        include_dec_bool = True
        break
    elif include_dec == 'no' or include_dec == 'No':
        include_dec_bool = False
        break
    else:
        print("Invalid input.")
        continue

network_addr = ""
broadcast_addr = ""

# Split IP Address in octets
ip_address = ip_address_input.split(sep='.')
first_octet = int(ip_address[0])
second_octet = int(ip_address[1])
third_octet = int(ip_address[2])
fourth_octet = int(ip_address[3])

print()  # empty print line to divide output data from input data
print(f"IP Address: {ip_address_input}/{mask}")

# IP address decimal representation:
if include_dec_bool:
    print("IP decimal representation:")
    print(convert_to_decimal(first_octet), end=".")
    print(convert_to_decimal(second_octet), end=".")
    print(convert_to_decimal(third_octet), end=".")
    print(convert_to_decimal(fourth_octet))

# Variables and logic to calculate the decimal mask
first_oct_m = 255
second_oct_m = 255
third_oct_m = 255
fourth_oct_m = 255
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

# Define and print DECIMAL MASK
decimal_mask = str(first_oct_m) + '.' + str(second_oct_m) + '.' + str(third_oct_m) + '.' + str(fourth_oct_m)
print(f"Mask: {decimal_mask} - /{mask}")

# Define and print WILDCARD MASK
wildcard_mask = str(255 - first_oct_m) + '.' + str(255 - second_oct_m) + '.' + str(255 - third_oct_m) + '.' \
                + str(255 - fourth_oct_m)
print(f"Wildcard mask: {wildcard_mask}")
print()  # empty print line for better visualization

# Calculate total usable host addresses:
power_var = 32 - mask  # variable to get the power used to calculate the total and usable addresses
total_hosts = 2 ** power_var  # total addresses in a subnet
# usable host addresses in a subnet are the total addresses - network and broadcast addresses
usable_hosts = total_hosts - 2  # usable host addresses in the subnet

# Calculate network address and available subnets:
# We create a list with all available network addresses
# The available subnets are calculated by checking the length of this list
network_address_list = []  # a list of all network/subnet IDs is defined if it's needed for future use
for i in range(0, 255, total_hosts):
    network_address_list.append(i)

max_subnets = len(network_address_list)

# Find the network address from the network_address_list
for each_address in network_address_list:
    if fourth_octet >= each_address:
        # We need an additional variable for the last octet of the network address (subnet_id_octet)
        # If we don't have it, the loop will cycle once more and the calculations
        # for host_min, host_max and broadcast_addr will be incorrect (off by one issue)
        subnet_id_octet = each_address
        network_addr = str(first_octet) + '.' + str(second_octet) + '.' + str(third_octet) + '.' + str(subnet_id_octet)
    else:
        break

# Get First Host, Last Host and Broadcast Addresses:
host_min = str(first_octet) + '.' + str(second_octet) + '.' + str(third_octet) + '.' + str(subnet_id_octet + 1)

# If condition for Class B addresses, where the mask is lesser than /24
if subnet_id_octet + usable_hosts > 255:
    third_octet = int(total_hosts / 256 - 1)
    host_max = str(first_octet) + '.' + str(second_octet) + '.' + str(third_octet) + '.' + '254'
    broadcast_addr = str(first_octet) + '.' + str(second_octet) + '.' + str(third_octet) + '.' + '255'
    # Sub-condition for Class A addresses, where the mask is lesser than /16
    if third_octet > 255:
        second_octet = int((total_hosts / 256) / 256 - 1)
        host_max = str(first_octet) + '.' + str(second_octet) + '.' + '255' + '.' + '254'
        broadcast_addr = str(first_octet) + '.' + str(second_octet) + '.' + '255' + '.' + '255'
# Else condition for Class C addresses, where the mask is /24 or greater
else:
    host_max = str(first_octet) + '.' + str(second_octet) + '.' + str(third_octet) + '.' + str(
        subnet_id_octet + usable_hosts)
    broadcast_addr = str(first_octet) + '.' + str(second_octet) + '.' + str(third_octet) + '.' + str(
        subnet_id_octet + usable_hosts + 1)

# PRINT RESULTS:
print(f"Network Address: {network_addr}")
print(f"First host: {host_min}")
print(f"Last host: {host_max}")
print(f"Broadcast Addr: {broadcast_addr}")
print(f"Usable hosts: {usable_hosts}")
print(f"Available subnets: {max_subnets}")
