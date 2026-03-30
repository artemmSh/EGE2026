from ipaddress import *
for A in range(256):
    net = ip_network(f'152.65.245.132/255.255.{A}.0')
    if all()