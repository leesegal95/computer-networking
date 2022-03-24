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
        - cost effective, self-scalable, dont require significant server infra and server bandwidth 
    - cons:
        - security
        - performance
        - reliability due to their higher decentralized structure 

#### How to create a network app 
    - write programs that:
        - run on diff end systems
        - communicate over network
        - web server software communicates with browser software
    - no need to write software for network core-devices
        - network-core devices do not run user apps

#### client0server paradigm

- server:
    -always-on host
    - permanent IP addy
    - often in data centers for scaling
- clients:
    - contact, communicate with server
    - may be intermittently connected
    - may have dynamic IP address
    - do not communicate with each other 
    - ex. HTTP,IMAP

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
- process sends/receives messages to/from its socket
- socket sends and receives the messages from the hosts 
- a socket is the interface between the app layer and transport layer within a host 
- a socket is also referred as an API (Application Programming Interface) between the app and the network sine the socket is the programming interface with which network apps are built 
- app developers have control on the app layer side but little control on the transport side of the socket 
- app developer controls on the transport side:
    - choice of transport protocol 
    - the ability to fix a few transport-layer parameters such as max buffer and ma segment sizes 
- socket analogous to door
    - sending process shoves message out door
    - sending process relies on transport infrastructure on other side of door to deliver message to socket at receiving process
    - two sockets involved: one on each side

#### Addressing Processes 
- Ip address is not enough on its own because you can have many process running on the same hosts
* identifier: includes both IP address and port number associated with the process on host
- combine IP address and port number -> combo defines a unique socket for communication to be used between two hosts 
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

#### An application-layer protocol defines:
- types of messages exchanged,
    - e.g., request, response
- message syntax:
    -what fields in messages & how fields are delineated
- message semantics
    - meaning of information in fields
- rules for when and how processes send & respond to messages
- open protocols:
    - defined in RFCs, everyone has access to protocol definition
    - allows for interoperability
    - e.g., HTTP, SMTP
- proprietary protocols:
    - e.g., Skype, Zoom
    - optimization of the protocol itself is why we use proprietary protocols 

### Transport Service Available to apps through transport-layer protocols through computer network 

####  What transport serevice does an app need?
- data integrity 
    - require 100 percent reliable data transfer -> like file transfer and web transactions
    - some apps that can tolerate loss (audio) -> but these need continuos connection
- timing
    - some apps require low delay to be effective -> like internet, telephony, interactive games
- throughput 
    - some apps require minimum amount of throughput to be effective -> multimedia
    - other apps make use of whatever throughput they get -> elastic apps
- security
    - encryption, data integrity 

#### Reliable Data Transfer
- process-to-process reliable data transfer 
- passes data onto the socket and knows with complete confidence that the data will arrive without error on the receiving end 
- if this isnt provided in a transport- layer protocol then some of the data sent by the sending process may never arrive at the receiving process
    - acceptable for loss-tolerant apps 

#### Throughput 
- reminder from chapter 1: throughput is the rate at which the sending process can deliver bits to the receiving process 
- if transport layer protocol enacts this you can rely that the app would guarantee throughout rate of *r bits /sec*
- apps that have throughput requirements are called -> *bandwidth-sensitive applications*
- apps that dont require certain throughput requirements are called -> *elastic applications*

#### Timing 
- guarantee the time it would take for the receiver to get the data 
- this is needed for real time appliations such as vms, multiplayer games, anything that cannot handle long delays 

#### Security 
- can encrypt all the data transmitted by the sending process and decrypt for the receiving host
- can provide confidentiality, data integrity and end point auth

### Transport services provided by the Internet 

- TCP/IP networks make two transport protocols available to apps:
    - UDP
        - unreliable data transfer service -> UPD provides no guarantee that the message will ever reach the receiving process
            - messages may also arrive out of order if they reach the receiving process 
        - lightweight transport protocol, providing minimal services 
        - connectionless -> no handshake before messages are sent 
        - does not provide: reliability, flow control, congestion control, timing, throughput, guarantee, secuirty or connection setup
        - why use UDP?
            - cost!!! 
            - cheaper and faster 
            - i.e youtube

    - TCP
        - reliable transport between sending and receiving process
        - flow control: sender will not overwhelm the receiver -> will make sure it cannot provide more information than can be absorbed 
        - congestion control: throttle sender network overload 
        - does not provide: timing, minimum throughput guarantee, security 
        - connection-oriented: setup required between client and server processes 
        - connection-oriented service
            - the client and server create a connection before the messages are sent, creates a TCP connection
            - the connection is full-duplex meaning that the two processes can send messages to each other over the connection at the same time 
            - the messages are finished, the connection is teared down 
        - reliable data transfer service 
            - can reply on TCP to deliver all data sent without error and in the correct order 
        - TCP includes a congestion control mechanism 

#### SEcuring TCP
    - Vanilla TCP and UDP sockets 
#### Focus on Security 

- neither TCP nor UDP provides encryption -> if the message is not encrypted than anyone who gets access to the links could steal the information since its in clear text 
- enhancement for TCP was created to protect the data being sent called Transport Layer Security (TLS)
    - TCP enhanced with TLS provides everything TCP originally provided and added on the following security features:
        - encryption
        - data integrity
        - end-point auth
- enhancement occurs on the application level
- if an app wants to use the TLS enhancement needs TLS code -> in both the client and server side of the app 
- How it works:
    - an app uses TLS -> send process passes cleartext data to the TLS socket -> TLS n the sending host then encrypts data and passes it to the TCP socket -> then travel to the TCP socket in the receiving process -> the receiving process socket passes to the TLS socket for decryption 

##### Services not provided by Internet Transport Protocol 

- timing guarantees and throughput are not provided by todays internet protocols 
- todays internet can often provide satisfactory service to time-sensitive apps but it cannot provide any timing or throughput guarantees 

### Application Layer Protocols 
* Application-layer protocol defines how an app, processes running on diff end systems, pass messages to each other. 
An app layer protocol defines:
    - types of messages exchange -> request or response message
    - syntax of the various message types -> fields of message, how they are delineated, etc
    - semantics of the fields -> info in the fields 
    - rules for determining when and how a process sends messages and responds to messages 
- difference  between network application and application-layer protocol is that the application-layer protocol is only one piece of the network layer app

### The Web and HTTP

#### Overview of HTTP
- HTTP allows you to have different endpoints, hardware, operating system
    - allows different systems to speak the same language 
- follows the client-server model 
- HyperText Transfer Protocol (HTTP) -> implemented in client and server programs 
    - webs application layer protocol 
    - client and server programs talk to each other by exchanging HTTP messages
    - HTTP defines the structure of these messages and how the client and server exchange these messages 
    - client: browser that request, receives, (using HTTP) and displays web objects
    - server: web server sends (using HTTP protocol) objects in response to reqeusts
- Definitions:
    * web page -> consists of objects 
        * an object -> a file that is addressable by a single URL i.e HTML. JPEG image, Javascript file, a CCS style sheet file, or a video clip 
        - the base HTML file references the other objects in the page with the objects URLS
        - each URL has two components: 
            1) The hostname of the server that houses the object
            2) the objects path name 
    * web browser: implements the client side of HTTP
        - ie: internet explorer and chrome 
        * note: browser and client are used interchangeably 
    * web server: implements the server side of the HTTP, house web objects each addressable by a URL
        - popular web servers include Apache and Microsoft Internet Information Server 
- HTTP uses TCP as its underlying transport protocol
- How it works:
    - HTTP client initiates a TCP connection with the server -> once connection is established the browser and server processes access TCP through their socket interfaces 
- The browser sends an HTTP request and the server sends a HTTP response
* Stateless protocol - protocol that saves no information about the client 
* Non-persistent connections - each request / response pair is sent over a separate TCP connection 
    - to load a webpage would need to open up multiple connections
    - con: has to establish a new connection for reach object
        - each object has a delivery delay of 2 RTT
        - OS overhead for each TCP connection
        - browsers often open multiple parallel TCP connections to fetch referenced objects in parallel
    - response time:
        - RTT (Round trip time): time for a small packet to ravel from client to sever and back
            - 1 RTT to initiate connection 
        - HTTP response time (per object):
            - one RTT to initiate TCP connection
            - one RTT for HTTP request and first few bytes of HTTP response to return
            - object / file transmission time 
        - Non-persistent HTTP response time = 2RTT + file transmission time
* Persistent connection - each request / response are sent over the same TCP connection 
    - HTTP/1.1 leaves the connection TCP connection open after sending a response -> will close connection when the TCP connection is not used for a certain amount of time
    - as little as one RTT for all the referenced objects (cutting response time in half)
- HTTP can be configured to use both persistent/ non-persistent connections but *default* is persistent connection 
* Round-trip time (RTT) -> time it take for a small package to travel from client to server and then back to the client

### HTTP Message FOrmat 
#### HTTP Request Message
* Request line: first line of an HTTP message
    - Request line contains 3 fields:
        * method field -> values it can take: GET, POST, HEAD, PUT, and DELETE 
            - GET method: used when the browser requests an object, with the requested object identified in the URL field 
            - POST method: often used when a user needs to fill out a form  
                - user is still requesting a Web page from the server but the specific contents of the web page depend on what the user entered into the form fields 
                - i.e: user provides search words in a search engine 
            - HEAD method: similar as GET method but often used for debugging 
            - PUT Method: often used in conjunction with Web publishing tools -> allow a user to upload an object to a specific path on a specific Web server. It also is used by application that need to upload objects to web servers 
            - DELETE method: allows user or app to delete an object
            * Important to note that not always essential to use POST method with a form can use GET and instead of having it in the entity body it will be included in the request URL
                - i.e: www.somesite.com/animalsearch?monkeys&bananas
* Header lines: subsequent lines 
    * Host: [enter hostname] ->specifies the host on which the object resides 
    * Connection: close -> this tells us that the tcp connection will close after sending the object -> non-persistent connection
    * User-agent: specifies the browser type that is making the request
    * Accept-language: specifies the version the user prefers to request the object in but if it doesnt exist then return in the default language 

#### HTTP Response Message
* status line: has 3 fields 
    - the protocol version field
    - status code
    - a corresponded status message 
* Header lines:
    - connection:close -> close connection after sending the message 
    - Date: time and date the HTTP response was created oe last modified 
    - Server: indicates what server type the response was created by 
    - Last modified: time or date the object was created or last modified 
        - this field is critical for object caching 
    - Content-length: indicates the number of bytes in the object being sent 
    - Content-type: indicates that the object in the entity body is HTML text 
- Common status codes:
    - 200 OK: request succeeded and the info is returned in the response
    - 301 Moved Permanently: Requested object has been permanently moved; the new URL is specified in the Location: header of the response message. The client software will automatically retrieve the new URL
    - 400 BAD Request: This isa generic error code indicating that the request could not be understood by the server 
    - 404 Not Found: the requested document does not exist on this server 
    - 505 HTTP Version is not Supported: the requested HTTP protocol version is not supported by this server 

#### User Interaction: Cookies

- HTTP GET/response interaction is statless -> once TCP connection is closed nothing is saved  
* Cookies: allow sites to keep track of users, allows us to maintain information from the previous session, creates a record that corresponds back to a users computer and browser 
    - cookie are in the original browser thats used 
    - use to maintain a state of the connection
- cookie file is used on the user hos
- Has 4 components:
    1) a cookie header line in the HTTP response message
    2) a cookie header line in the HTTP request message
    3) a cookie file kept on the users end system and managed by the users browser 
    4) a back-end database on at the web site 
- Header line: Set-cookie: contains the identification number created for that user when they visited the site  
- where else have cookies effected our privacy:
    - ads
    - tracking 
what cookies can be used for:
    - auth
    - shopping carts 
    - recommendations
    - user session state (web email)

### Web Caching
goal: satisfy client request without involving origin server 
- google drive is an example of web caching
* Web cache: also called proxy server 
- has its own disk storage and keeps copies of recently requested objects in this storage 
- a users browser can be configured so that all the users HTTP requests are first directed to the Web cache

An example of a client requesting an object:

1) browser establishes a TCP connection to the Web cache and sends an HTTP request for the object to the Web cahce
2) web cache check to see if the object stored locally -> if yes sends it in the HTTP response message 
3) If not stored locally, web cache opens a TCP connection to the web server -> then the web cache sends an http request for the object on the cache-to-server TCP connection
4) when the web cache receives the object it store it locally and send a copy within an HTTp response message 

Web cache benefits:
1) reduce the response time for a client requests
2) can reduce traffic on an institution access ink to the Internet 
    - by reducing traffic, you need less bandwidth which ultimately reduces costs 
- web caching can reduce traffic in the Internet as a whole and thereby improving performance for all apps 

- Through the use of Content Distribution Networks (CDNs), web caches are increasingly playing an important role in the INternet 
    - CDN company installs many geographically distributed caches throughout the Internet -> thereby localizing much of the traffic 
#### The Conditional GET
goal: dont send object if cache has up-to-date cached version 
    - no object transmission delay
    - lower link utilization
cache: specify date of cached copy in HTTP request
    if-modified-since: <date> 
server: response contains no object if cached copy is up-to-date
    HTTP/1.0 304 Not Modified 
- caching reduces user-perceived response time but also introduces the new problem that the copy of an object residing in the cache may be stale 
    - the object houses in the Web server may have been modified since the copy was cached at the client 
- HTTP has a mechanism that resolves this problem -> the mechanism allows a cache to verify that its objects are up to date 
    - This mechanism is called a *conditional GET*
- HTTP request message is called a conditional GET if:
    1) the request message uses the GET method
    2) the request message includes an If-Modified-Since: header line 
#### HTTP/2
- HTTP/2 changes how the data is formatted and transported between the client and server 
- HTTP/1.1 uses persistent TCP connection -> allowing a web page to be sent from server to client over a single TCP connection 
* Head of Line (HOL) blocking: when the earlier objects on the HTML base page are bigger and take longer to render then the rest of the objects on the page -> causes a delay since its one TCP connection link
    - resolution: open parallel TCP connection so that the smaller objects can render and not be delayed by the bigger object 
    - HTTP/1.1 can open up to 6 parallel TCP connection -> this helps circumvent HOL blocking and to obtain more bandwidth 
- Primary goal of HTTP/2 -> reduce the number of parallel TCP connections for transporting a single Web page 
    - this will help reduce the number of sockets that need to be open and maintained at servers but also allows TCP congestion control to operate as intended 

#### HTTP 2 Framing 
- HTTP/2 solution for HOL blocking is to break each message into small frames and interleave the request and response massages on the same TCP connection 
- Most important enhancement of HTTP/2 is the ability to to break down an HTTP message into independent frames, interleave them, and then reassemble them on the other end 
- framing is down in a sub-layer of the HTTP/2 protocol 

### 2.3 Electronic Mail in the Internet 

Key components of the internet mail system:
- user agents
    - mail reader 
    - allow us to: read, reply, forward, save, and compose messages 
    - examples: Microsoft outlook, gmail
- mail servers
    - user agent sends the message to the mail server and the mail server queues the message 
    - each recipient has a mailbox located in one of the mail servers 
- Simple Mail Transfer Protocol (SMTP)
    - mail protocol for the Internet electronic mail 
    - uses TCP to transfer mail from the senders mail server to the recipients mail server 
    - 2 sides:
        - client: executes on the senders mail server 
        - Server: executes on the recipient mail server 
#### email: mail servers
mail servers:
- mailbox: contains incoming messages for user
- messaging queue of outgoing *to be sent) mail messages
- SMTP protocol: between mail servers to swend email messages
    - client: sending mail server
    - server: receiving mail server
    - the servers are unware of anything else that stands between them 
    - designed for communication between two computers 
#### SMTP
- SMTP does not normally use intermediate mail servers for sending mail 
    - if one mail server is in Hong Kong and the other servers is in St. Louis -> the TCP connection is a direct connection between the Hong Kong and St Louis servers 
    - SMTP uses port 25
- SMTP client and server do a handshake before transferring information
    - SMTP client indicates the email address of the sender and the email address of the recipient
    - after starting the handshake the client sends the message 
- SMTP relies on the reliable data transfer service of TCP to get the message to the server without errors 
- SMTP = Push, uses persistent connections 
#### email
- uses TCP to reliably transfer email message from client to server over port 25 or the secure mail port 465
#### Mail access protocols 
- mail access protocol: retrieval from server 
- Use mail servers to obtain all the emails and that why a users computer does not have to stay "always on" waiting for a message
- A user sends the message to their mail server either through SMTP or HTTP and then from her mail server uses SMTP to relay the email message to the other users mail serer ( the desired receiver of the message) -> this makes it so the user agent doesnt need to deal with an unreachable destination if the desired receiver computer is offline
- How does a user running a user agent on their local host obtain their messages that are sitting in a mail server?
   Note: Cant use SMTP to obtain messages because obtaining the messages is a pull operation and SMTP is a push protocol
   Two commons ways to retrieve the emails from the mail server:
    1) if it is a web based email or smartphone app (i.e gmail) then the user agent will use HTTP to retrieve the users email
        - this means the users mail server has an HTTP and SMTP interface 
    2) Internet Mail Access Protocol (IMAP) -> typically used by mail clients such as outlook

### DNS - The INternets Directory Service 
* Hostname -> a way to identify hosts -> using a name which is easier for humans but gives very little about where the host lives on the internet 
    - the alphanumeric characters are difficult to be processed by routers 
* Ip addresses -> another way to identify hosts 
    - consists of 4 bytes and has a rigid hierarchical structure 
    - each period separates on of the bytes expressed in decimal notation from 0 to 255
    - IP address is hierarchical because as humans scan the address from left to right you obtain more and more information about where the host is located on the internet

#### Services provided by DNS

* Domain name system (DNS) -> translates hostnames to IP address 
DNS is:
    1) a distributed database implemented in a hierarchy of DNS servers 
    2) an application-layer protocol that allows hosts to query the distributes db 
- DNS servers are often UNIX machines running the Berkeley Internet Name Domain (BIND) software 
- DNS protocol runs on UDP and uses port 53
- DNS is commonly used by other application-layer protocols including HTTP and SMTP to translate user supplied hostnames to IP address 
- DNS adds an additional delay to the Internet apps that use it 
    - to minimize delay and network traffic the desired IP address is often cached ina "nearby" DNS server 
Other DNS services:
    - Host aliasing: a host with a complicated hostname can have one or more alias names -> DNS can be invoked by an app to obtain the canonical hostname for a supplied alias hostname as well as the IP  address of that hostname 
        * canonical hostname: having a hostname with multiple aliases 
    - Mail server aliasing
    - Load Distribution 

#### Overview of how DNS works 

3 class of DNS servers:

- root DNS servers 
- top level domain (TLD) DNS servers
- authoritative DNS servers 

- TLD:authoritative servers

Top-Level Domain (TLD) servers:
- response for .com,.org,.net.

Authoritative DNS servers
- organization own DNS server(s), providing authoritative hostname to IP mapping for organizations named hosts 


Example of how a DNS client wants to determine the IP address for the hostname www.amazon.com 
1) client contacts of the root servers which returns IP address for the TLD server for the top level domain com 
2) client then contacts one of these TDL servers which returns the IP address of an authoritative server for amazon.com 
3) Finally, the client contacts one of the authoritative servers for amazon.com which returns the IP address for the hostname www.amazon.com

* local DNS server -> central to the DNS architecture
    - each ISP such as a residential ISP or an institutional ISP has a local DNS server (also called a default name server)
    - hosts local DNS server is typically "close to" the host
    - when a hosts make a query its usually sent to the local DNS server which acts as a proxy 
    - local DNS servers help with speed and cost

- DNS caching
    - Recursive query:
        puts burden of name resolution on contacted name server
    - -> used by DNS to approve the delayed performance and to reduce the number of DNS messages being sent around the internet 
    - when a DNS get a reply it caches the mapping in its local memory 
    - DNS discard cache information after a period of time because data is always changing 

- caching, updating DNS records
    - once name server learns mapping -> it caches mapping 
        - cahce entries timeout after some time (TTL)
        - TLD servers typically cached in local name servers 
    - cache entries may be out-of-date
        - if not host changes IP address may be known internet-wide until all TLLs expire 
- DNS records and messages 
    - DNS protocol messages
        - DNS query and reply messages, both have the same format:
            message header:
                identification: 16 bit # for query
                flags: tell us speicifcs about the message itself 
    - INteresting records into DNS
        - i.e network utopia 
- DNS security
    - DDoS attacks 
        - bombard root server with traffic
        - bombard TLD servers 
    - redirect attacks
        - man-in-middle
            * intercept DNS queries
        - DNS poisoning
            * sending bogus replies to DNS server, which caches
    - Exploit DNS for DDos
        - send queries with spoofed source address: target IP
        - requires amplification 
            
    * Resource records (RR): basic building blocks of host-name and IP information and are used to resolve all DNS queries -> exist as many types to provide extended name-resolution services
        - 4 tuple that contains the following:
            (Name, Value, Type, TTL)
            - TTL = time to live of the resource record -> determines when a resource should be removed from cache 
            - Name and Value depend on Type
                - If Type = A then Name = hostname an Value = IP address for hostname 
                - if Type = NS, then Name is a domain and Value is hte hostname of an authoritative DNS server that knows how to obtain the IP address for hosts in the domain 
                - If Type = CNAME, then value is a canonical hostname for the alias hostname Name -> this record can provide querying hosts the canonical name for a hostname 
                - If Type = MX then Value is the canonical name of a mail server that has an alias hostname Name -> MX records allow the hostnames of mail server to have simple aliases 
    - each DNS reply record carries one or more RR
- host file: 
    - first area the operating looks at before it resolves the name 
    - in host file you can create a RR -> pointing a hostname to IP address 

### P2P file distribution
- no always on server
- arbitrary ends systems directly communicate
- peers request service from other peers, provide service in return to others
    - self scalability: new peers bring new service capacity, and new service demands
- bittorrent, distributing code, etc 

- Content Distribution Networks (CDN's) -> all major video-streaming companies make us of CDNS to help resolve the challenge of distributing massive amount of video data to users distributed around the world 
