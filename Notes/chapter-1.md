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

- Home access: DSL, Cable, FTTH, and 5G fixed wireless
    - two most popular for home networks: 
        * digital subscriber line ( DSL)
            - some line as the home phone so a telco and can become an ISP
            - divides it up as if there were three separate links so that a telephone call and an Internet connection can share the DSL link at the same time
            * Spitter: separates the data and telephone signals arriving to the home and forwards the data signal to the DSL modem
        * cable 
            * Cable Internet Access: makes use of the cable television companys existing cable television infra. 
            - require cable modems 
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

### Physical Media

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

#### Twisted-pair Copper Wire

- least expensive and most commonly used guided transmission medium 
- consists of two insulted copper wire 
* Unshielded twisted pair (UTP): commonly used for computer networks within a building (for LANS)
    - data rates are 

#### Coaxial Cable 

- two copper conductors -> concentric 
- common in cable television systems 

#### Fiber Optics

- thin, flexible medium that conducts pulses of light with each pulse representing a bit
- can support up to 10-100 gigabits per second 
- many long distance telephone networks in the US use fiber optics exclusively 

#### Terrestrial Radio Channels

#### Satellite Radio Channels 
* geostationary satellites
* low-earth orbiting (LEO) satellites 

## 1.3 The Network Core

#### Packet Switching 
* Packets: smaller chunks of data that are being sent to a destination end system 
* Packet switches: packets travels through this and communication links
    - Two types:
        - routers
        - link-layer switches 
    - Time to transmit packet: *L/R seconds* 
        - L -> bits over a link
        - R -> transmission rate bits/sec 

#### Store-and-forward transmission

