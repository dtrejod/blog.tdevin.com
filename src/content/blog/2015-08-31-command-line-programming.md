---
title: Command Line Programming
slug: command-line-programming
featured: false
draft: false
tags:
  - programming-bash
  - linux
  - temple-university
  - ece-3822-software-tools
description: ECE 3822 - Software Tools for Engineers
pubDatetime: 2015-08-31 00:00:00
---

![Command Line Programming](@assets/images/3822_software_tools/simple-bash-scripting.png)

# Problem

In this first assignment of the semester we simply want to familiarize
ourselves with command line tools. We start by learning how to personalize
our Linux configuration by editing the `.bash_profile` and `.bashrc` files in
`~/`. Aliases and manipulating the environment path allow us to run
commands from any directory on our machines.

1. Edit the environment path so a `hello world` command can be ran from
   any directory. Then create an alias by modifying the `.bash_profile`.
   We then switch gears and learn some commonly used commands. Commands like
   `grep`, `find`, `wc`, `echo`, etc. are powerful commands that we should
   know. Specifically we will work with a large data set of clinical EEGs and
   query for three cases:

2. Patient Names whose first names start with R and last names start with
   S who had an EEG in the date range 2010-13

3. EEG reports that contain the word _‘spike’_. EEG reports that contain the
   word ‘seizure’. We then produce a histogram of the words in these reports.

4. For EEG reports that contain the word _‘spike’_ produce a histogram of
   bi-grams.

[Click here for full report.](/assets/files/20150831_trejo_devin_hw1.pdf)
