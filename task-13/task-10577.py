from ipaddress import *

host_1 = ip_address('165.112.200.70')
host_2 = ip_address('165.112.175.80')

for mask in range(30, 15, -1):
    net = ip_network(f'{host_1}/{mask}', False)
    if host_1 in net.hosts() and host_2 in net.hosts():
        print(mask)
        break
