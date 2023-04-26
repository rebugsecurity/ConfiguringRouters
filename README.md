# ConfiguringRouters
This is an example code in Python that uses the paramiko library to automate the configuration of a router. Note that you'll need to modify the code to match your router's model and configuration

This code connects to the router using SSH and uses the ``exec_command()`` method to send commands to the router's command-line interface. The commands disable remote management, change the default username and password, and enable WPA2 encryption with a pre-shared key. Finally, the code saves the configuration changes and disconnects from the router.

# Installing requirements:
``pip3 install paramiko``

# Usage:
``python3 configuring.py``
