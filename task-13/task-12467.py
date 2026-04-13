from ipaddress import *


def f(ip):
    ip = f'{int(ip):032b}'
    return ip[16:].count('1') > 3


for A in range(256):
    net = ip_network(f'183.192.{A}.0/255.255.252.0', False)
    if ip_address(f'183.192.{A}.0') == net.network_address and all(f(ip) for ip in net):
        print(A)
        break
