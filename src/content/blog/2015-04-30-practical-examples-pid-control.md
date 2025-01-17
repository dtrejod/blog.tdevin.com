---
title: Practical Examples of PID Control
slug: practical-examples-of-pid-control
featured: false
draft: false
tags:
  - hardware
  - programming-matlab
  - arduino
  - temple-university
  - ece-3412-classical-control-systems
description: ECE 3412 - Classic Control Systems
pubDatetime: 2015-04-30 00:00:00
---

![Practical Examples of PID Control](@assets/images/3412_controls/practical_examples_pid_control.png)

# Problem

In this lab we will be experimenting with practical PID control applications.
In particular, we will concern ourselves with controlling the speed of a DC
motor using both the output of the encoder, and an accelerometer.

# Procedure

For this lab we will reference our PID control to the throttle vale position.
The throttle control is what determines a car’s acceleration and is tied to the
angle in which the gas pedal is situated. To begin we will showcase different
scenarios with varying PID control. We will discuss which levels of PID control
correspond to the most desired response. Next we will introduce an
accelerometer to our system.

The accelerometer feeds into a MatLab function that also takes into account the
current speed of our motor. The two in combination we be feed back into our DC
motor controller. Our accelerometer will be able to determine if our motor is
accelerating uncontrollably.

[Click here for full report.](/assets/files/20150430_trejo_devin_lab10.pdf)
