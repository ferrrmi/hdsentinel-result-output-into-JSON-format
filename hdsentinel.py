import subprocess
import re
import socket
import json

cmd = ['sudo', './hdsentinel-019c-x64']
cwd = '{{ ur directory of hdsentinel }}'

result = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')

output = result.stdout.strip()

device_regex = r"HDD Device\s+\d+:\s+([^\n]+)"
model_regex = r"HDD Model ID\s+:\s+([^\n]+)"
serial_regex = r"HDD Serial No:\s+([^\n]+)"
revision_regex = r"HDD Revision\s+:\s+([^\n]+)"
size_regex = r"HDD Size\s+:\s+([^\n]+)"
interface_regex = r"Interface\s+:\s+([^\n]+)"
temperature_regex = r"Temperature\s+:\s+(\d+)\s+°C"
high_temperature_regex = r"Highest Temp.:\s+(\d+)\s+°C"
health_regex = r"Health\s+:\s+(\d+)\s+%"
performance_regex = r"Performance\s+:\s+(\d+)\s+%"
power_on_regex = r"Power on time:\s+([^\n]+)"
lifetime_regex = r"Est\. lifetime:\s+([^\n]+)"

hostname = socket.gethostname()

device_match = re.search(device_regex, output)
model_match = re.search(model_regex, output)
serial_match = re.search(serial_regex, output)
revision_match = re.search(revision_regex, output)
size_match = re.search(size_regex, output)
interface_match = re.search(interface_regex, output)
temperature_match = re.search(temperature_regex, output)
high_temperature_match = re.search(high_temperature_regex, output)
health_match = re.search(health_regex, output)
performance_match = re.search(performance_regex, output)
power_on_match = re.search(power_on_regex, output)
lifetime_match = re.search(lifetime_regex, output)

if device_match and model_match and serial_match and revision_match and size_match and interface_match and temperature_match and high_temperature_match and health_match and performance_match and power_on_match and lifetime_match:
    result_dict = {
    "Hostname": hostname,
    "Device 0": device_match.group(1),
    "Model ID": model_match.group(1),
    "Serial No": serial_match.group(1),
    "Revision": revision_match.group(1),
    "Size": size_match.group(1),
    "Interface": interface_match.group(1),
    "Temperature": temperature_match.group(1),
    "Highest Temperature": high_temperature_match.group(1),
    "Health": health_match.group(1),
    "Performance": performance_match.group(1),
    "Power on time": power_on_match.group(1),
    "Est. lifetime": lifetime_match.group(1)
    }
    result_json = json.dumps(result_dict)
    with open('/tmp/health_storage.json', 'w') as f:
        f.write(result_json)
else:
    print("Error: could not parse output")