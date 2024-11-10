# Python Programming & Ethical Hacking Scripts

This repository contains Python scripts developed as part of a comprehensive course on Python programming and ethical hacking. The course starts from scratch and teaches both ethical hacking techniques and Python programming to write hacking tools and scripts, including but not limited to network hacking tools, keyloggers, backdoors, and website penetration testing scripts.


## Table of Contents
- [Introduction](#introduction)
- [Course Scripts Overview](#course-scripts-overview)
- [Programs Implemented](#programs-implemented)
- [Hacking Tools](#hacking-tools)
- [How to Use the Scripts](#how-to-use-the-scripts)
- [Prerequisites](#prerequisites)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Welcome to the Python Programming & Ethical Hacking Scripts repository! This collection of scripts is the result of a hands-on course where ethical hacking and Python programming are taught side by side. The course covers everything from basic Python programming concepts to advanced ethical hacking techniques and penetration testing tools. The goal is to provide you with practical skills to write Python programs for hacking systems in a responsible, ethical manner.

## Course Scripts Overview
This repository includes scripts designed for ethical hacking and penetration testing. The course teaches how to write these programs step by step, and each script corresponds to a specific concept or hacking technique. These scripts range from network-based tools like ARP spoofers to web application testing tools like XSS exploiters and vulnerability scanners.

## Programs Implemented
The following programs are included in the course and implemented in this repository:

**Networking & System Hacking**
- **mac_changer** :  Change the MAC address of your network interface.
- **network_scanner** : Scans the network to discover the IP and MAC addresses of connected clients.
- **arp_spoofer** : Redirects the flow of packets in a network, allowing data interception.
- **packet_sniffer** : Captures and filters network packets to extract sensitive information like usernames and passwords.
- **dns_spoofer** : Redirects DNS requests from one domain to another.
- **file_interceptor** : Intercepts and replaces files being downloaded from the network.
- **code_injector**: Injects malicious code into intercepted HTML pages.

**Malware & Exploitation**
- **reverse_backdoor**: Creates a backdoor that provides remote control over a compromised system.
- **keylogger**: Records keypresses and sends them via email.
- **execute_and_report_payload**: Executes commands on a system and sends the result via email.
- **download_execute_and_report_payload**: Downloads and executes a file on a target system, then reports back.

**Website Penetration Testing**
- **crawler**: Crawls a website to discover hidden paths and files.
- **discover_subdomains**: Discovers subdomains of a given website.
- **vulnerability_scanner**: Scans a website for common vulnerabilities and generates a report.
- **guess_login** : Runs a wordlist-based attack to guess login credentials for a website.

# Hacking Tools
These tools focus on various aspects of network security, website hacking, and malware creation. Each tool is demonstrated and explained within the course, and you can find the complete Python scripts here. These tools are meant for educational use and should only be used on systems where you have explicit permission to conduct testing.

# How to Use the Scripts
1. **Clone this repository to your local machine**:
```bash
git clone https://github.com/linson-rodrigues/python-hacking-scripts.git
```


2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the scripts***:
```bash
python network_scanner.py
```


## License
This repository is for educational purposes only. All scripts are provided "as is" with no warranties. Use them only on systems that you have permission to test. Unauthorized access or use of these tools is illegal and unethical.

## Disclaimer
This repository is intended strictly for educational purposes. All hacking activities should be conducted in controlled environments (like your own penetration testing lab) and only on systems that you own or have explicit permission to test.

