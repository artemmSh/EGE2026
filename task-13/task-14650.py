from ipaddress import *

host_1 = ip_address('216.54.187.235')
host_2 = ip_address('216.54.174.128')

for mask in range(24, 15, - 1):
    net = ip_network(f'{host_1}/{mask}', False)
    if host_1 in net.hosts() and host_2 not in net.hosts():
        print(mask)
        break
