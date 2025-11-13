"""
sync_from_cmdb.py
Example script for fetching asset data from a CMDB (e.g. Nautobot/NetBox)
and exporting it to an Excel/CSV file.
"""

import requests
import pandas as pd
import yaml

with open("config/settings.yaml", "r") as f:
    config = yaml.safe_load(f)

API_URL = config["cmdb"]["url"]
TOKEN = config["cmdb"]["token"]

headers = {"Authorization": f"Token {TOKEN}", "Content-Type": "application/json"}

r = requests.get(f"{API_URL}/api/dcim/devices/", headers=headers)
devices = r.json().get("results", [])

df = pd.DataFrame(devices)
df.to_excel("examples/example_output.xlsx", index=False)
print(f"Exported {len(df)} devices to examples/example_output.xlsx")
