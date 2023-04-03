# Get hdsentinel result output into JSON format

simple python script to convert result of hdsentinel output into JSON file.

How to run?
--> py hdsentinel.py

Json example output:
```json
{
    "Hostname": "client-01",
    "Device 0": "/dev/nvme0",
    "Model ID": "MidasForce SSD 1TB",
    "Serial No": "2022121700616",
    "Revision": "V0323A0",
    "Size": "953869 MB",
    "Interface": "NVMe",
    "Temperature": "50",
    "Highest Temperature": "50",
    "Health": "100",
    "Performance": "100",
    "Power on time": "7 days, 12 hours",
    "Est. lifetime": "more than 1000 days"
}