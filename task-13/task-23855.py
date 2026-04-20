from ipaddress import *

host = ip_address('172.95.116.174')
net = ip_network(f'{host}/255.255.192.0', False)
if host in net.hosts():
    for ip in net.hosts():
        print(eval(str(ip).replace('.', '+')))
        break
