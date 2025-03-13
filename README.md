

## Advanced Shodan Intelligence Scanner

## **AUTHOR:**
`Rip70022`/`craxterpy`

# Overview:

Advanced Shodan Intelligence Scanner is a Python-based tool that retrieves and displays detailed information about a target IP address using the Shodan API. It presents structured intelligence reports, including network details, geolocation, and open ports.

# Features:

Retrieves host details using the Shodan API

Displays organization, ISP, and ASN information

Provides geolocation data (country, city, coordinates)

Lists associated hostnames and domains

Shows open ports and detected services

Includes a dynamic loading effect for a futuristic user experience


# Requirements:

`Python 3.x`

`requests`

`colorama`


# Installation:

Clone the repository and install the required dependencies:
```
git clone https://github.com/Rip70022/SHODAN.git
cd SHODAN
```

# Usage:

Run the script and enter the target IP address:
```
python SHODAN_SCANNER.py
```

# API Key Configuration:

Replace the API_KEY variable in the script with your Shodan API key:

```
API_KEY = "YOUR_SHODAN_API_KEY"
```

# Example Output:

```
[+] IP Address: 192.168.1.1
[+] Organization: Example Corp
[+] ISP: Example ISP
[+] ASN: AS12345
[+] Country: United States (US)
[+] City: New York
[+] Open Ports: 80, 443, 22
```

## Disclaimer:

This tool is intended for cybersecurity research and ethical use only. Misuse of this software is strictly prohibited.

## License:

This project is licensed under the `MIT License`.

