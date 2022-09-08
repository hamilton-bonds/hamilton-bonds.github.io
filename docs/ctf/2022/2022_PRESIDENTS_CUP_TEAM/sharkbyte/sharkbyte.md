# Sharkbyte! Ooh ha ha!
## Analyze Spaceship Network Traffic

**NICE Work Roles**
Data Analyst

**NICE Tasks**
T0366 - Develop strategic insights from large data sets.
T0342 - Analyze data sources to provide actionable recommendations.

**Background**
There are two different subnets on the Dauntless Spaceship that have network traffic on them -- the Engine subnet and the Sensor subnet.

The traffic within the Engine subnet is not understood by anybody on board. Documentation is limited. You must identify how the Spaceship Engine Monitoring System (SEMS) works so we can understand if it becomes compromised in the future (or even now!)

The Sensor subnet may have been compromised. You must answer the questions to identify if an IP address is sending out spoofed/illegitimate sensor status updates to the server on the Dauntless Sensor System (DSS).

**Getting Started**
The Engine subnet traffic is available as an ISO on the provided Kali workstation. Questions Engine Q[1-6] are related to this pcap. Some guidance regarding the custom SEMS protocol is found within the ISO. ONLY USE THE DEFAULT WIRESHARK CONFIGURATION PROFILE (as user or root). UNAPPLICABLE PROTOCOLS HAVE BEEN DISABLED ON THIS PROFILE. ALL UDP/6186 TRAFFIC IS ASSOCIATED WITH SEMS.

The Sensor subnet traffic is only available on the Ubuntu Server (via ISO) due to network segmentation. You must run the command sudo mount /dev/cdrom /media to be able to view the pcap in the /media directory. You may want to copy this pcap to your home directory for analysis. Questions Sensor Q[1-4] are related to this pcap. Tools such as tshark, tcpdump, and suricata are available for you on the Ubuntu Server.

The DSS sensors send updates to the DSS server at `172.31.57.5`.
The DSS server replies with the same data payload back to the DSS sensor verifying receipt
The Kali and Ubuntu Server VMs are located on different subnets of the spaceship and cannot communicate with each other. The Kali and Ubuntu Server VMs are unable to sniff their subnets live. We only have these pcaps for analysis.

**System and Tool Credentials**
[REDACTED]

**Note**
Attacking or unauthorized access to `challenge.us` (`10.5.5.5`) is forbidden. You may only use the provided web page to view challenge progress and download any challenge artifacts that are provided.

==============

## Challenge Questions
1. (80) Engine Q1: How many packets are associated with Engine 1? `10100`
Filters Used: `udp.port==6186 and data[1]==31`

2. (160) Engine Q2: When four flags are set, the Status should be either Warning or Fatal. What is the packet number of the packet that failed to correctly set the Status? `23830`
Filters Used: `udp.port==6186 and data.len>=20 and data[0]<=3`

3. (240) Engine Q3: What is the lowest the burn speed can be without the Gas Flag being turned on? `25`
Filters Used: `udp.port==6186 and data[6]=="2" and data[7]=="5" and data[13]=="1"`

4. (320) Engine Q4: The Oil Flag is turned on when Burn Speed is at least ANSWER1 (or over) and Temperature reaches ANSWER2 (or below)? Submit your answer as ANSWER1:ANSWER2 (e.g., 55:1234) `75:1899`
Filters Used: `udp.port==6186 and data[6]=="7" and data[7]=="5" and data[13]=="2"  :  udp.port==6186 and data[8]<="1" and data[9]<="8" and data[10]<="9" and data[11]<="9" and data[13]=="2"`

5. (160) Engine Q5: What is the highest recorded temperature of any engine? (it may have hit this level once, or more than once; however, NEVER higher). `4000`
Filters Used: `udp.port==6186 and data[8]>="4" and data[9]>="0" and data[10]>="0" and data[11]>="0"`

6. (160) Engine Q6: The Other Flag appears to be very buggy. How many times has the Other Flag been triggered, regardless of potentially other flags being turned on/off as well. `575`
Filters Used: `udp.port==6186 and (data[13]=="5" or data[15]=="5" or data[17]=="5" or data[19]=="5" or data[21]=="5")`

![Engine 6](/engine6.png "Engine 6")

7. (80) Sensor Q1: What is the 3-digit identifier for Roger? `715`
Commands Used: `sudo tcpdump -nAAAXr dauntless-sensors.pcapng`

![Sensor 1](/sensor1.png "Sensor 1")

8. (160) Sensor Q2: A codename is being spoofed as the 24-hr key is incorrect. What was the packet number of the spoofed packet sent to the DSS Server? `271678`
Methods Used: Parsed with Python code

9. (160) Sensor Q3: What is the codename being spoofed? `james`
Methods Used: Parsed with Python code

10. (80) Sensor Q4: What was the incorrect 24-hr key being used for the spoofed codename? `A7555`
Methods Used: Parsed with Python code

==============

Below is a picture of the table I used to visualize the data:

![Data Table](/data_table.png "Data Table")
