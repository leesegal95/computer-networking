# Chapter 2: Application Layer

## 2.1 Principles of Network Applications 

- This level works on the users browser and the web server -> does not interact with switches / hosts etc 

* Application architecture: dictates how the application is structured over the various end systems 

Two predominant arch paradigms in modern network app:
1) client-server arch
    - always-on host -> server 
        - server services requests from other hosts (clients)
        - server has a fixed address
        - always on
    - clients: make requests to the server 
        - client hosts do not communicate with each other 
        - can always contact the server to that fixed ip address 
    - examples of this arch:
        - email, web, FTP, Telnet 
    - data center: house a large number of hosts to be able to handle all the request from clients 
    - must pay recurring interconnection and bandwidth costs for sending data from their data centers 
2) peer-to-peer (P2P) arch
    - minimal or no reliance on dedicated servers in data centers - app exploits direct communication between pairs of intermittently connected hosts called peers 
    - does not need to go through a service provider communicated directly with peers (desktops and laptops)
    - popular example -> BitTorrent
    - compelling feature: self-scalability 
    - pros:
        - cost effective, self-scalable, dont require significcant server infra and server bandwidth 
    - cons:
        - security
        - performance
        - reliability due to their higher decentralized structure 

#### Process Communication 

* process: program running within a host 
    - within same host -> 2 processes communicate using inter-process communication (defined by OS)
    - processes in diff hosts communicate by exchanging messages 
* client process: process that initiates communication 
* server process: process that waits to be contacted 
- App with P2P arch have client processes and server processes  as the same process 
- Within the Web -> a web browser is a client process and web server is the server process 
- I.E with P2p file sharing -> the peer downloading is the client and the peer that is uploading the fille is the the server 

#### Sockets 
* Socket: when a process want to end a message to another process on another host, it shoves the message out its door (socket)
- socket sends and receives the messages from the hosts 
- a socket is the interface between the app layer and transport layer within a host 
- a socket is also referred as an API (Application Programming Interface) between the app and the network sine the socket is the programming interface with which network apps are built 
- app developers have control on the app layer side but little control on the transport side of the socket 
- app developer controls on the transport side:
    - choice of transport protocol 
    - the ability to fix a few transport-layer parameters such as max buffer and ma segment sizes 

#### Addressing Processes 

- To be able to send packets from on host to another you need:
    1) the address of the host
        - Ip address of host
    2) an identifier that specifies the receiving process in the destination host 
        - identify the receiving socket -> identify the receiving socket through a prot number 

- Internet host is identified by an IP address
    - 32-bit quantity that uniquely identifies the host 
- popular app have been assigned port numbers
    - i.e web server = port 80
    - mail server process (SMTP) = port 25 
    - can find a list here: www.iana.org 
