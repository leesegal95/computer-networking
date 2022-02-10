# Chapter1 -> Introduction 

* term used / defintion

- notes

## 1.1 What is the internet?

* Hosts / end systems: devices that are hooked up to the internet 

- End system are connected together by communication links and packet switches

* transmission rate: rate at which the a link transmits data -> measured by bits/second

* Internet Service Providers (ISP): method which end systems access the Internet

* Protocols: control the sending and receiving of information within the Internet
    * Transmission Control Protocol (TCP)
    *  Internet Protocol (IP)
        - Specifies the format of the packets that are sent and received among routers and end systems
    * TCP/IP : the internets principal protocols

* Internet Standard: created by Internet Engineering Task Force (IETF)
    * IETF standards documents are called requests for comments (RFC)
        - define protocols such as TCP / IP/ HTTP(for the web), and SMTP (for email)

- Internet : a service description
    - can also be described as an infrastructure that provides services to applications 
    * distributed applications: they involve multiple end systems that exchange data with each other 
    - important internet apps run on end systems -> not on packet switches 

* socket interface: set of rules that the sending program must follow so that the internet can deliver the data to the destination program 

* Network Protocol: defines the format and the order of messages exchanged between two or more communicating entities as well as the actions taken on the transmission and/or receipt of a message or other event

## 1.2 Network Edge

* access network: the network that physically connects an end system to the first router (edge router) on the path from the end system to any other distant end system

- network edge refers to clients and servers that sit at the edge of the infrastructure 
    - i.e fridge, cameras, car, iphones
    - servers often sit in the data centers 

- access networks, physical media -> part of the network edge structure 
    - wired / warless communication links 
    - starling 

- Access networks and physical media:
    q: how to connect end systems to edge router?
        - residential access networks (home)
        - institutional access networks (school, company)
        - mobile access networks (WiFi, 4G,5G)
    q: What to look for:
        - transmission rate (bits per seconds) of access network 
        - shared or dedicated access among users 


- Home access: DSL, Cable, FTTH, and 5G fixed wireless
    - two most popular for home networks: 
        * digital subscriber line ( DSL)
            - use  exsiting telephone line to central office DSLAM
                - DSLAM -> DSL access multiplexer 
                - data over DSL phone goes to internet
                - voice over DSL phone line goes to telephone net 
            - 24-53 Mbps dedicated downstream transmission rate 
            - 3.5-16 Mbps dedicated upstream transmission rate 
            - some line as the home phone so a telco and can become an ISP
            - divides it up as if there were three separate links so that a telephone call and an Internet connection can share the DSL link at the same time
            * Spitter: separates the data and telephone signals arriving to the home and forwards the data signal to the DSL modem
        * cable 
            * Cable Internet Access: makes use of the cable television companys existing cable television infra. 
            - require cable modems 
            - Access Networks: Cable-based access: uses diff type of modulations to move the data through the wire 
                - Frequency division multiplexing (FDM): different channels transmitted in different frequency bands 
                    - diff channels operating at diff freq
                    - freq used for video provides us with uninterrupted connection
                    - data runs idd, there can be delayed -> as long as it arrives in the same order it doesnt have to be continuos 
                - HFC: hybrid fiber coax
                    - asymmetric: up tp 40 Mbps - 1.2 Gbs downstream transmission rate, 20-100 Mbps upstream transmission rate
                    - network of cable, fiber attaches homes to ISP router
                    - homes share access network to cable headend 
                - cable based network access is a shared network 
        - Difference between DSL and Modem connection
            - DSL was on connection -> did not have to dial up 
                - DSL offers diff freq other than voice 
            - dial up modem -> virtual circuits -> take over the phone connection 
                - operated over the same frequency as used to transfer the data 
        * fiber at home (FTTH)
            - provides higher speeds than DSL and Cable 
            - provides an optical fiber path from the CO (Central Office) directly to the home 
            - potential provide rates in the gigabits per second range 
            - direct fiber -> one fiber leaving the central office then splits off when its gets home to the actual homes
            - two competing optical distribution networks arch that perform this spitting;
                * active optical networks (AON): switched ethernet 
                * passive optical networks (PON):
                    - used in Verizons FiOS service 
                    * Optical network terminator (ONT) -> each home has one which is an optical fiber dedicated to a neighborhood splitter 
                    * splitter: combines a number of homes (typically less than 100) onto a single, shared optical fiber 
                    * Optical line terminator (OLT): splitter connects to the OLT
                        - the OLT connects to the Internet via a telco router 
                        - at home: users connect a home router to the ONT and access the internet via this home router 
        * 5G fixed wireless 
            - promises high-speed residential access without having to install cabling from the telco CO to the home 

### Access in Enterprise (and the Home): Ethernet and WiFi

* Local Area Network (LAN): commonly used in home settings to connect an end system to the edge router 
    - ethernet is most popular access technology in corporate, university and home networks
* wireless LAN (WIFI)-> wireless users trasmit / receive packets to/from an access point that is connected into the enterprises network (most likely using wired ethernet) -> connected to the wired internet

- Wireless access networks :

- wireless local area networks: WiFI -> WLANS
    - high transmit rate 
- wide area cellular access networks 
    - provided by mobile, cellular network operator
- difference:
    - diff tech, diff ways of communicating, diff transmission rate 
    - speeds and configs are different 

enterprise networks:

- mix of wired, wireless link tech, connecting a mix of switches and routers 
    - ethernet: wired access at 100 Mbps, 1 Gbps, 10 Gbps
    - WiFi: wireless access points 
- 
### Physical Media

*Important Definitions: Links - physical media*
    * bits: propagates between transmitter / receiver pairs 
    * physical link: what lies between transmitter and reciever 
        * guided media: signals propagate in solid media: copper, fiber, coax 
        * unguided media: signals propagate freely -> radio 
    * twisted pair (TP): two insulated copper wires 
        - category 5: 100 Mbps, 1 Gbps Ethernet
        - category 6: 10 Gbps, ethernet 
        - twist in the wires to reduce noise reduction 
        - why do we need shielding:
            - for electrical interference - EMI
            - if you design a network and you run a wire net to florescent lights -> your ethernet switch starts to show a lot of errors and cannot transit
            - use shielding to protect the wires from outside elements 

- HFC: combination of fiber cable and coaxial cable
- DSL & Ethernet: copper wire
- mobile access networks: radio spectrum 
* Physical medium: takes a physical form
    - ex) twisted-pair copper wire, coaxial cable, multimode fiber-optic cable
    - Fall into two categories:
        * guided media:
            - go through a solid medium (physical thing)
            - i.e fiber-optic cable, twisted-pair copper wire, or a coaxial cable
        * unguided media
            - waves propagate in the atmosphere and in outer space 
            i.e wireless LAN or digital satellite channel 

#### Twisted-pair Copper Wire (TP): 

- least expensive and most commonly used guided transmission medium 
- consists of two insulted copper wire 
* Unshielded twisted pair (UTP): commonly used for computer networks within a building (for LANS)
    - data rates are 
- category 5: 100 Mbps, 1 Gbps Ethernet
- category 6: 10 Gbps, ethernet 
- twist in the wires to reduce noise reduction 
- why do we need shielding:
    - for electrical interference - EMI
    - if you design a network and you run a wire net to florescent lights -> your ethernet switch starts to show a lot of errors and cannot transit
    - use shielding to protect the wires from outside elements 

#### Coaxial Cable 

- two concentric copper conductors
- common in cable television systems 
- bidirectional
- broadbrand:
    - multiple frequency channels on cable
    - 100 Mbps per channel 

#### Fiber Optics

- glass fiber carrying light pulses -> each pulse a bit 
- high-speed operation:
    - high-speed point-to-point transmission 
    - - can support up to 10-100 gigabits per second 
- low error rate"
    - repeaters spaced far apart
    - immune to electromagnetic noise 
- in factories and such you must use fiber optics because of the low error rate 
- thin, flexible medium that conducts pulses of light with each pulse representing a bit
- many long distance telephone networks in the US use fiber optics exclusively 

#### wireless radio
- signal carried in electromagnetic specturm
- no physical wire
- broadcast and half-duplex 
- propagation environment effects:
    - refection
    - obstruction by objects
    - interference 

#### Radio link types:

-  Terrestrial Radio Channels-> terrestrial microwave
    - up to 45 Mbps channels
- Wireless Lan (WiFi)
    - up to 100 Mbps
- Wide area (cellular)
    - 4G = 10s Mbps
- Satellite Radio Channels 
    * geostationary satellites
    * low-earth orbiting (LEO) satellites 
    - up to 45 Mbps per channel
    - 270 mse end-end delay

## 1.3 The Network Core

- interconnected routers , networks of networks 
- core responsibility is to pick up the packet as fast as it can and move it to another router as fast as it can
- destination based routing -> inside thee core -> figure out where you are going and forward that way 

### Packet Switching 
* Packets: smaller chunks of data that are being sent to a destination end system 
- in packet swithcing hosts break application - layer message into packets -> forwards packets from one router to the next, across links on path from source to destination 
* Packet switches: packets travels through this and communication links
    - Two types:
        - routers
        - link-layer switches 
    - Time to transmit packet: *L/R seconds* 
        - L -> bits over a link
        - R -> transmission rate bits/sec 
- Host: sends packets of data 
    - host sending function:
        - takes app message -> breaks into smaller chunks knows a *packets*, of length of L bits 
    - transmits the packet into access network at transmission rate of R 
        link transmission rate -> link capacity -> link bandwidth 
* Packet transmission delay: time needed to transmit L bits packet into the link 
    - Number of bits over transmission rate (bits/seconds ) --> L (bits) / R
#### Store-and-forward transmission

* Store and forward transmission: packet switch must receive the entire packet before it can begin to transmit the first bit of the packet onto the outbound link 
* incident links: switch incoming packet onto an outgoing link 
- Calculating the amount of time that elapses from when the source begins to send the packet until the destination has received the entire packet (ignoring propagation delay)
    * Propagation delay: time it takes for the bits to travel across the wire at near the speed of light 
        - source begins to transmit at time 0
        - L/R seconds -> source has transmitted the entire packet and the entire packet has been received and stored in router  
        - L/R seconds -> the router has received the entire packet -> can start transmitting the packet onto the outbound link towards the destination 
        - 2L/ R -> router has transmitted the entire packet and the entire packet has been received by destination 
- Total delay for store and forward transmission is 2L/ R
- If router sent packets as they where received then the total delay would by L/R
* End to end delay: 2L/R assuming zero propagation delay
    - N = Links 
    - R = rate 
    - L = Bits 
* transmission delay: takes L/R seconds to transmit (Push out) L-bit packet into the link at R bps 
#### Queuing Delays and Packet Loss

* Packet queuing and loss: if arrival rate (in bps) to link exceeds transmission rate (bps) of link for a period of time:
    - oackets will queue, waiting to be transmitted on output link
    - packets can be dropped (lost) if memory (buffer) in router fills up 
* Output buffer (output queue): stores packets that the router is about to send into that liknk
    - every packet switch has one
    - key role in packet switching 
* Queuing delays : when a packet needs to wait in an output buffer since the link is busy with another packet 
    - additional delay on top of store and forward delays 
* packet loss: when a buffer is completely full with other packets waiting for transmission -> either the arriving packet or one of the already queued packets will be dropped 

#### (From Lecutre) Two key Network-core functions

- forwarding
    - local action: move arriving packets from routers input link to appropriate router output link 
    - when the packet arrives -> looks at dest addrs -> the router looks up the dest addrs. 
    - forwarding decisions gets made at the input port 
- routing 
    - determine end to end source of destination path which is done by the algorithms 
    - global action: determine source-destination paths taken by packets 
    - routing algorithms 
- every time there is a change in the network the routing algorithms re-cacute the network and put updated information into the input forwarder 
- ARP protocols -> address resolution protocol 

#### Forwarding Tables and Routing Protocols

- Forwarding done in the Internet:
    - Source includes the destinations IP address in the packet headers 
    - each router has forwarding tables 
    * Forwarding tables: maps destination address ( or portions of the destination address) to the routers outbound links 
    - Internet has a number of *Special routing protocols* that are used to automatically set the forwarding tables 

- Packet switching has a queue and delays since it does not reserve resources and uses whatever resources are on demand 
    - i.e a restaurant that does not require or accept reservations -> do not need to call in advance but when arriving at the restaurant are not sure if there will be availability 

### Circuit Switching 
- Two approaches to moving data through a network of links and switches: Packet switching & *Circuit switching*
- can take the circuit and reserve the entire operation of the circuit for transmission weather you have something to transmit or not 
- Has reserved resources 
    - i.e a restaurant that requires reservation, needs to call in advance but guaranteed spot when you arrive 
    - traditional telephone networks use circuit-switched networks 
* Circuit: path between two or more points along which an electrical current can be carried 
    - when the network establishes the circuit it also reserves a constant transmission rate in the networks links for the duration of the connection 
    - since the transmission rate is reserved you have a guaranteed constant rate
- dedicated resources: no sharing 
    - circuit like gauranteed performance 


#### Multiplexing in Circuit-Switched Networks -> modulation technologies 

Circuit in a link is implemented with either:

* Frequency-division multiplexing (FDM)
    - the link dedicates a frequency band to each connection for the duration of the connection
    * bandwidth: width of the band 
    - FM radio stations use FDM to share the frequency spectrum between 88 MHz and 108 MHz -> each station gets allocated a specific frequency band 
    - allows u to take a band and divide it into 4 bands -> transmits at 1/4 bandwidth 

* time-division multiplexing (TDM)
    - divided into frames of fixed duration and each frame is divided into a fixed number of time slots -> when a connection is established the network dedicates one time slot in every frame to this connection 
    - full advantage of the bandwidth but can only transmit at a certain time -> this is divided up by time slots 
        - 4 users get 15 min slot -> get full bandwidth but only get to talk 15 min of an hour 

- since resources are allocated in advance if someone is not using them then they go to waste -> one reason some are not a fan of circuit switching 

#### Packet Switching vs Circuit Switching

- packet switching is great for burst to data
    - resource sharing
    - simpler, no call setup
- circuit switching is great for audio and video applications 
Critics on packet switching:
- not suitable for real-time services (telephone call and video conference calls) because of its variable and unpredictable end to end delays

Proponents of packet switching:
- offers better sharing of transmission capacity then circuit switching 
- simpler, more efficient and less costly to Implement then circuit switching 
- more efficient 
    - packet switching provides the same performance as circuit switching but *does so while allowing for more than three time the number of users* 

- Packet switching reserves based on demand so less waste while circuit switching pre-saves the bandwidth so goes to waste if the demand is not there 

### A Network of Networks 

- Network of networks is the idea of connecting ISP themselves 
    - goal: interconnect the access ISP so that all end systems can send packets to each other 
* PoP (points of presence) : simply a group of one or more routers (at the same location) in the providers network where customers ISP's can connect into the provider ISP
* Peer: ISP can directly connect their networks together so that all the traffic between them passes over the direct connection rather than through upstream media
    - a way to lower costs 
    - when ISP peer its usually no extra charge 
* Internet Exchange Point (IXP): meeting point where multiple ISP can peer together 
* content provider networks: google is the biggest example 
- Hosts connect to Internet via access Internet Service Providers (ISP)
    - residential, enterprise (company, university, commercial) ISPs
- Access ISPs in turn must be interconnected
    - so that any two hosts can send packets to each other
- Resulting network of networks is ery complex
    - evolution was driven by economics and national policies 

- large number of global ISP that are interconnected to each other 
    - internet exchange point -> inter connection -> bring multiple ISP connections together 
    - peering link: connect to other ISP
    -regional ISP - that can connect assets to access ISP
        - access ISP charge subscribers to make money
- content provide network 
    - google, microsoft, amazon 

Internet Structure: a "network of networks"

at "center": small # of well-connected large networks 

- tier-1 commercial ISPs -> national and international coverage
- content provider networks (google, facebook): private network that connects its data centers to Internet, often bypassing tier-1 regional ISPs

### Delay, Loss, and Throughput in Packet-Switched Networks 

#### Overview oF Delay in Packet-Switched Networks 

- packet loss: arrival rate to link (temp.) exceeds output link capacity 

Delays packet suffer from several types of delay at each node:

* Total Nodal delay -> accumlation of all of the following delays:
    * nodal processing delay
        * processing delay: the time required to examine the packets header and determine where to direct the packet 
        - processing delay on high speed routers are on the order of microseconds or less 

    * queuing delay
        * delay caused by waiting to be transmitted onto the link 
        - length of queuing delay depends on the number of earlier-arriving packets that are queued and waiting to be transmitted onto the link 

    * transmission delay
        * L/R -> the time it takes to push (transmit) all of the pakcetds bits into the link 
        - typically microseconds to miliseconds  

    * propagation delay 
        * time it takes to propagate from the beginning of the link to router B
        - propogates at the propagation speed of the link which changes based off of the physicall medium of the link
        - Range of:
            input photo here
        - propagation delay is the distance between two routers divided by the propagation speed: d/s
            - d = distance between router A and router B
            - s = propagation speed of the link 
        - NOT dependent on the size of the packet 

- performance of internet app are greatly affected by network delays 

    * packet queuing delay
        - the more cars the delay grows exponential 
        - R: link bandwidth (bps)
        - L: packet length (bits)
        - a: average packet arrival rate 
        La / R
- real internet delays and routes 
    - traceroute: cool tool to use
        - can go see delays 
- throughput: rate (bits / time unit) at which bits are being sent from sender to receiver 
    - instantaneous: rate at given point in time
    - average: rate over longer period time 
## 1.5 Protocol Layers and Their Service Models 

* Protocol stack: protocols of the various layers

* Protocol: responsible for defining the format, order of messzge sent and received among network entities and actions taken on msg transmission, receipt 

#### Application Layer 

- internet application protocols:
    - HTTP protocl (provides for web document request and transfer)
    - SMTP (protocol for transfer of email messages)
    - FTP (protocol for transfer of files between two end systems )
    - DNS 

* message = packet of information 

#### Transport Layer 

- transports application layer messages 
- two types:
    - TCP
    - UDP
- Segment = transport layer packet

#### Network Layer

* datagrams: network layer packets 

- deliverers the segment to the transport layer in the destination host

#### Link Layer

- example protocols: Ethernet, WiFI, cable address networks DOCSIS

* Frames = link layer packets 

#### Physical layer

- moves the individual bits within the frame from one node to the next 

### Networks under attack 

#### Network attack
* malware -> infects devices and can cause harm 
    * botnet
    * virus: self-replicating infection by receiving / executing object -> email attachment 
    * worm: self replicating infection by passively receiving object that gets itself executed 
* spyware malware -> can record keystrokes, web sited visiting, upload info to collection sites
- infected host can be enrolled in botnet -> used for spam or distributed denial of service (DDoS) attacks 
* Denial-of-service-attacks (DoS)
    - renders a network host or other piece of infra unusable by legit users 
- DoS attacks fall into 3 categories:
    * Vuln attack: sending messages to a vuln application or system -> sent in the right seq of packets then a service can stop or host can crash
    * Bandwidth flooding: sending so many packets the targets access link gets clogged ->legit packets cannot reach server
    * connection flooding: sends so many fake connections it overflows the network so it cannot accept legit connections 
- Distributed DoS (DDoS) attack: attacker controls multiple sources and each source blast traffic at the target ->extremely common with botnet 
- packet interception
    - packet sniffing: 
        - broadcast media 
- Fake identity
    - IP spoofing: send packet with false source address 
