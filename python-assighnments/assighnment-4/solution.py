from socket import *
import os
# from statistics import stdev
import statistics
import sys
import struct
import time
import select
import binascii
# Should use stdev

ICMP_ECHO_REQUEST = 8


def checksum(string):
    csum = 0
    countTo = (len(string) // 2) * 2
    count = 0

    while count < countTo:
        thisVal = (string[count + 1]) * 256 + (string[count])
        csum += thisVal
        csum &= 0xffffffff
        count += 2

    if countTo < len(string):
        csum += (string[len(string) - 1])
        csum &= 0xffffffff

    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer



def receiveOnePing(mySocket, ID, timeout, destAddr):
    timeLeft = timeout
    # time at which you recieve the packet and time at which you send the packet 
    # calc vars based off of the round trip time -> how much time passed
    while 1:
        startedSelect = time.time() #returns time as a floating point number 
        whatReady = select.select([mySocket], [], [], timeLeft) 
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []:  # Timeout
            return "Request timed out."

        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)
        icmpHeader = recPacket[20:28]
        icmpType, code, theChecksum, recID,seq = struct.unpack('bbHHh', icmpHeader) 
        # if something:
            #data_time = struct.unpack('d',??)
            #RTT = timeReceived - data_time
            #return RTT

        # Fill in start
        
        if recID == ID:
            bytesInDouble = struct.calcsize("d")
            timeSent = struct.unpack("d", recPacket[28:28 + bytesInDouble])[0]
            return timeReceived - timeSent
        # Fetch the ICMP header from the IP packet

        # Fill in end
        timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            return "Request timed out."


def sendOnePing(mySocket, destAddr, ID):
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)

    myChecksum = 0
    # Make a dummy header with a 0 checksum
    # struct -- Interpret strings as packed binary data
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("d", time.time()) # current time when the packet is being built, can extract this time and subtract from the time you recieved theresponse = RTT
    # Calculate the checksum on the data and the dummy header.
    myChecksum = checksum(header + data)

    # Get the right checksum, and put in the header

    if sys.platform == 'darwin':
        # Convert 16-bit integers from host to network  byte order
        myChecksum = htons(myChecksum) & 0xffff
    else:
        myChecksum = htons(myChecksum)


    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data

    mySocket.sendto(packet, (destAddr, 1))  # AF_INET address must be tuple, not str


    # Both LISTS and TUPLES consist of a number of objects
    # which can be referenced by their position number within the object.

def doOnePing(destAddr, timeout):
    icmp = getprotobyname("icmp")


    # SOCK_RAW is a powerful socket type. For more details:   https://sock-raw.org/papers/sock_raw
    mySocket = socket(AF_INET, SOCK_RAW, icmp)

    myID = os.getpid() & 0xFFFF  # Return the current process i
    sendOnePing(mySocket, destAddr, myID)
    delay = receiveOnePing(mySocket, myID, timeout, destAddr)
    mySocket.close()
    return delay


def ping(host, timeout=1):
    # timeout=1 means: If one second goes by without a reply from the server,  	
    # the client assumes that either the client's ping or the server's pong is lost
    # packet_min = 0.00
    # packet_avg = 0.00
    # packet_max = 0.00
    # stdev_var = 0.00
    # stdev = 0.00
    dest = gethostbyname(host)
    print("Pinging " + dest + " using Python:")
    print("")
    
    #Send ping requests to a server separated by approximately one second
    #Add something here to collect the delays of each ping in a list so you can calculate vars after your ping
    delay_lst = []
    for i in range(0,4): #Four pings will be sent (loop runs for i=0, 1, 2, 3)
        delay = doOnePing(dest, timeout)
        print(delay)
        delay_lst.append(delay)
        time.sleep(1)  # one second
    # collect delays and then calculate the vars based off of that list 
    #You should have the values of delay for each ping here; fill in calculation for packet_min, packet_avg, packet_max, and stdev
    print(delay_lst)
    packet_delay_added = 0
    if len(delay_lst) > 0:
        packet_min = delay_lst[0]
        packet_max = delay_lst[0]
    else:
        print("Error no delays listed")
    for i in delay_lst:
        print(i)
        packet_delay_added += i 
        if i > packet_max:
            packet_max = i
        if i < packet_min:
            packet_min = i
    vars = [str(round(packet_min, 8)), str(round(packet_delay_added / 4, 8)), str(round(packet_max, 8)),str(round(statistics.stdev(delay_lst), 8))]
    # print(vars)
    return vars

if __name__ == '__main__':
    ping("google.co.il")
    # ping("127.0.0.1")
