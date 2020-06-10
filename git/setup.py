#init setup script
import os
stream = os.popen('apt install -y git')
output = stream.read()
print(output)
