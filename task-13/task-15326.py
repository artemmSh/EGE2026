from ipaddress import *

net = ip_network('105.224.200.224/255.255.255.224', False)
print(sum(f'{int(ip):032b}'.count('1') % 4 == 0 for ip in net))
