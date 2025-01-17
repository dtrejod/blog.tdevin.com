---
title: Linear Block Code Error Correction
slug: linear-block-code-error-correction
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
pubDatetime: 2016-04-06 00:00:00
---

![Linear Block Code Error Correction](@assets/images/4532_data_comm/flow_control.png)

# Summary

We introduce the (6,3) Hamming Linear Block Coding a error detecting and
correcting algorithm. For this lab we will parse a string into 3-bit sized
messages and encoded into 6-bit codewords. We then transmit our codewords
as characters to a Windows client from a PIC32 MCU. To simulate a noisy
communication medium our client introduces random errors into our message
and returns it back to the server. We show that the Hamming LBC is capable
of correcting up to 1-bit in error for each received codeword.

[Click here for full report.](https://github.com/dtrejod/myece4532/blob/master/lab4/trejo_devin_004.pdf)
