from ipaddress import *


def f(ip):
    ip = f'{int(ip):032b}'
    return ip[:len(ip) // 2].count('0') <= ip[len(ip) // 2:].count('0')


for A in range(256)[::-1]:
    net = ip_network(f'223.167.{A}.167/255.255.255.192', False)
    if all(f(ip) for ip in net):
        print(A)
        break
