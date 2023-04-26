import paramiko

# Define the router's IP address, username and password
router_ip_address = "192.168.1.1"
username = "admin" # replace with your username
password = "YOUR_CURRENT_PASSWORD_HERE" # replace with your current password

# Connect to the router using SSH.
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(router_ip_address, username=username, password=password)

# Disable remote management config
stdin, stdout, stderr = ssh.exec_command("no ip http server")

# Change the default username and password
stdin, stdout, stderr = ssh.exec_command("username yourusername password yourpassowrd")

# Enabling WPA2 Encryption method.
stdin, stdout, stderr = ssh.exec_command("dot11 ssid yourssid")
stdin, stdout, stderr = ssh.exec_command("authentication open")
stdin, stdout, stderr = ssh.exec_command("authentication key-management wpa version 2")
stdin, stdout, stderr = ssh.exec_command("wpa-psk ascii yourpassword")

# Save the configuration changes
stdin, stdout, stderr = ssh.exec_command("write memory")

# Disconnecting from the router afterwards:
ssh.close()