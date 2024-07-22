---
title: DC Motor Model For Open-Loop Control In MATLAB Simulink
slug: dc-motor-model-for-open-loop-control-in-matlab-simulink
featured: false
draft: false
tags:
  - hardware
  - programming-matlab
  - arduino
  - temple-university
  - ece-3412-classical-control-systems
description: ECE 3412 - Classic Control Systems
pubDatetime: 2015-02-17 00:00:00
---

![DC Motor Model For Open-Loop Control In MATLAB Simulink](@assets/images/3412_controls/dc_motor_model_openloop_in_simulink.png)

# Problem

For the next lab we experiment working with DC motors. In the previous lab we
worked with stepper motors, which operate by supplying power to one of serval
magnets surrounding the rotor. The difference provided by the electromagnet
causes the rotor to spin in a very precise increments. The DC motor works in
similar fashion except with the magnet is permanent (armature) and while the
commutator provide a field difference. Due to the rather simple construction of
the DC motor we can construct a model for the DC motor using an equivalent
circuit consisting of a resistor, inductor, and dynamo. By the end of the lab
we will demonstrate the accuracy of our DC motor model via Simulink.

# Procedure

To begin designing a control for this system, we must determine the current, I,
and , and model `𝑑𝜃/𝑑𝑡` the integrals of the rotational acceleration and of the
rate of change of the armature current.

[Click here for full report.](/assets/files/20150217_trejo_devin_lab03.pdf)
