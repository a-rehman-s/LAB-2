import re

with open("D://file.txt", "r") as file:
    content = file.read()
    ips = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', content)
    print("IP Addresses:", ", ".join(ips))
