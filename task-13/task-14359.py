from ipaddress import *

host_1 = ip_address('157.127.172.56')
host_2 = ip_address('157.127.191.78')

for mask in range(16, 25):
    net = ip_network(f'{host_1}/{mask}', False)
    if host_1 in net.hosts() and host_2 not in net.hosts():
        print(mask)
        break
