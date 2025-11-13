# cmdb-sync-automation
A python-based automation framework for syncing CMDB data with external systems like SharePoint and Excel.
=======
# CMDB Sync Automation

This project automates synchronization between a **CMDB** (such as Nautobot or NetBox) and **SharePoint/Excel** to manage portable network assets and their lifecycle states.

## Overview
The system uses Python scripts to keep your CMDB and SharePoint aligned — ideal for IT, networking, or operations environments.

## Data Flow
1. Fetch asset data from CMDB (API)
2. Generate Excel/CSV overview
3. Upload to SharePoint
4. Detect SharePoint updates
5. Push changes back into CMDB

## Features
- Two-way synchronization (CMDB ↔ SharePoint)
- Tracks asset states, custodians, and locations
- Uses APIs for automation
- Logs and validates every update

## Tech Stack
- **Python 3**
- `requests`, `pandas`, `openpyxl`
- **Microsoft Graph API**
- **Nautobot/NetBox REST API**

## Quick Start
```bash
git clone https://github.com/AJTechnics/cmdb-sync-automation.git
cd cmdb-sync-automation
pip install -r requirements.txt
python scripts/sync_from_cmdb.py

## 9bb5894 (Initial commit - CMDB Sync Automation project structure)
