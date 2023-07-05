# 0x07. Networking basics #0
<kbd>DevOps</kbd> <kbd>Network</kbd>

## Resources
### Read/watch
* [OSI model](https://intranet.alxswe.com/rltoken/k2uCsynicuNbu1cAQhXqVQ)
* [Different types of network](https://intranet.alxswe.com/rltoken/XW3ZGm5Ya_a8XVDXcAKT_A)
* [LAN network](https://intranet.alxswe.com/rltoken/en370-Hrwgi_GUvFcg3bKg)
* [WAN network](https://intranet.alxswe.com/rltoken/Ah1EKqnINR85lM4P2WnLSw)
* [Internet](https://intranet.alxswe.com/rltoken/Lwh9xQxFD4dWh5sIApXI1g)
* [MAC address](https://intranet.alxswe.com/rltoken/j-Wp-YRvFTVP04SpIeRzHQ)
* [What is an IP address](https://intranet.alxswe.com/rltoken/HaZZvrmGaQ3U7ZLDYgZb6w)
* [Private and public address](https://intranet.alxswe.com/rltoken/OPJCZYuWSEXLIZOqU9Uc0A)
* [IPv4 and IPv6](https://intranet.alxswe.com/rltoken/M8g-egWLlldTl6Y0QECdwA)
* [Localhost](https://intranet.alxswe.com/rltoken/7lj-zoZQ7xFTkj4MTyos_g)
* [TCP and UDP](https://intranet.alxswe.com/rltoken/uJbs8E9-FyATfsELpmtTIg)
* [TCP/UDP ports List](https://intranet.alxswe.com/rltoken/4PYkqDfOvIZZb9aUPGOOzQ)
* [What is ping /ICMP](https://intranet.alxswe.com/rltoken/3zBgO6r2M1Q8lUVt9g8aJw)
* [Positional parameters](https://intranet.alxswe.com/rltoken/ZbMHH3jmxFhcrbigVy15iw)

### man or help:
* `netstat`
* `ping`

## General
### OSI Model
The *Open Systems Interconnect model* is a conceptual model from the **International Organization for Standardization** (ISO) the "provides a common basis for the coordination of standards development for the purpose of systems interconnection.

The model partitions the flow of data in a communication system into seven abstraction layers to describe networked communication:
* Physical layer
* Data link layer
* Network layer
* Transport layer
* Session layer
* Presentation layer
* Application layer

### LAN
A local area network connects devices over a relatively short distance. LANs are typically used within a networked office building, school or home, but can occasionally span a group of nearby buildings. LANs are often implemented as a single IP subnet.

### WAN
A wide area network span a larger physical distance. A WAN is a geographically-dispersed collection of LANs. A router connects LANs to a WAN.

### The Internet
The internet is the global system of interconnected computer networks that uses the Internet protocol suite to communicate between networks and devices.
* What is an IP Address?
> Every machine on the the Internet has a unique number assigned to it, called an IP address.  There are two types of IP addresses: **public** and **private** IP addresses. A public IP address is an IP address that can be accessed over the Internet. It is a globally unique IP address assigned to a computing device. A Private IP address, on the other hand, is used to assign computers within your private space without letting them directly expose to the Internet.
* What is Localhost?
> In computer networking, localhost is a hostname that refers to the current computer used to access it. It is used to access the network services that are running on the host via the loopback network interface. Using the loopback interface bypasses any local network interface hardware.
* What is a subnet?
> A subnet is a logical subdivision of an IP network. The practice of dividing a network into two or more networks is called *subnetting*.
* Why was IPv6 created?
> IPv6 (Internet Protocol Version 6) or IPng (Internet Protocol next generation) was deployed to fulfil the need for more internet addresses. IPv6 as born out of concern that the demand for IP addresses would exceed the available supply.

### TCP/UDP
* TCP and UDP are the 2 mainly used data transfer protocols for IP.
* The main difference between TCP and UDP is that the Transmission Control Protocol (TCP) provides a way to deliver (and receive) an ordered and error-checked stream of information packets over the network, while the User Datagram Protocol (UDP) is used to deliver a faster stream of information by doing away with error-checking. 
* What is a port?
> In computer networking, a port or port number is a number assigned to uniquely identify a connection endpoint and to direct data to a specific service. Some regularly used port numbers are 22 (SSH), 80 (HTTP) and 443 (HTTPS).
* What tool/protocol is often used to check if a device is connected to a network?
> **ping** is a computer network administration software utility used to test the reachability of a host on an Internet Protocol (IP) network. Ping operates by means of *Internet Control Message Protocol* (ICMP) packets. Pinging involves sending an ICMP echo request to the target host and waiting for an ICMP echo reply. The program reports errors, packet loss, and a statistical summary of the results, typically including the minimum, maximum, the mean round-trip times, and standard deviation of the mean.

## Requirements
* Allowed editors: `vi`, `vim`, `emacs`
* Files will be interpreted on Ubuntu 20.04 LTS
* Files should end with a new line
* A `README.md` file at the root of the folder of the project
* Bash script files must be executable
* Bash script must pass `Shellcheck` (version `0.7.0`) without any error
* The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
* The second line of all Bash scripts should be a comment explaining what is the script doing
