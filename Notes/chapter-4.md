# Chapter 4: Network Layer: Data Plan

- There is a piece of the network layer in each and every host and router in the network

* data plane: determines how a datagrams is forwarded

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
