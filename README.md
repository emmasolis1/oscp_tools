# OSCP Tools Repository

This repository contains a curated collection of tools for OSCP preparation and practical penetration testing.  
Tools are organized according to the typical attack workflow: Recon → Initial Access → Active Directory (if applicable) → Privilege Escalation → Credentials Looting → Reverse Engineering (if applicable).

> **Note:** Some tools are intentionally duplicated for convenience. Their descriptions appear in all folders where they are placed.

---

## 📂 01_recon_enum
**Purpose:** Reconnaissance and enumeration of networks, hosts, and services.

- **wordlists/** – Passwords, usernames, and directories for brute-force attacks.  
- **network_utilities/** – Network tools for scanning, pivoting, and tunneling:
  - `ncat` – Netcat variants for quick shell connections.  
  - `chisel` – TCP/UDP tunneling tool for port forwarding/pivoting.  
  - `ligolo` – Lateral movement agent and proxy.  
  - `PowerCat.ps1` (↔ duplicate) – PowerShell netcat alternative for scanning and reverse shells.  
  - `PortKnocker.sh` – Script for port knocking and stealth access.  
- `windapsearch.py` – LDAP enumeration script.  
- `linpeas.sh` (↔ duplicate from 04_privilege_escalation/linux/) – Linux privilege enumeration script.  
- `winpeasx64.exe` (↔ duplicate from 04_privilege_escalation/windows/) – Windows PEAS enumeration tool.

---

## 📂 02_initial_access
**Purpose:** Tools and scripts for gaining initial access to targets.

- **client_side_attacks/** – Malicious shortcut and library files for social engineering.  
- **git_dumper/** – Scripts to extract sensitive data from git repositories.  
- **cross_compiling/** – C programs for creating user accounts or DLLs.  
- `PowerCat.ps1` (↔ duplicate from 01_recon_enum/) – Quick reverse shell and network tunneling tool.

---

## 📂 03_active_directory
**Purpose:** Enumeration and exploitation of Active Directory environments.

- `PowerView.ps1`, `PowerMad.ps1` – AD enumeration and privilege scripts.  
- `Get-SPN.ps1`, `Invoke-Kerberoast.ps1` – Kerberoasting and SPN enumeration.  
- `GetCLSID.ps1`, `GetNPUsers.py` – Object enumeration and AS-REP roasting.  
- `SharpHound.exe / .ps1` – BloodHound data collection.  
- `GMSAPasswordReader.exe`, `SharpGPOAbuse.exe` – GMSA and GPO exploitation.  
- `mimikatz.exe` (↔ duplicate from 05_credentials_looting/) – Extracts Windows credentials.  
- `Rubeus.exe` (↔ duplicate from 05_credentials_looting/) – Kerberos ticket extraction and abuse.

---

## 📂 04_privilege_escalation
**Purpose:** Elevate privileges on Windows and Linux systems.

- **windows/**  
  - `PrivescCheck.ps1` – Quick Windows privilege check.  
  - `PowerUp.ps1` – Automated Windows privilege escalation tool.  
  - `Invoke-RunasCs.ps1` – Exploit misconfigured `runas` for privilege escalation.  
  - `FullPowers.exe` – Combined PowerShell privilege escalation binary.  
  - `SeRestoreAbuse.exe` – Abuse SeRestorePrivilege.  
  - `SeDebugPrivesc.exe` – Exploit SeDebugPrivilege for privilege escalation.  
  - `SeManageVolumeExploit.exe` – Exploit SeManageVolumePrivilege.  
  - `accesschk.exe` – Windows permissions and ACL auditing tool.  
  - `CVE-2023-29360.exe` – Windows local privilege escalation exploit.  
  - **potatoes/** – Various "Potato" exploit binaries:
    - `JuicyPotato.exe`, `SweetPotato.exe`, `GodPotato-NET4.exe`, `RottenPotato.exe`, `RoguePotato.exe`, `PrintSpoofer.exe`, `SharpEfsPotato.exe`, `SigmaPotato.exe`, `CVE-2023-29360.exe` (exploit binaries for privilege escalation).  
  - `winpeasx64.exe` – Windows enumeration script (↔ duplicate from 01_recon_enum).    
  - `chisel/` (↔ duplicate from 01_recon_enum/network_utilities) – Pivoting and tunneling tool.  
  - `ligolo/` (↔ duplicate from 01_recon_enum/network_utilities) – Lateral movement proxy.

- **linux/**  
  - `LinEnum.sh` – Linux privilege enumeration script.  
  - `linuxprivchecker.py` – Linux privilege escalation helper.  
  - `linpeas.sh` – Linux PEAS script (↔ duplicate from 01_recon_enum).

- **cross_platform/**  
  - `peas-utils/` – Helper scripts for parsing PEAS output (json2pdf.py, json2html.py, peas2json.py).

---

## 📂 05_credentials_looting
**Purpose:** Extract and manipulate credentials.

- `mimikatz.exe` – Windows credential dumper (↔ also in 03_active_directory and 04_privilege_escalation).  
- `mimikatz32.exe` – 32-bit Windows credential dumper.  
- `Rubeus.exe` – Kerberos ticket extraction and abuse (↔ also in 03_active_directory).

---

## 📂 06_reverse_engineering
**Purpose:** Analyze binaries and assemblies.

- `dnSpy/` – .NET assembly decompiler and debugger (↔ also in 04_privilege_escalation/windows/).

---

## ⚡ Tips for Usage
1. Start with `01_recon_enum` for network and host discovery.  
2. Use `02_initial_access` once an entry point is found.  
3. Enumerate AD and credentials in `03_active_directory` & `05_credentials_looting`.  
4. Perform privilege escalation in `04_privilege_escalation` (Windows/Linux separation helps).  
5. Reverse engineer suspicious binaries using `06_reverse_engineering/dnSpy`.  
6. Duplicates exist intentionally for convenience; always check the canonical folder for updates.

---
