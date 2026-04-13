from ipaddress import *

host_1 = ip_address('200.154.190.12')
host_2 = ip_address('200.154.184.0')

for mask in range(24, 15, -1):
    net = ip_network(f'{host_1}/{mask}', False)
    if host_1 in net.hosts() and host_2 in net.hosts():
        print(mask)
        break
