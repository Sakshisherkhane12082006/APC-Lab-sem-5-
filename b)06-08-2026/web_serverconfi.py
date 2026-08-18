server_ip = ("192.168.1.10",)
allowed_ips = ["192.168.1.2", "192.168.1.3"]

def update_allowed_ips(ip):
    allowed_ips.append(ip)

update_allowed_ips("192.168.1.4")

print("Server IP:", server_ip)
print("Allowed IPs:", allowed_ips)

# server_ip cannot be changed directly because it is a tuple