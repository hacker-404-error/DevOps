# Command Line

### The Shell

- A shell is a type of computer program called a command-line interpreter that lets Linux and Unix users control their operating systems with command-line interfaces
- `Why the name "Shell"`:The Linux command line interface is called a shell because it is an outer layer (like a walnut’s shell) around the operating system’s core functions. Users communicate with the system’s core by typing commands into this outer layer.
- `Importance of Linux Shell`: While modern graphical user interfaces (GUIs) provide a user-friendly way to interact with computers, sysadmins and seasoned users still prefer a shell for several reasons
  - Efficiency
  - Scripting And Automation
  - Remote Access
  - Economic Resource Consumption

### Types of Linux Shell

- `Bourne Shell (sh)`

  - It is typically referred to as sh.
  - Full Path to Command: /bin/sh or /sbin/sh
  - Default Prompt for Non-Root User: $.
  - Default Prompt for Root User: #.

- `C Shell (csh)`

  - Shell Name: It is referred to as csh in scripts.
  - Full Path to Command: /bin/csh.
  - Default Prompt for Non-Root User: hostname %.
  - Default Prompt for Root User: hostname #.

- `TENEX C Shell (tcsh)`

  - Shell Name: It is referred to as tcsh.
  - Full Path to Command: /bin/tcsh.
  - Default Prompt for Non-Root User: hostname:directory>.
  - Default Prompt for Root User: hostname:directory#.

- `KornShell (ksh)`

  - Shell Name: It is referred to as ksh.
  - Full Path to Command: /bin/ksh or /bin/ksh93.
  - Default Prompt for Non-Root User: $.
  - Default Prompt for Root User: #.

- `Debian Almquist Shell (dash)`

  - Shell Name: It is referred to as dash.
  - Full Path to Command: /bin/dash.
  - Default Prompt for Non-Root User: $.
  - Default Prompt for Root User: #.

- `Bourne Again Shell (Bash)`

  - Shell Name: It is referred to as bash.
  - Full Path to Command: /bin/bash.
  - Default Prompt for Non-Root User: $.
  - Default Prompt for Root User: #.

- `Z Shell (zsh)`

  - Shell Name: It is referred to as zsh.
  - Full Path to Command: /bin/zsh.
  - Default Prompt for Non-Root User: user@hostname location %.
  - Default Prompt for Root User: hostname (user):~#.

- `Friendly Interactive Shell (fish)`
  - Shell Name: It is referred to as fish.
  - Full Path to Command: /usr/bin/fish.
  - Default Prompt for Non-Root User: user@hostname location>.
  - Default Prompt for Root User: root@hostname location#.

### Basic Commands

- `echo`: prints out the text arguments to the display.

```
localhost:~# echo hey this is pritam Das
hey this is pritam Das
localhost:~#
```

- `pwd`: “print working directory” and it just shows you which directory you are in, note the path stems from the root directory.

```
localhost:~/pritam/das# pwd
/root/pritam/das
localhost:~/pritam/das#
```

- `cd`: Change directory
  - . (current directory). This is the directory you are currently in.
  - .. (parent directory). Takes you to the directory above your current.
  - ~ (home directory). This directory defaults to your “home directory”. Such as /home/pete.
  - - (previous directory). This will take you to the previous directory you were just at.

```
localhost:~/pritam/das# cd linux
localhost:~/pritam/das/linux#
```

```
localhost:~/pritam/das/linux# cd .
localhost:~/pritam/das/linux#
```

```
localhost:~/pritam/das/linux# cd ..
localhost:~/pritam/das#
```

```
localhost:~/jyotsna/bharti# cd ~
localhost:~#
```

```
localhost:~/jyotsna/bharti# cd ~
localhost:~# cd -
/root/jyotsna/bharti
localhost:~/jyotsna/bharti#
```

- `ls`: List Directories
  - ls : The "ls" command will list directories and files in the current directory by default.
  - ls /home/pete : With this we can specify which path you want to list the directories of.
  - ls -l : This shows a detailed list of files in a long format. This will show you detailed information,
           Starting from the left: file permissions, number of links, owner name, owner group, file size, timestamp of last
           modification, and file/directory name.
  - ls -a : Filenames that start with . are hidden, you can view them however with the ls command and pass the -a flag to
            it (a for all).
  - ls -la : As we added -a and -l, well you can add them both together with -la. The order of the flags determines which 
             order it goes in, most of the time this doesn’t really matter so you can also do ls -al and it would still 
             work.

```
localhost:~# ls
bench.py    hello.c     jp          readme.txt
bharti      hello.js    jyotsna
localhost:~#
```

```
localhost:~#
localhost:~# cd /root/jyotsna/pritam/das
localhost:~/jyotsna/pritam/das# cd ~
localhost:~# ls /root/jyotsna
pritam
localhost:~# ls /root/jyotsna/pritam
das
localhost:~#
```

```
localhost:~# ls -l
total 28
-rw-r--r--    1 root     root           114 Jul  5  2020 bench.py
drwxr-xr-x    2 root     root            37 May 17 13:42 bharti
-rw-r--r--    1 root     root            76 Jul  3  2020 hello.c
-rw-r--r--    1 root     root            22 Jun 26  2020 hello.js
drwxr-xr-x    2 root     root            37 May 17 13:42 jp
drwxr-xr-x    3 root     root            60 May 17 13:39 jyotsna
-rw-r--r--    1 root     root           151 Jul  5  2020 readme.txt
localhost:~#
```

```
localhost:~# ls -a
.             .cache        bench.py      hello.js      readme.txt
..            .mozilla      bharti        jp
.ash_history  .wine         hello.c       jyotsna
localhost:~#
```

```
localhost:~# ls -la
total 52
drwxr-xr-x    8 root     root           303 Jan  9  2021 .
drwxrwxrwx   21 root     root           461 May 17 14:16 ..
-rw-------    1 root     root           303 May 17 14:16 .ash_history
drwx------    3 root     root            61 Jul  6  2020 .cache
drwx------    5 root     root           124 Jul  6  2020 .mozilla
drwxr-xr-x    4 root     root           202 Jul  6  2020 .wine
-rw-r--r--    1 root     root           114 Jul  5  2020 bench.py
drwxr-xr-x    2 root     root            37 May 17 13:42 bharti
-rw-r--r--    1 root     root            76 Jul  3  2020 hello.c
-rw-r--r--    1 root     root            22 Jun 26  2020 hello.js
drwxr-xr-x    2 root     root            37 May 17 13:42 jp
drwxr-xr-x    3 root     root            60 May 17 13:39 jyotsna
-rw-r--r--    1 root     root           151 Jul  5  2020 readme.txt
localhost:~#
```

- `Touch`: Creates a new empty file.
  - Also used to change timestamps on existing files and directories.

```
localhost:~/jyotsna# touch Myfile
localhost:~/jyotsna# ls -l
total 4
-rw-r--r--    1 root     root             0 May 17 14:21 Myfile
drwxr-xr-x    3 root     root            57 May 17 13:39 pritam
```

```
localhost:~/jyotsna# touch Myfile
localhost:~/jyotsna# ls -l
total 4
-rw-r--r--    1 root     root             0 May 17 14:22 Myfile
drwxr-xr-x    3 root     root            57 May 17 13:39 pritam
```

- `file`: Show's description of the file’s contents.
  - In Linux, filenames aren’t required to represent the contents of the file. You can create a file called funny.gif that isn’t actually a GIF.

```
localhost:~/jyotsna# file linux.txt
linux.txt: empty
localhost:~/jyotsna#

`After file Updation`

localhost:~/jyotsna# file linux.txt
linux.txt: ASCII text
localhost:~/jyotsna#

```

- `cat`: To read a file.
  - It not only displays file contents but it can combine multiple files and show you the output of them.

```
localhost:~/jyotsna# cat linux.txt python.txt
this is a linux file
this is a python file

localhost:~/jyotsna#
```

- `less`: 

```
localhost:~/pritam/das# less html.txt

`file opened`

this is a html file
~
~
~
~
~
~
~
html.txt
```

- `history`

```
localhost:~/pritam/das# history
   0 pwd
   1 ls -l
   2 ls -a
   3 mkdir pritam
   4 cd pritam
   5 cd das
   6 mmkdir das
   7 cd das
   8 mkdir das
   9 cd das
  10 pwd
  11 cd~
  12 cd ~
  13 echo hey this is pritam Das
  14 cd das
  15 cd pritam
  16 cd das
  17 mkdir linux
  18 cd linux
  19 cd .
  20 cd ..
  21 cd ~
localhost:~/pritam/das#
```

- `cp`:

```

```

- 'mv`:

```
localhost:~# mv readme.txt readhim.txt
localhost:~# ls -a
.             .cache        bench.py      jyotsna
..            .mozilla      hello.c       pritam
.ash_history  .wine         hello.js      readhim.txt
localhost:~#
```

- `mkdir`:

```
localhost:~# mkdir folder1
localhost:~# ls -l
total 28
-rw-r--r--    1 root     root           114 Jul  5  2020 bench.py
-rw-r--r--    1 root     root            76 Jul  3  2020 bye.c
drwxr-xr-x    2 root     root            37 May 14 21:19 folder1
-rw-r--r--    1 root     root            22 Jun 26  2020 hello.js
drwxr-xr-x    3 root     root           113 May 14 20:44 jyotsna
drwxr-xr-x    3 root     root            57 May 14 20:40 pritam
-rw-r--r--    1 root     root           151 Jul  5  2020 readhim.txt
```

```
localhost:~# mkdir -p folder1/bharti/das
localhost:~# cd folder1
localhost:~/folder1# cd bharti
localhost:~/folder1/bharti# cd das
localhost:~/folder1/bharti/das# pwd
/root/folder1/bharti/das
localhost:~/folder1/bharti/das#
```
- `rm`:
```
localhost:~# ls -a
.             .cache        bench.py      hello.js      readhim.txt
..            .mozilla      bye.c         jyotsna
.ash_history  .wine         folder1       pritam
localhost:~# rm bye.c
localhost:~# ls -a
.             .cache        bench.py      jyotsna
..            .mozilla      folder1       pritam
.ash_history  .wine         hello.js      readhim.txt
localhost:~#
```
```
localhost:~# rm -i hello.js
rm: remove 'hello.js'? y
localhost:~# ls -a
.             .cache        bench.py      pritam
..            .mozilla      folder1       readhim.txt
.ash_history  .wine         jyotsna
localhost:~#
```
```
localhost:~# rm folder1
rm: 'folder1' is a directory
localhost:~# rm -r folder1
localhost:~#
```
