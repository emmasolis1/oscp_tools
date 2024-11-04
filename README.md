# OSCP_Tools

## Active Directory
- **Get-SPN.ps1** - Retrieves Service Principal Names in AD, commonly used in Kerberoasting attacks.
- **GetCLSID.ps1** - Extracts CLSID information for COM objects, sometimes useful in AD contexts.
- **GetNPUsers.py** - Requests Ticket-Granting Tickets (TGTs) for Active Directory accounts without pre-authentication enabled, allowing brute-force attacks on the returned ticket hashes.
- **Invoke-Kerberoast.ps1** - Extracts Kerberos tickets for offline cracking.
- **PowerMad.ps1** - Creates and manages machine accounts in AD, often used in AD exploitation scenarios.
- **PowerView.ps1** - PowerShell script for comprehensive AD enumeration, useful for gathering domain information.
- **SharpGPOAbuse.exe** - Exploits Group Policy Objects (GPOs) to gain elevated privileges in a Windows Active Directory environment by modifying or hijacking GPOs to introduce malicious scripts or commands.
- **SharpHound.exe** - Collects AD data for BloodHound, identifying relationships, permissions, and attack paths in AD.
- **SharpHound.ps1** - PowerShell script implementation of SharpHound.
- **windapsearch.py** - Performs LDAP enumeration tool designed for Windows environments, allowing attackers to query and extract information from Active Directory, such as user accounts, groups, and permissions, to aid in privilege escalation or lateral movement.

## Client Side Attacks
- **config.Library-ms** - Library configuration for client attack setup.
- **install.lnk** - LNK file for installation attack vector.

## Credentials Extractors
- **mimikatz.exe** - Tool for extracting Windows credentials (64-bit).
- **mimikatz32.exe** - 32-bit version of Mimikatz.
- **Rubeus.exe** - Kerberos ticket extraction and abuse tool.

## Cross-Compiling
- **add_user_dll.c** - `.dll` for cross compiling and replace in DLL Hijacking attack, adds a new user (emma:Password123!).
- **add_user_exe.c** - `.exe` for cross compiling and replace in Service Binary Hijacking attack, adds a new user (emma:Password123!).

## `Gitdumper`
- **gitdumper.sh** - Dumps Git repositories.
- **extractor.sh** - Helper script for extracting Git data.

## Network Utilities
- **chisel_linux** - TCP/UDP tunneling tools for network redirection and port forwarding.
- **chisel_windows** - Windows version of Chisel.
- **ligolo_agent_linux / ligolo_agent_windows.exe** - Ligolo tunneling agents (clients), used for creating secure reverse tunnels.
- **ligolo_proxy_linux** - Ligolo proxy server for managing tunneling connections.
- **nc** - Linux version of Netcat.
- **nc.exe** - Windows version of Netcat.
- **nc64.exe** - 64-bit version of Netcat.
- **PortKnocker.sh** - Script for setting up a port-knocking mechanism, used in network operations.
- **PowerCat.ps1** - PowerShell implementation of Netcat (can move to Network Utilities for consistency).

## Potatoes (Windows Privilege Escalation)
- **CVE-2023-29360.exe** - CVE-based privilege escalation exploit.
- **GodPotato-NET4.exe, JuicyPotato.exe, RoguePotato.exe, RottenPotato.exe, SweetPotato.exe, SigmaPotato.exe** - Exploits for named pipe impersonation based on the permission `SeImpersonate`.
- **PrintSpoofer.exe** - Print Spooler exploit for privilege escalation.

## Privilege Escalation
- **accesschk.exe** - A Windows Sysinternals utility that enumerates access control permissions for files, directories, services, and registry keys, revealing areas where unauthorized access could be leveraged for privilege escalation.
- **FullPowers.exe** - A Windows privilege escalation tool designed to restore a service account’s default privileges, including `SeAssignPrimaryToken` and `SeImpersonate`, which can enable unauthorized actions by impersonating higher-privileged users or processes.
- **Invoke-RunasCs.ps1** - Executes commands as another user, useful for privilege escalation.
- **LinEnum.sh** - A comprehensive Linux privilege escalation script that automates the discovery of potential misconfigurations, vulnerable permissions, and exploitable binaries, often used for post-exploitation in penetration testing.
- **linuxprivchecker.py** - A detailed Linux privilege escalation checker that searches for misconfigurations, weak permissions, and vulnerable kernel modules, assisting in identifying escalation paths on Linux systems.
- **peass** - A set of privilege escalation auditing scripts (`linpeas`, `winpeas`) for Linux and Windows systems. These tools systematically identify misconfigurations, weak permissions, and exploitable services that may lead to privilege escalation.
- **PowerUp.ps1** - Searches for privilege escalation vectors on Windows.
- **PrivescCheck.ps1** - Checks Windows configurations for privilege escalation vulnerabilities.
- **SeManageVolumeExploit.exe** - An exploit targeting systems where the `SeManageVolume` privilege is granted, allowing unprivileged users to escalate privileges by manipulating volume-level permissions.

### `peass` Subfolder Contents
- **json2html.py, json2pdf.py** - Converts output to HTML and PDF.
- **legacy_linpeas.sh, legacy_winpeasx64.exe** - Legacy versions of `linpeas` and `winpeas`.
- **new_linpeas.sh, new_winpeasx64.exe** - Updated versions of `linpeas` and `winpeas`.
- **peas2json.py** - Converts `peas` output to JSON format.
