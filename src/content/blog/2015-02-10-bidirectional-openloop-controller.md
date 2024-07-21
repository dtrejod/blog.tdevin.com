---
title: Designing A Bi-Directional Open-Loop Position Controller
slug: designing-a-bi-directional-open-loop-position-controller
featured: false
draft: false
tags:
  - hardware
  - programming-matlab
  - arduino
  - temple-university
  - ece-3412-classical-control-systems
description: ECE 3412 - Classic Control Systems
pubDatetime: 2015-02-10 00:00:00
---

![Designing A Bi-Directional Open-Loop Position Controller](@assets/images/3412_controls/bidirectional_openloop_position-controller.png)

# Problem

MatLab is a versatile toolbox that allows us to build digital control systems
quickly. In this lab we will use an open loop system for the control of a
stepper motor. We create the hypothetical situation of using a photo resistor
to sense the ambient light in a room. If the light is too low then we tell the
motor to open the blinds, and if the light is too high then we close the
blinds. The stepper motor is crucial for this operation in order to precisely
control the position of the blinds. MatLab has built in functionality to use
stepper motors via an Arduino board. The stepper block has three inputs so we
can control the speed, direction, and step count directly. Using switching,
sum, difference, memory blocks we can construct our open loop control system
that controls the inputs to our stepper motor.

[Click here for full report.](/public/assets/files/20150210_trejo_devin_lab02.pdf)
