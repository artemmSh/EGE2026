from ipaddress import *

ip_host = ip_address('218.48.192.56')
net_address = ip_address('218.48.192.0')
cnt = 0
for mask in range(10, 25):
    net = ip_network(f'{ip_host}/{mask}', False)
    if ip_host in net.hosts() and net_address == net.network_address and net.num_addresses >= 500:
        cnt += 1
print(cnt)
