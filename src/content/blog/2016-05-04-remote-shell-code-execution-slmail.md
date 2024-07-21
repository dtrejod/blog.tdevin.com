---
title: Remote Shell-Code Execution using the SLMail-5.5.0 Service
slug: remote-shell-code-execution-using-the-slmail-5-5-0-service
featured: false
draft: false
tags:
  - security
  - networking
  - temple-university
  - programming-python
  - programming-bash
  - programming
  - linux
  - ece-5526-computer-intrusion
description: ECE 5526 - Engineering Principles of Computer Intrusion and Detection
pubDatetime: 2016-05-04 00:00:00
---

![Remote Shell-Code Execution](@assets/images/5526_engineering_principles_computer_intrusion/nmap-scan-windows2k.png)

# Summary

Today we extend the previous experiment with probing a buffer exploit
vulnerability inside SLMail and getting the program to execute the remotely
placed shell-code. We successfully get SLMail to open a TCP socket
listening socket on port 4444 leading to a Administrative privileged command
prompt. The shell-code is loading remotely using a Python script that
creates the specially crafted payload that contains the shell-code inside.

[Click here for full report.](https://github.com/dtrejod/myece5526/blob/master/projects/20160501_slmailremoteshell/20160504_trejo_devin_slmail_exploit.pdf)
