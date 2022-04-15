# Chapter 4: Network Layer: Data Plan

- There is a piece of the network layer in each and every host and router in the network

* data plane: determines how a datagrams is forwarded, forwarding 
* control plane: determines how the datagrams is routed, routing 

## Overview of the Network Layer

Layer goal: move packets from a send host to a receiving host

- Network layer function:
    - Forwarding: forward the packets to the correct receiving link
        - takes nanoseconds to accomplish -> usually implemented in hardware 
    - Routing: determine the route taken by packets as they flow from a sender to receiver
        * routing algorithms: the algorithm that calculates the path a packet will take 
        - takes seconds to accomplish -> usually implemented in software
* Forwarding table: table that defines how a frame will be forwarded out of a given switch or router in the network

### Control Plane: the traditional approach

- both forwarding and routing functions are contained within the router 
- routing algos determine values in the forwarding tables 
- traditional approach: each router has a routing component that communicates with the routing components of the other routers

#### Control Plane: The SDN Approach

- New approach: control plane routing functionalities is separated from the physical router
    - routing device performs forwarding only while the remote controller computes and distributes forwarding tables 
    - remote controller and routers communicate by exchanging messages containing forwarding tables and other pieces of routing information 
- SDN (Software defined networking): software-defined because the controller that computes forwarding tables and interacts with routers is implemented in software 
    - software implemention is open source -> can be approved upon by all 

### 4.1.2 Network Service model 

* Network service model: defines the characteristics of end-to-end delivery of packets between sending and receiving hosts 
- Services the network layer can provide:
    - Guaranteed deliver: Service gauarantes that a packet sent by a source host will eventually arrive at the dest host
    - Guaranteed delivery with bounded delay: guarantees delivery of packet within a specified host-to-host delay bound 
    - in order packet deliver: packets will arrive at dest in the order they are sent
    - guaranteed minimal bandwidth: emulates the behavior of a transmission link of a specified bit rate between sending and receiving hosts -> as long as the sending host transmits bits at a rate below the specified  bit rate, all packets are eventually delivered to the destination host 
    - security: encrypts datagrams at the source and decrypts at the destination  -> this provides confidentiality to all transport-layer segments
- The internet network layer -> best effort service 

* packet switch: general packet-switching device that transfers a packet from input link interface to output link interface -> according to the values in a packet header fields
    - some are called link-layer switches which based their forwarding on the link layer frame 
    - other packet switch's are called routers -> base forwarding decision on header field values in the network-layer datagrams

## 4.2 whats Inside a Router

- Generic router arch:
    - input ports: terminates an incoming physical link at a router, link layer functionality, lookup function -> here it uses the forwarding table to determine the router output port 
    - switching fabric: connects routers input and output ports -> fully contained within the router
    - output ports: stores packets received from the switching fabric and transmits these packets on the outgoing link by 
    - routing processor: preforms control plane functions -> executes the routing protocols, maintains routing tables and attached link state info, computes the forwarding table fro the router 
        - in SDN: routers -> routing processor is responsible for communicating with the remote controller and install these entries in the routers input ports and performs the network management functions 

### 4.2.1 input port processing and destination-based forwarding 

- impossible to scale if using dest address to forward packets -> users a the prefix of the packets destination address with the entries in the table -> if there is a match it will forward to the corresponding link interface 
- When there are multiple matches the router uses *longest prefix matching rule* -> finds the longest matching entry in the table and forwards the packet to the link interface associated with the longest prefix match

- Actions taken in input port:
    1. physical and link layer processing must occur 
    2. packets version number, checksum, and time-to-live field must be checked and the latter two fields rewritten
    3. counters used for network management must be updated 

### 4.2.2 Switching aka Switching fabric 

- here the packets are switched from an input port to and output port 
- Three switching techniques:
    1. Switching via Memory: switching between input and output ports are done under the direct control of the CPU (routing processor )
        - two packets cannot be forwarded at the same time even with diff dest ports 
    2. Switching via Bus: input port transfers a packet directly to the output port over a shared bus without intervention by the routing processor -> done by having the input port pre-pend a switch internal label (header) to the packet indicating the local output port to which this packet is being transferred and transmitting the packet onto the bus 
        - if diff packets arrive at the input port at the same time -> only one can go at a time since only one can ride the bus 
        - since all packets must cross the bus the switching speed of the router is limited to the bus speed 
    3. Switching via interconnection network: crossbar switching that connects multiple input ports to output ports
        - this allows for multiple packets being forwarded at once 
        - a crossbar switch is *non-blocking* -> a packet being forwarded to that output port will not be blocked from reaching that output port as long as no other packet is currently being forwarded to that output port 
        - routers switching capacity can be scaled by running multiple switching fabrics in parallel
            - an input port breaks a packet into K smaller chunks and sends the chunks through K of these N switching fabrics to the selected output port -> which reassembles the K chunks back into the original packet 

### 4.2.3 output port processing 

- output port processing: takes packets that have been stored in the output ports memory and transmits them over the output link 
    - scheduling and de-queuing packets for transmission
    - preforming the needed link layer and physical layer transmission functions

### 4.2.4 Where does queuing occur

- queuing can occur in input / output ports 
    - queuing will depend on the traffic load, the relative speed of the switching fabric, and the line speed 
    - if the queue grows too large and the memory runs out, packet loss will occur
        - here is where the packets are actually dropped and lost 
#### Input queuing 

- if the switching fabric is not fast enough to transfer all arriving packets through the fabric without delay then queuing will occur at the input port 
    - packets queued at the input port are waiting to be transferred through the switching fabric to the output port 
- Head of line (HOL) blocking occur in the input queued as well 
    - a queued packet in the input queue has to wait in the queue even though their output port is free because it is stuck behind another packet waiting for their output port to become available 

#### Output queueing 

- queueing can occur which can also lead to packet loss. When There is not enough memory left for an incoming packet there are two options:
    - drop the arriving packet -> drop-tail 
    - remove one or more already queued packets to make room for the arriving packet 
- Congestion control signal: mark the header of a packet before the buffer is full in order to provide a congestion singal to the sender 
* Active queue management (AQM): this is the idea of being proactive about packet dropping and marking policies to avoid congestion 
    - Popular AQM algo: 
        - Random Early Detection (RED) algo
        - PIE - proportional Integral controller Enhanced
        - CoDel

#### How much buffering is "Enough"?

- Adding more buffering is a double edge sword
    - If you have too much buffering can lead to increased delay 
        - buffering is like salt -> the right amount on food makes it delicious but too much makes it inedible 
* Bufferbloat: long delays deu to persistent buffering 

### 4.2.5 Packet Scheduling

#### First-in-first-out (FIFO)

- selects packets for link transmission in the same order they arrived at the output link 

#### Priority Queuing 

- packets arriving at the output link are classified into priority classes upon arrival at the queue 
    - assign priority for incoming packets
        - each priority class usually has its own queue, choice between the same priority class is usually done FIFO
* non-preemptive priority queuing discpline -> a packet is not interrupted once it has begun , even if a packet with a higher priority as come in -> the lower priority packet will finish before transmitting the higher priority pakcet 

#### Round Robin and Weighted Fair Queuing (WFQ)

- divided into classes and then use round robin to decide which classes queue first 
* work-conserving queueing discipline: never allows the link to remain idle whenever there are packets (for any class) queued for transmission
    - looks for a packet in a given class and if that class is empty will check the next class in the round robin sequence 
* weighted fair queuing (WFQ) discipline: a generalized form of round robin
    - arriving packets are classified and queued in the correct class waiting area -> WFQ scheduler will server classes in a circular manner -> class 1 first, class 2 second, class 3 and then repeating the service pattern 
    - WFQ is also a work conserving queue discipline -> meaning once a class is empty it will immediately move on to check the next class in the queue and wont let a link go idle 
- WFQ difference from Round Robin: in WFQ each class may receive a differential amount of service in any interval of time 

## 4.3 The Internet protocol (IP): IPv4, Addressing IPv6, and More

### 4.3.1 IPv4 Datagram Format 

- Internets network-layer packet is referred to as a datagram 
    - IPv4 datagram format header : Page 331 
    * Version Number: 4 bits specify the IP protocol version of the datagram -> the version number helps the router to determine how to interpret the remainder of the IP datagram -> Ipv4 and Ipv6 have diff datagram formats 
    * Header Length: tells you where the payload actually begins -> most IP datagrams have a 20-byte header 
    * Type of Service: TOS identifies which service is being used and two of the TOS bits are used for Explicit Congestion Notification
    * Datagram Length: Total length of the IP datagram (header + data) -> measure in Bytes
        - This field is 16 bits long -> theoretical max size of the IP datagram is 65,535 bytes
        - most datagrams are rarely larger than 1,500 bytes -> this allows an IP datagram to fit in the payload field of a maximally sized ethernet frame 
    * Identifier, flags, fragmentation offset: 3 fields are for fragmentation -> fragmentation is when you break up an IPv4 datagram into pieces and resemble it at the dest host before going to the transport layer -> IPv6 does not allow for fragmentation 
    * Time-To-Live (TTL): TTL field is included to make sure that datagrams dont circulate forever -> this field decreases by 1 each time the IP datagram is processed by the router -> If TTL hits 0 the datagram is dropped
    * Protocol: used when the datagram reaches its final destination -> used to specify the transport layer protocol which the data portion of this IP datagram should be passed too
        - Value 6 -> passed to TCP
        - Value 17 -> passed to UDP
        - Protocol number is the glue that binds the network and transport layer together , port number is the glue that binds the transport and application layers together 
    * Header Checksum: aids a router in detecting bit errors in a received IP datagram 
    * source & dest IP address" source creates a datagram and it inserts it Ip address into the source IP address field and inserts the address of the dest into the destination IP address field -> finds dest IP address through DNS lookup 
    * Options: this allows the IP header to be extended 
        - since this complicates and IP header this was not included in IPv6
    * Data (Payload): data field of the IP datagram contains the transport-layer segment (TCP or UDP) to be delivered to the dest -> the data field can carr other types of data such as ICMP messages
    - Note: IP datagram has a total of 20 bytes of header (assuming no options) -> if the datagram carries a TCP segment then the datagram carries 40 bytes of header *20 bytes of IP header plus 20 bytes of TCP header) along with the app-layer message 

### 4.3.2 IPv4 Addressing 

* interface: boundary between host and physical link 
- a router has multiple links connected to it and a interface for each link 
- Ip requires each host and router interface to have its own IP address
    - This means an IP address is technically associated with an interface rather than with the host or router containing that interface 
- each IP address = 32 bits (4 bytes) -> possibility of 2^32 (4 billion) IP address possible 
* dotted-decimal notation: format at which IP address are written 
- Every host and router in the global Internet must have an IP address that is globally unique (except for interfaces Behind NATS)
    - portion of interfaces IP address will be determined by the subnet to which it is connected
* Subnet (IP network): network interconnecting three host interface and one router interface 
    - determining subnet: detach each interface from its host or router -> creating islands of isolated networks with interfaces terminating the end points of the isolated networks -> each of these isolated networks is called a subnet 
* Subnet Mask: splits the IP address into the host and network address -> defining which part of the IP address belongs to the device and which part belongs to the network 
* Classless Interdomain Routing (CIDR): internets addressing assignment strategy -> CIDR generalizes the notion of subnet addressing
    - with subnet addressing the 32-bit IP address is divided into two parts with the dotted-decimal form a.b.c.d/x where x indicates the number of bits in the first part of the address
    - x -> constitutes the network portion of the IP address -> also known as a prefix of the address
        - organizations typically assign a block of contiguous addresses -> meaning a range of addresses with a common prefix -> devices within the organization will share common prefixes 
    - The rest of the 32 bits are used to distinguish among the devices within the organization 
        - these bits are considered when forwarding packets WITHIN the organization 
* address aggregation (route aggregation or route summarization): ability to use a single prefix to advertise multiple networks 
    - works well when addresses are allocated in blocks to ISP's and then from ISP's to client organizations 
* IP broadcast address: 255.255.255.255 
    - when a host sends a datagram with the broadcast as dest address -> the message is delivered to all hosts on the same subnet 

#### Obtaining a block of addresses / Obtaining a Host Address: The Dynamic Host Configuration Protocol

- once an organization has obtained a block of addresses it can assign individual IP addresses to host and router interfaces in its organization 
* Dynamic Host Configuration Protcol (DHCP): allows a host to obtain (be allocated) an IP address automatically 
    - network admin can configure DHCP so that give host receives the same IP address each time it connects to the network or a host may be assigned a temporary IP address that will be diff each time the host connects to the network
    - DHCP allows a host to learn addtion information such as:
        - subnet mask
        - the address of its first-hop router (called default gateway)
        - address of its local DNS server 
* plug-and-play / zeroconf (zero configuration) protocol -> ability to automate the network-related aspects of connecting a host into a network 
- DHCP is a client server 
    * client: newly arriving host wanting to obtain network configuration information -> including Ip address for itself 
- DHCP protocol is a four-step process:
    1. DHCP server discovery
        - The host first step is to find a DHCP server with which to interact with 
        * DHCP discovery message: method of finding the DHCP server to interact with
            - clietn sends the discovery message within a UDP packet -> port 67 -> this is encapsulated in an IP datagram 
            - DHCP client creates an IP datagram containing its DHCP discover message along with the broadcast deest IP address of 255.255.255.255 an a "this host" source IP address of 0.0.0.0
                - IP then forwards to the link layer an then broadcasts this frame to all nodes attached to the subnet 
    2. DHCP server offers
        * DHCP offer message: this is the response from a DHCP server which is receiving a DHCP discover message 
            - the offer message is also broadcast to all nodes 
            - each server offer message contains:
                - transaction ID of the received discover message
                - proposed IP address for the client
                - the network mask
                - an IP address lease time -> amount of time for which the IP address will be valid -> commeon for the server to set the lease time to several hours or days 
    3. DHCP Request
        * DHCP request message : this message accepts the offer -> indicating which server it selected 
            - broadcasts to all the DHCP servers to let them know which server was selected
    4. DHCP Ack 
        - the server responds to the DHCP request message with a DHCP ACK message confirming the request parameters 

- Once the DHCP ACK is recieved by the client -> the interaction is complete and the client can use the DHCP-allocated IP address for the lase duration 
    - if a client wants to extend the lease on the IP address, DHCP allows you to do so
- DHCP has short comings when it comes to mobile -> review more in chapter 7

### 4.3.3 Network Address Translation (NAT)

- NAT-enabled router that hides the details of the home network from the outside world 
    - this router usually gets its address from a DHCP server as well
* NAT translation table -> lives at the NAT router, used to tell the router the internal host to whit it should forward given datagram 
- port number field is 16 bits long -> NAT protocol can support over 60,000 simultaneous connections with a single WAN-side IP address for the router 
- IP address arrives at NAT router -> NAT router uses the NAT translation table to get the correct IP address and dest port number for the browser in the home network -> rewrites it in the datagram and forwards the datagram 

- NAT shortcoming: p2p connections
    - How can peers connect when one peer is behind a NAT?
        - NAT traversal tools were created to solve these problems 

* Intrusion detection systems (IDS) and firewalls: used to protect a network from malware / malicious packets trying to infiltrate the network 
    * firewalls: sit between the network and the internet  
        - they inspect the datagram and segment headers -> deny any suspicious datagram entries into the internal network 
    * IDS: situated at the network boundary -> performs a deep packet inspection 
        - examines the payloads in the datagram (including app layer data) and header fields 
            - IDS db contains packet signatures that are known to be part of attacks and automatically get updated when a new attack is discovered 
            - If a match is found an alert is created
    * IPS (intrusion prevention system): similar to IDS except that if actually blocks packets in addition to creating alerts 

### 4.3.4 IPv6

#### IPv6 Datagram Format 

- Most important changes introduced in IPv6: 
    - Expand Addressing capabilities
        - increases size from 32 bit to 128 bit -> this ensure the word will not run out of IP address 
        - introduce a new tye of address: anycast address
            - this allows the datagram to be delivered to any group of hosts 
    - Streamlined 50-byte header 
        - fields from IPv4 have been dropped or made optional -> this allows for a fixed 40-byte header which then allows for faster processing of the IP datagram by a router 
        - new encoding of options allows for a more flexible options processing 
    - Flow labeling: IPv6 has an elusive def of lwo 
        - allows labeling of packets belonging to particular flows for which the sender requests special handling such as non-defualt quality of service or real-time server 
- Fields defined in an IPv6 Datagram:
    - version: 4 bit field -> identifies IP version 
    - traffic class: 8 bit field, can be use to give priority within a flow or to an app
    - flow label: 20 bit field used to identify a flow of datagrams
    - payload length: 16-bit value -> unassigned integer giving the num of bytes in the datagram followed by the fixed-length header of 40 byte 
    - Next header: identifies the protocol to which the contents of this datagram will be delivered (TCP or UDP) -> same value as used in IPv4
    - Hop limit: gets lowered by 1 each time a router forwards the datagram, if it hits 0 the router discards the datagram 
    - Source and dest address
    - Data: payload portion of IPv6 Datagram

- What is no longer used in IPv6 but used in IPv4:
    - fragmentation / reassembly
    - header checksum
    - options 

#### Transitioning from IPv4 to IPv6

- How to transition to IPv6 when the internet is based on IPv4
    - Note: IPv6 can handle IPv4 systems but not vice versa 

- Possible solutions:
    - Flag deciding what day the whole internet transition from IPv4 to IPv6
        - This flag day option is impossible
    - Tunneling : most widely adopted option
        * Tunnel: intervening st of IPv4 routers between two IPv6 routers 
        - how it works:
            - IPv6 node on the sending side takes the entire IPv6 datagram and puts it in the payload field of the IPv4 datagram -> IPv4 datagram is addressed to an IPv6 node  on the receiving side of the tunnel -> then is sent to the first node in the tunnel 
            - the intervening IPv4 routers in the tunnel route the IPv4 datagram among themselves (they are fully unaware that there is an IPv6 datagram in the payload and forward normally)
            - The IPv6 receiving node on the other end of the tunnel eventually receives the IPv4 datagram -> determines that the IPv4 datagram contains an IPv6 datagram (does this by seeing the protocol number field contain 41 indicating that the IPv5 payload is a IPv6 datagram )
            - Extracts the IPv6 datagram and routes the IPv6 datagram exactly as it would if it had received the IPv6 datagram from a directly connected IPv6 neighbored  

## 4.4 Generalized Forwarding and SDN

* flow table -> entry in the match-plus-action in the forwarding table
    - The entry includes:
        - a set of header fields: incoming packet gets matched on these fields 
        - a set of counters: these are updated as packets are matched to the flow table entries 
            - number of packets matched and the time it was last updated
        - a set of actions to be taken when a packet matches a flow table entry
            - this could include:
                - forward the packet, make copies of the packet or rewrite selective headers 
### 4.4.1 Match

- how the OpenFlow 1.0 match-plu-action rule can match on 
    - can match on the 11 packet header fields and the incoming port ID's
- Flow tables an interpret wildcards and can matched on selected fields from three layers of protocol headers 
- Each flow table has an associated priority 
    - if a packet matches multiple flow table entries the selected match and corresponding action will be that of the highest priority entry with which the packet matches 
- Not all fields in the IP header can be matched in a flow table 
    - cannot match on:
        - TTL field or datagram length field 

### 4.4.2 Action

- there is a list of zero or more action that determine the processing that is applied to the packet that matches a flow table entry 
    - if multiple actions then they are preformed in the order of that they are on the list 
- possible actions include:
    - forwarding
    - dropping: a flow table entry with no action indicates that a matched packet should be dropped 
    - Modify-field: the values in the 10 packet header fields (all layer 2,3, and 4 except the IP protocol field) can be re-written before the packet is forwarded to the chosen output port 

### 4.4.3 OpenFlow examples of Match-plus-action in Action 


