# Chapter 3 - Transport Layer Protocol

### Transport layer overview 

* Segment -> transport-layer packet 

* IP -> provides logical communication between hosts 

- IP service model -> best-effort delivery service
    - called unreliable service 
    - each host as an Ip address

- transport layer multiplexing and demultiplexing = extending hosts-to-host deliver to process-to-process

#### Transport services and protocols:

- provide logical communication between application and processes running on different hosts 
    - tcp does not know or care where the segment came from  before
- transport protocols actions in end systems:
    - sender: breaks app messages into segments, passes to network layer
    - receiver: reassembles segments into messages, passes to application layer 
- two transport protocols available 
    - TCp
    - UDP

#### Transport vs network layer services and protocols 

- network layer: logical communication between hosts 
- transport layer: logical communication between processes 
    - relies on an enhances network layer services 

- TCP doesnt care what process communicates with TCP, if  it wants reliable  transfer of the segments 

#### Transport layer actions

- Sender:
    - passes an app layer message
    - determine segment header fields first
    - creates segment 
    - passes segment to IP
- Receiver
    - receives segment from IP
    - checks header values 
    - extracts app layer message
    - demultiplexes messages up to app via socket 

- Internet transport protocols
    - TCP: Transmission control protocol
        - reliable, in order delivery
        - congestion control
        - flow control
        - connection set up
    - UDP: User Datagram protocol
        - unreliable, unordered deliver
        - no frills extension of best effort IP
    - Services not available: delay guarantees and bandwidth guarantees

### Multiplexing and demultiplexing 

* demultiplexing: job of delivering the data in a transport-layer segment to the correct socket 
    - demultipleing at receiver: use header info to deliver received segments to correct socket 
* multiplexing: job of gathering data chunks at the source host from diff sockets, encapsulating each data chunk with header info to create segments, and passing the segments to the network layer 
    - - Multiplexing at sender: handle data from multiple sockets, add transport header 
    - multiplexing requires:
        - sockets have unique identifiers
        - each segment have special fields that indicate the socket in which the segment is to be delivered 
    - THese special fields are source port and dest port 
        - port number range from 0 to 65535
        * well known port numbers: 0 to 1023
#### How demultiplexing works: 
    - hosts receives IP datagrams: 
        - each datagram has source IP address, destination IP address
        - each datagram carries on transport-layer segment 
        - each segment has source destination port number 
    - hosts uses IP address and port numbers to direct segments to appropriate socket 
#### Connectionless demultiplexing -> UDP

- when creating socket, must specify host-local port #
- when creating datagram to send into UDP socket, must specify
    • destination IP address
    • destination port #

- when receiving host receives UDP segment:
    • checks destination port # in segment
    • directs UDP segment to socket with that port #
    Note: IP/UDP datagrams with same dest. port #, but different source IP addresses and/or source port numbers will be directed to same socket at receiving host
 

#### Connection-oriented demultiplexing -> TCP

- Difference between TCP socket and UP socket is TCP socket is identified by a four tuple 

    - TCP socket identified by 4-tuple:
        • source IP address
        • source port number
        • dest IP address
        • dest port number
* If two TCP segment with diff source IP address or source prot number will be directed to two different socket 
- demux: receiver uses all four values (4-tuple) to direct segment to appropriate socket

- server may support many simultaneous TCP sockets:
• each socket identified by its own 4-tuple
• each socket associated with a different connecting client

- Multiplexing, demultiplexing: based on segment, datagram header field values
- UDP: demultiplexing using destination port number (only)
- TCP: demultiplexing using 4-tuple: source and destination IP addresses, and port numbers
- Multiplexing/demultiplexing happen at all layers

### Connectionless Transport: UDP

- UDP: User Datagram Protocol
    - “no frills,” “bare bones” Internet transport protocol
    - “best effort” service, UDP segments may be:
        • lost
        • delivered out-of-order to app
- Other than multiplexing/demultiplixing and error checking -> doesnt add anything else to the IP 
- No handshake prior to sending segments which is what makes it connectionless -> does not create a connection pior 
connectionless:
    • no handshaking between UDP sender, receiver
    • each UDP segment handled independently of others
- UDP use:
    - streaming multimedia apps (loss tolerant, rate sensitive)
    - DNS
    - SNMP
    - HTTP/3
- if reliable transfer needed over UDP (e.g., HTTP/3):
     - add needed reliability at application layer
     - add congestion control at application layer
Why is there a UDP?
    - no connection establishment (which can add RTT delay)
    - simple: no connection state at sender, receiver
    - small header size
    - no congestion control
        - UDP can blast away as fast as desired!
        - can function in the face of congestion
* Reasons to use UDP over TCP:
    - Finer app level control over what data is sent and when
         - App sent to UDP (transport) which then packages the data inside a UDP segment and immediately passes the segment to the network layer 
    - no connection establishment
        - TCP uses a three way handshake before it starts to transfer data 
        - UDP just sends wihtout any connection 
            - This means UDP does not introduce any delay to establish a connection 
            - Most likely why DNS uses UDP vs TCP since if it used TCP it would run a lot slower 
        - QUIC protocol -> used by googles chrome browser -> uses UDP as its underlying transport protocol and implements reliability in an application-layer protocol on to of UDP 
        - No connection State
            - because of thi a server can support many more active clients when the app runs over UDP rather than TCP 
        - Small packet header overhead
            - tcp segment has 20 bytes of header overhead in every segment, UDP has 8 bytes of overhead 
#### UDP segment structure
- UDP header has 4 fields -> each consiting of two bytes 
- port number allow the destination host to pass the application data to the correct processes running on the destination end system to perform the demultiplexing function 
- Length field -> specifies the number of bytes in the UP segment (header plus data)
- checksum is used by the receiving host to check wether errors have been introduced into the segment 

#### UDP checksum VIDEO STOPPED AT 1 hour and 4 min

- UDP checksum provides error detection 
    - it checks to see if the bits within the UDP segment have been altered 
    - at the end you expect the sum to be all 1's, if you see any 0's than you know an error has occurred 
- UDP provides error checking but does not do anything to recover if an error is found 
    - some implementation of UDP discard of it or some pass along the segment with a warning

### Principles of Reliable Data Transfer 

- reliable data transfer occurs in transport layer, link layer, and application layer 
- reliable data transfer gaurantees nothing was corrupted (no 1's flipped to 0's in the checksum)
- challenge is the lower level may be unreliable 
- sending side of the data transfer protocol will be invoked from the following call:
    - rdt_send()
        - rdt = reliable data transfer
        - send indicates that the send side of the rdt is being called
- following is called on the receiving side when a packets arrives 
    - rdt_rcv ()
- deliver_data() -> called when the rdt protocol wants to deliver data to the upper layer 
- unidirectional data transfer -> data transfer from the sending to the receiving side 
    - focusing on this use case there is also bidirectional (full duplex) data transfer -> but follows the same concept but is more tedious to explain 
    - Note: sending and receiving sides of our protocols will need to transmit packets in BOTH directions
- udt_send() -> unreliable data transfer 

### Building a reliable data transfer protocol

#### Reliable Data transfer over a perfectly reliable channel -> rdt1.0

- First case: underlying channel is completely reliable 
- Finite-state machine (FSM) -> rdt 1.0
    - separate FSM for sender and receiver 
- sending side of rdt: accepts data from the upper ;auer voa rdt_send(data)
    - creates a pack via make_pkt(data) and send the packet into the channel 
    - rdt_send(data)
- recieving side of rdt: receives packet from underlying channel via rdt_rcv(packet)
    - removes data from packet via extract(packet,data) and passes the data up to the upper layer via deliver_data(data)

Note: here we are assuming that the receiver is able to receive data as fast as the sender happens to send ata -> so no reason to ask for the sender to slow down 

#### Reliable Data Transfer over a Channel with Bit Errors: rdt2.0 

- more realistic example is one in which bits may be corrupted -> such bit errors typically occur in the physical components of the network as a packet si transmitted, propagates or is buffered 
- Assumption: all bit packets were received in the order they were sent, even if some were corrupted 
* ARQ -> automatic repeat request protocols -> what reliable ata transfer protocols are based on 
    - ARQ protocol capabilities to handle bit errors 
        - error detection: can be found in the checksum field of the data packet 
        - receiver feedback: the only for the sender to learn of the receivers view is for the receiver to provide explicit feedback -> positive (ACK) and negative 
        (NAK) acknowledgement replies -> only 1 bit longs can send 0 or 1 to represent NAK or ACK
        - retransmission: a packet that is received in error at the receiver will be transmitted by the sender 
- when sender is waiting for ACK or NAK it cannot get anymore data 
- when not get a new packet unless it has received the current packet with no errors -> because of this it is known as the stop-and-wait protocol 
- Fatal flaw with this -> doesnt know if ACK or NAK have been corrupted 

- Solution: new field in data packet -> *sequence number* -> sender numbers its data packets 
    - this is adopted by almost all existing data transfer protocols including TCP

- rdt2.1 -> fixed version of rdt2.0 -> rdt2.2 -> is a NAK-free reliable data transfer protocol for a channel with bit errors 

#### Reliable Data Transfer over a Lossy Channel with Bit Errors: rdt3.0 

- assume bit errors and the underlying channel can lose packets as well 
- concerns need to solve: how to detect packet loss and what to do when the packet are lost 
- solution: choose a time value that if the packet is not received it is assumed it is lost and the packet is retransmitted 
- This solution introduces the possibility of *duplicate data packets* in the sender to receiver channel 
    - rdt2.2 has functionality to deal with this  with teh sequence number functionality 
- adds a timer functionality
- Usender = (L/R)/(RTT+ (L/R))
    - finds *Utilization* of sender = the fraction of time the sender is actually busy sending bits in the the channel 
- Send-and-wait protocol is extremely low and wastes bandwidth -> instead of waiting for ack allowing the sender to send packets without hte ack would triple the the utilization 
* Pipelining: sending packets without receiving an ACK or NACK
    - consquences of pipeling:
        - range of seq num must be increased 
        - sender and receiver sides of the protocols may have to buffer more than one packet 
        - range of seq num needed and the buggering requirements will depend on the manner in which a data transfer protocol responds to lost, corrupted and overly delayed packets 
            - two basic approaches toward pipeline error recover
                - Go-Back-N
                - selective repeat 

#### Go-Back-N (GBN)

- allowed to transmit multiple packets without waiting for an ACK  -> but is constrained to have no mor than some max allowable number (N) of un-ACK packets in the pipeline
- [0,base-1] = seq num in the interval correspond to packets have already been transmitted and ACK
- [base, nextseqnum-1] = packets that have been sent but not yet ACK
- [nextseqnum,base+N-1] = packets that can be sent immediately should data arrive from the upper layer 
- seq num greater than or equal to base+N cannot be used until an un-ACK packet currently in the pipeline has been ACK
- reasons to impose a limit on the sender for this protocol is for flow control and TCP congestion control 
- resends all packets if one is lost or corrupted to avoid buffering and out of order packets 

#### Selective Repeat (SR)

- avoids unnecessary retransmission by having the sender retransmit only those packets that it suspects were received in error (lost or corrupted)
- requires the receiver individualy ack correctly received packets 
    - uses size of N to limit the num of outstanding packets in the pipeline
- Sr receiver will ACK a correctly received packet wether or not it is in order
    - out of order packets are buffered until any missing packets (packets with lower seq numbers) are received -> at which point a batch of packets can be delivered in order to the upper layer 

* NOTE: page 224 has a summary of all the mechanism used for reliable data transfer 

### Connection-oriented Transport: TCP

- Handshake must occur before one app process can send data to another app process 
- Note: TCP resides on in the two communicating end system so any routers or link-layer switches is completely unaware of the TCP protocol running
* full duplex service: TCP provides bi directional network data transmission at the same time 
* point to point: always between a single sender and receiver 
* client process -> initiates connection 
    - issues a connection through the following python command:
        clientSocket.connect((serverName,serverPort))  
            - serverName = name of server
            - serverPort = identifies the process on the server 
- first two segements cary no app  data but the third of these segments may carry a payload -> because it takes 3 segments to initiate connection is often referred to has a 3 way handshake

* maximum segment size (MSS) -> max amount of data that can be grabbed and placed in a segment  -> NOTE: MSS is the max amount of app-layer data in the segment and not the max size of the TCP segment including headers 
    - set by determining the length of the largest link-layer frame that can be send by the local sending host (max transmission unit - MTU)

- Then setting the MSU to ensure the TCP segment (when encapsulated in an IP datagram) + TCP / IP header length which is typically 40 bytes will fit in a single link layer frame
- typical value of MSS is 1460 bytes 

#### TCP Segment Structure

- TCP header usually 20 bytes -> 12 bytes more than the UDP header 
- Interactive application often transmit data chunks that are smaller than the MSS -> data field in the TCP segment is often only one byte -> I.E Telnet and SSH
- Fields in a TCP header:
    - source and dest. port numbers
    - checksum field
    - 32-bit sequence num field and 32 bit acknowledgment num field -> used by TCP sender and receiver in implementing a reliable data transfer service 
    - 16 bit receive window-> used for flow control
    4-bit header length field ->length of TCP header -> usually 20 bytes
    - options field -> used when a sender and receiver negotiate the max segment size (MSS)
    - flag field -> 6 bits 

#### Sequence Number adn ACK nums

* sequence number for a segment = the byte-stream number of the first byte in the segment 
- The ack num that Host A put in its segment is the seq num of the next byte Host A is expecting from Host B
- What happens when segements are recieved out of order in TCP?
    - Since RFC does not define it is up to the coder to decide. There are two main options
        1. the receiver immediately discards out-of-order segments (which can simplify receiver deign)
        2. the receiver keeps the out of order bytes an wait for the missing bytes to fill in the gaps 

* Note: telnet case study skipped go back if you have time *

#### Round Trip Time Estimation and Time out

- TCP (like rdt) uses timeout/retransmit mechanism to recover lost segments 
- Subtle issues during implementation:
    - length of the timeout intervals 
        - Time out interval needs to be longer than round trip time (RTT) -> time it would take from when a segment is sent until it is ack 
    - diff is estimating or deciding RTT and deciding time out interval

##### Estimating the Round-Trip time
- SampleRTT = amount of time between when the segment is sent and when an ack for the segment is received
    - grabs it once from a sample that has been transmitted -> never grabs sampleRTT from a retransmitted segment 
- TCP grabs the average to the "typical" RTT and maintains the average -> called EstimatedRTT
    - every time TCP grabs a new SampleRTT it also updates the EstimatedRTT
* EstimatedRTT formulate = 0.875 * EstimatedRTT + 0.125 * SampleRTT
    - estimatedRTT = weighted average of the SampleRTT
- DevRTT -> estimate of how much SampleRTT typically deviates from EstimatedRTT
* DevRTT formula = (1-0.25) * DevRTT + 0.25 * |SampleRTT- |EstimatedRTT
    - if sampleRTT have little fluctuation then devRTT will be small and if sampleRTT has big fluctuation then devRTT will be large 

##### Setting and Managing the Retransmission Timeout Interval

- set the timeout equal EstimatedRTT + margin
    - if set to larger than can cause large data transfer delays 
    - if set to less than, than unnecessary retransmissions would be sent 
- Margin should be large if fluctuation in SampleRTT values are large and small if the fluctuation for SampleRTT values are small 
    - DevRTT comes into play when deciding Margins 
* TimoutInterval = EstimatedRTT + 4 * DevRT
    - an initial TimeoutInterval of 1 sec is recommended
- when a timeout occurs the value of the TimeoutInterval is doubled to avoid premature timeout occurring for a subsequent segment that could soon be ACK

#### Reliable Data Transfer 

- Remember: network-layer service (IP) is unreliable
    - bits can be lost, datagrams come out of order, datagrams can get corrupted (flipped 0to 1 and vice versa)
- transport layer segments are carried across the network by IP datagrams -> transport-layer segment can suffer from these problems
- TCP reliable data transfer ensures that the data stream that process reads out of its TCP receive buffer is uncorrupted, without gaps, without duplication, and in seq. 
- TCP uses a single re-transmission timer to reduce overhead 
- Timer expiration interval is the TimeoutInterval 
- Timeout -> TCP retransmits the segment that caused the timeout
    - it then restarts the timer
- TCP needs to handle the arrival of an ACK segment from the receiver -> segment containing a valid ACK field value
    - TCP compares ACK value y with its variable SendBase
        - SendBase = seq number of the oldest un-ACK byte
        - SendBase - 1 = seq num of the of the last byte that is known to have been received correctly and in order at the receiver 
    - If y>SendBase then the ACK is acknowledging one or more previously un-ACK segments -> if so sender updates its SendBase variable 
- Doubling the TimeoutInterval
    - TCP will double the timeout variable every time the timeout event occurs -> the timeout variable grows exponentially 
    - every time timer restarts because ACK is received it gets it from the original TimeoutInterval
    - This helps with congestion control -> most likely occurring because to many packets in the queue which is causing packets to be dropped
- Fast Retransmit 
    * duplicate ACK - an ACK that re-acknowledges a segment for which the sender has already received an earlier acknowledgement 
    - fast retransmit -> retransmitting the missing segment before that segments timers expires 

##### Go-Back-N or Selective Repeat?

* selective acknowledgement -> this allows a TCP receiver to acknowledge out of order segments selectively rather than just cumulatively acknowledging the last correctly received in order segment 

- TCP is a hybrid of GBN and selective repeat 

#### Flow Control 

- has flow control service to eliminate the possibility of the sender overflowing the receivers buffer with too much data too quickly 
- speed matching service: matching the rate at which the sender is sending against the rate at which the receiving app is reading 
* Note we assume that TCP implementation discards out-of-order segments for the explanation of flow control
* Receive window - variable maintained by sender 
    - used to give the sender an idea of how much free buffer space is left at the receiver 
    - RcvBuffer -> receive buffer window variable 
    - Defines the following vars in Host B (Receiver Host)
        - LastByteRead: the num of the last byte in the data stream read from the buffer by the app process 
        - LastByteRcvd: the num of the last byte in the data stream that has arrived from the network and has been placed in the receive buffer 
- Allocated buffer: LastByteRcvd - LastByteRead <= RcvBuffer 
- rwnd = receive window
    - set to the spare room in the buffer
    - rwnd = RcvBuffer - [LastByteRcvd-LastByteRead]
    - rwnd is dynamic because vars change over time 
- Host B (receiver host) tells Host A (sender host) hopw much spare room it has in the connection buffer by placing its current value of rwnd in the receive window field of every segment it sends to host A 
    - initially host b sets rwnd = RcvBuffer 
- Host A (sender host) keeps track of two vars:
    - LastByteSent and LastByteAcked
        - diff between the two vars (LastByteSent - LastByteACked) is the amount of UN-ACK data that A has sent into the connection 
        - By keeping the amount of UN-AWK data less than the value of rwnd -> Host A is assured that it is not overflowing the receive buffer at Host B -> Host A makes sure throughout the connect life that 
            - LastByteSent - LastByteAcked <= rwnd 
- When rwnd gets to 0 on host B -> host A stops sending data -> however since host b does not send data to host A unless its an ACK then host A would never know when space opened up in host B and would send data
    - Resolution: Host A sends 1 segments with 1 data byte when Bs receive window = 0 -> these segments will be ack by the receiver -> eventually the buffer will begin to empty and the acknowledgments will contain a nonzero rwnd value 

#### TCP Connection Management 

- TCP connection is important because it can significantly add delays and is vulnerable to attack 
    - i.e syn flood attack 

*How a connection is established in TCP*

1) client-side TCP sends a special TCP segment to the server-side TCP 
    - segment contains no app layer data
    - 1 flag bit in segment header -> SYN bit -> set to 1
    - client randomly chooses the initial seq num (client_isn)-> puts this num in the seq num field of the initial TCP SYN segment 
        - this segment is encapsulated within an IP datagram and sent to the server 
        - important to properly randomize the client_isn in order to avoid certain security attacks 

2) Once it arrives -> server extracts the TCP SYN segment from the datagram -> allocated the TCP buffers and vars to the connection and sends a connection granted segment to the client TCP
    - allocation of these variables before completing step 3 of the three way handshake makes TCP vulnerable to denial-of-service attack known as SYN flooding
    - does not contain app layer data but contains the following
        1) SYN bit set to 1
        2) ack field of the TCP segment header is set to client_isn+1
        3) server chooses its own initial seq num (Server_isn) -> puts value in seq num field of the TCP segment header 
    - Connection-granted segment is called SYNACK segment
        - this states that the server has received the SY packet to start a connection with the client initial seq num (client_isn) -> the server agrees to establish a connection and sets its own seq num to server_isn
3) when receiving SYNACK segment -> client also allocates buffers and variables to the connection 
    - client host sends the server another segment -> this last segment of the three way handshake acks the servers connection-granted segment -> does so be putting the server+isn+1 in the ack field of the TCP segment header   
    - the SYN bit is set to zero since the connection is established
    - the third stage of the 3 way handshake may carry client-to-server data in the segment payload

- once all steps completed the client and server host can send segments containing data to each other 
- Since three packets are sent to establish a connection this procedure if referred too as a three-way handshake 

*How TCP closes a connection*

- resources (buffer and vars) are deallocated
- client decides to close connection and issues close command
    - client TCP sends a special TCP segment to the server process containing a flag bit in the segment header -> the FIN bit set to 1

*Diff states during a TCP connection*

- Client TCP phase
    -> Closed -> initiating TCP connection -> SYN-SENT state -> Established state 
        - while in the established state the TCP client can send and receives TCP segments containing payload data 

- What happens if the host receives a TCP segment whose port numbers or source IP address do not match with any of the ongoing sockets in the host
    - i.e TCP SYN packet with dest port 80 but web server is not accepting connection on port 80
        - TCP segment will send a reset flag -> RST flag bit set to 1 
    * Note for UDP: when a host sends a upd packet whose dest port number doesnt match an ongoing UDP socket -> host sends a special ICMP datagram 

*Deeper dive into namp with TCP*

- Exploring a TCP port (i.e 6789) on target host -< nmap will send a TCP SYN segment with the dest prot 6789 to that host. There are three possible outcomes
    1. The source host recieves a TCP SYNACK segment from the target host
        - this means the app is running with TCP port 6789 on the target -> nmap returns "open"
    2. The source host receives a TCP rest segment from the target host
        - SYN segment reached target host but the host is not running an app with TCP on port 6789 
        - what we do know: the segments destined to the host at port 6789 are not blocked by any firewall on the path between source and target hosts
    3. sources receives nothing 
        - likely means SYN segment was blocked most likely by firewall and never reached the host 

### Principles of COngestion Control 

#### Causes and Costs of Congestion

*Scenario 1: Two senders, a Router with Infinite Buffers*

* Per connection throughput -> number of bytes per second at the receiver 
- when sharing a connection the throughput can only ever reach R/2 no matter that rate of Host A or Host B
- Consequence of reaching near rate capacity: delay becomes larger 
* One cost of congested network: large queuing delays are experienced as the packet-arrival rate nears the link capacity 

*Scenario 2: Two senders and a Router with Finite Buffers*

- Finite buffer: means once the buffer is full the packets will be dropped 
- Assuming connection is reliable which means if a packet is dropped it will be retransmitted 

* Another cost of congested network - sender must preform restranmissions in order to compensate for dropped packets due to buffer overflow
* Another cost: unneed retransmissions by the sender in the ace of large delays may cause a router to use its link bandwidth to forward unneeded copies of a packet 

*Scenario 3: Four senders, Routers with Finite Buffers and Multihop Paths*

* Another cost: when a packet is dropped along a path, the transmission capacity that was used at each of the upstream links to forward that packet to the point at which it is dropped ends up having been wasted 

### TCP Congestion Control 

#### Classic TCP congestion control

- TCP has each sender limit the rate at which it sends traffic into its connection 
- How TCP sender limits the rate at which it sends traffic into its connection:
    - Establishes a var: *Congestion Window* -> denoted by cwnd
    - this var imposes a constraint on the rate at which a TCP sender can send traffic into the network 
    - the amount of un-ACK data cannot exceed the min of cwnd and rwnd
        - LastByteSent - LastByteAcked <= {cwnd,rwnd}
- Senders rate is roughly: cwnd/RTT bytes/sec
    - by adjusting the value of cwnd the sender can therefore adjust the rate at which it sends data into its connection 
* self-clocking -> using ACK to trigger (or clock) its increase in congestion window size

- Lost segment implies congestion -> the tcp sender rate should be decreased when a segment is lost 
- an ack segment indicates that the network is delivering the senders segments to the receiver and hance the senders rate can be increased when an ack arrives for a prev. un-ACK segment 
    - assumes all is going well and there is no congestion so the congestion window size can be increased 
- bandwidth probing
    - continously checking the transmission rate by probing it

#### Review of the TCP congestion control alogthrim 

* The Alogrighm contains 3 components: slow start, congestion avoidance, and fast recover 
    - 1 and 2 are mandatory for TCP but the third is just highly recommended 

##### Slow start

- When TCP connection begins -> cwdn is typically initialized to 1 MSS (small value) -> initial sending rate is roughtly MSS/RTT
- Goal: quickly find out how much bandwidth is available
- TCP sender starts off with 1 MSS and increase by 1 MSS every time a transmitted segment is frist ack
- Every RTT the sending rate doubles
    - starts slow but then grows exponentially during this phase
- when does it stop to grow?
    - if there is a loss event (congestion) indicated by a timeout -> TCP sender sets the value of vwnd to 1 and begins the slow start process a new
        - also sets ssthresh (slow start threshold) to cwnd/2 = half the value of the cwnd when the conegestion was last detected 
    - if cwnd = ssthresh -> slow start ends and TCP transitions into congestion avoidance mode
    - if 3 duplicate ACKs are detected, in which case TCP performs a fast retransmit and enters the fast recovery state 

##### Congestion Avoidance 

- enter this state when cwnd is half its value when congestion was last encountered, so need to be careful not get back to a congested state
    - does this by only adding 1 mss every RTT rather than doubling it 

- TCP congestion control is often referred to as additive-increase, multiplicative-decrease (AMID) form of congestion control

- most popular web servers are running a version of TCP cubic and is the defaults version in the linux operating system
