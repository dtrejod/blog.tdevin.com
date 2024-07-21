---
title: TCP/IP Data Transmission
slug: tcp-ip-data-transmission
featured: false
draft: false
tags:
  - programming-c
  - networking
  - temple-university
  - microcontroller
  - programming
  - ece-4532-data-and-computer-Communication
description: ECE 4532 - Data Communications
pubDatetime: 2016-02-05 00:00:00
---

![TCP/IP Data Transmission](@assets/images/4532_data_comm/client_server_frame_analysis.png)

# Summary

Today we introduce the TCP/IP, a standard communication network protocol
commonly used when communicating over the internet and other computer
networks. The TCP/IP protocol guarantees the message being sent by a server
is received by a client without error. We will look at a simple application
of the protocol using a PIC32 Microcontroller Unit (MCU) as a server and
a Windows machine as a client. By analyzing the raw Ethernet frame
transmission of the TCP/IP messages we better the understanding of how
TCP/IP successfully transmits data. The analysis of the frames show how
a client first establishes a socket connection to a server, then sends a
command to the server, and finally completes the communication medium by
waiting for a response back from the server. The TCP/IP protocol has some
overhead messages on top of the messages sent by the client to ensure data
integrity on both sides.

[Click here for full report.](https://github.com/dtrejod/myece4532/blob/master/lab4/trejo_devin_004.pdf)
