## portscan.py

Python script that scan the top 100 TCP ports, like nmap

### Usage:

```bash
$ python portscan.py

Enter the IP to scan: 10.10.11.221
SCAN 10.10.11.221 in 100 TOP PORTS ...


OPEN PORTS:
 - PORT 80 (HTTP)
 - PORT 22 (SSH)


```

The script performs a TCP port scan on a given IP address to check which ports from a predefined list (Top 100 TCP ports) are open.
Main Steps:

    Top Ports Definition: A dictionary TOP_PORTS contains common TCP ports with their respective services (e.g., HTTP, SSH, FTP).

    Port Scanning:
        The scan_port function tries to connect to a given port on a specified IP address with a timeout of 0.5 seconds.
        If the connection is successful (connect_ex returns 0), it considers the port open.

    Parallel Execution:
        The script uses the concurrent.futures.ThreadPoolExecutor to perform the port scanning concurrently on multiple ports, allowing faster scanning by using multiple threads.

    Result:
        After scanning all the ports, it prints out a list of open ports and their corresponding services.
        If no open ports are found, it notifies the user.



