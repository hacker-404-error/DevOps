## What is Linux

- Linux is often referred to as an operating system, but in reality, it is more accurately described as a kernel
- `Definition`: It is an open-source operating system which is freely available to everyone.
- `Development`: As it is open source, it is developed by sharing and collaboration of codes by world-wide developers.
- `Manufacturer`: Linux kernel is developed by the community of developers from different parts of the world. Although the father of Linux, Linus Torvalds oversees things.
- `GUI`: Linux is command based but some distros provide GUI based Linux. Gnome and KDE are mostly used GUI. It has different distros like Ubuntu, Redhat, Fedora, etc.
- `Interface`: The default interface is BASH (Bourne Again Shell). But some distros have developed their own interfaces.
- `Coding`: Linux is a Unix clone, behaves like Unix but doesn't contain its code.
- `Security`: It provides higher security. Linux has about 60-100 viruses listed till date.
- `Error detection and solution`: As Linux is open-source, whenever a user posts any kind of threat, developers from all over the world start working on it. And hence, it provides faster solution.

## Introduction To Linux

- Linux is an open-source Unix-like operating system-based family on the Linux kernel, and the OS kernel was first published on 17 September 1991 by Linus Torvalds.
- Typically, Linux is packaged as the Linux distribution, which contains the supporting libraries and system software and kernel, several of which are offered by the GNU Project.
- Several Linux distributions use the term "Linux" in the title, but the Free Software Foundation uses the "GNU/Linux" title to focus on the necessity of GNU software, causing a few controversies.]

## Design of Linux OS

Image from https://static.javatpoint.com/linux/images/what-is-linux2.png

- `BootLoader`: It is a program that can load the Linux kernel into the main memory of the computer by being run by the computer after when it’s turned on
- `init program`: It is the first process announced by the Linux kernel and the process tree root. In other words, every process is opened from init. It initiates processes like login prompts and system services (whether in terminal or graphical mode).
- `Software libraries`: which include code that can be applied by running processes. the most widely used software library is the GNU C Library (glibc) on Linux systems. There are several other liabilities like Mesa and SDL.
- `User interface`: the user interface is called a shell. It is either a GUI (graphical user interface), a CLI (command-line interface), Command-line interface shells are text-based UIs, which utilize text for both output and input. The dominant shell is the bash (Bourne-Again Shell) used in Linux, originally designed for the GNU project. GUI shells are the most famous user interfaces on desktop systems, packaged with broad desktop environments like Xfce, Pantheon, LXDE, Cinnamon, MATE, GNOME, and KDE Plasma, though a range of several user interfaces is available.
- `Video input infrastructure`: Currently, Linux has two kernel-userspace APIs to handle video input devices: DVB API for TV reception and V4L2 API for radio and video streams.

## Linux Distributions:

- A Linux distribution, commonly known as a Linux distro, refers to a complete operating system that is based on the Linux kernel and bundled with various software packages.
- A Linux distribution is a complete operating system that includes the
  - Linux kernel,
  - system libraries,
  - utilities,
  - application software, and
  - a package management system.
- It is created by assembling various software components from different sources and packaging them together to provide a cohesive and user-friendly computing environment.

### Main Characteristics and Components of a Linux Distribution

- `Linux Kernel`: The Linux kernel serves as the core component of the operating system, providing low-level functionality, hardware abstraction, and device drivers.
- `System Libraries`: Linux distributions include a set of system libraries, such as the GNU C Library (glibc), which provide essential functions and interfaces for applications to interact with the underlying operating system.
- `User Interface`: Linux distributions offer different user interfaces, including graphical user interfaces (GUIs) like GNOME, KDE, or Xfce, as well as command-line interfaces (CLIs). These interfaces allow users to interact with the system and run applications.
- `Software Packages`: Linux distributions come with a collection of software packages, including productivity tools, web browsers, email clients, media players, development tools, and more. These packages are typically managed and installed through a package management system.
- `Package Management System`: Linux distributions utilize a package management system to install, update, and remove software packages. Examples of popular package management systems include Advanced Packaging Tool (APT) used in Debian-based distributions, Yellowdog Updater, Modified (YUM) used in Fedora and Red Hat-based distributions, and Pacman used in Arch Linux.
- `Configuration and Customization`: Linux distributions provide tools and utilities for configuring various aspects of the system, such as network settings, display preferences, user accounts, and security options. Users can customize the operating system to suit their specific needs and preferences.
- `Support and Community`: Linux distributions are often backed by vibrant communities and support forums where users can seek assistance, share knowledge, and contribute to the development and improvement of the distribution.

### Trends and types

- Linux distributions might be:

  - Non-commercial or commercial
  - Developed for home users, power users, or enterprise users
  - Supported on two or more types of platform or hardware-specific, even to the certification extension via platform vendor
  - Developed for embedded, desktop, or server devices
  - Highly specialized or general purpose toward particular machine functionalities (e.g., computer clusters, network routers, and firewalls)
  - Targeted at particular user groups, e.g., by language internationalization and localization or by including several scientific computing and music production packages
  - Primarily, built for comprehensiveness, portability, usability, or security
  - Rolling release or standard release

| Distribution | Why To Use                                                                         |
| ------------ | ---------------------------------------------------------------------------------- |
| UBuntu       | It works like Mac OS and easy to use.                                              |
| Linux mint   | It works like windows and should be use by new comers.                             |
| Debian       | It provides stability but not recommended to a new user.                           |
| Fedora       | If you want to use red hat and latest software.                                    |
| Red hat      | enterprise To be used commercially.                                                |
| CentOS       | If you want to use red hat but without its trademark.                              |
| OpenSUSE     | It works same as Fedora but slightly older and more stable.                        |
| Arch Linux   | It is not for the beginners because every package has to be installed by yourself. |

# History

- In 1969, **Ken Thompson** and **Dennis Ritchie** of Bell Laboratories developed the UNIX operating system.
- It was later rewritten in C to make it more portable and eventually became a widely used operating system.
- A decade or so later, Richard Stallman started working on the GNU[^1] (GNU is Not UNIX) project, the GNU kernel called Hurd, which unfortunately never came to completion
- The kernel is the most important piece in the operating system. It allows the hardware to talk to the software.
- During this time other efforts such as BSD, MINIX, etc were developed to be UNIX like-systems. However, one thing that all these UNIX like-systems had in common was the lack of a unified kernel.
- Then in 1991, a young fellow named **Linus Torvalds** started developing what we now know today as the Linux kernel.

```
- The term Linux is actually quite a misnomer,
- Since it actually refers to the Linux kernel.
- Many distributions use the Linux kernel so therefore are commonly known as Linux operating systems.

```

- A linux system is divided into 3 parts:
  - `Hardware`: Includes all the H/Ws like Memory CPU, Disks
  - `Linux Kernel`: Core of the operating System
  - `User Space`: Beautiful View of the operating system, THE GUI

[^1]: GNU Operating System.
