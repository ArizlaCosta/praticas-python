servidor1 = {
    "nome": "Web-01",
    "IP": "192.168.0.10",
    "containers": ["ngix", "mysql"]
}

servidor2 = {
    "nome": "App-01",
    "IP": "192.168.0.11",
    "containers": ["python-app", "redis"]
}

servidor3 = {
    "nome": "Storage",
    "IP": "192.168.0.12",
    "containers": "nfs-server"
}
servidor1["containers"].append("certbot")
servidor2["containers"].remove("redis")
print(servidor3["IP"])
print(servidor1["containers"])
