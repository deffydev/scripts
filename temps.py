#!/usr/bin/env python3
# temps.py: Python version of my temps script

import json
import shutil
import subprocess

#Run the sensors command and capture the output
result = subprocess.run(["sensors", "-j"], capture_output=True, text=True)
data = json.loads(result.stdout)

# Dig into the dictionary for each reading
cpu = data["k10temp-pci-00c3"]["Tctl"]["temp1_input"]
gpu = data["amdgpu-pci-0300"]["edge"]["temp1_input"]
hotspot = data["amdgpu-pci-0300"]["junction"]["temp2_input"]
power = data["amdgpu-pci-0300"]["PPT"]["power1_average"]

print("==> Temperatures")
print(f"CPU:            {round(cpu)}°C")
print(f"GPU:            {round(gpu)}°C")
print(f"GPU hotspot:    {round(hotspot)}°C")
print(f"GPU power:      {round(power)} W")
print()

# disk(): prints used, total, percent, and free space for one drive
def disk(name, folder):
    usage = shutil.disk_usage(folder)
    gb = 1024 ** 3
    used = usage.used / gb
    total = usage.total / gb
    free = usage.free / gb
    percent = usage.used / usage.total * 100
    print(f"{name:<24} {used:5.0f}G of {total:5.0f}G {percent:3.0f}% used ({free:.0f}G free)")

print("==> Linux disk space")
disk("System (PNY SSD)", "/")
disk("Steam games (Samsung SSD)", "/mnt/storage")