# Shirah
A curses based terminal RSVP speed reader.

![Alt text](/assets/shirah.gif "Optional Title")

Caution, early stage software.

### What is an RSVP reader?
RSVP stands for [Rapid Serial Visual presentiation](https://en.wikipedia.org/wiki/Rapid_serial_visual_presentation).
Its a controversial method to enable speedreading. I have been using this on my devices, and it has given me great results. I wanted to have an option to do this in the terminal too.
![Alt text](/assets/speedread.gif "Optional Title")

Ignore the haters, and try it for yourself.
Also, I don't like that the best options on a computer are paid softwares.

### Usage
To install, use either 

```pip install shirah-reader```

or

```pip3 install shirah-reader```


To read a book, and set a speed, enter

```shirah /path/to/book```

Here are the shortcuts:
```
Usage:
    shirah             read last epub
    shirah EPUBFILE    read EPUBFILE
    shirah STRINGS     read matched STRINGS from history
    shirah NUMBER      read file from history
                       with associated NUMBER
                       
Options:
    -r              print reading history
    -d              dump epub
    -h, --help      print short, long help
```

### How to speed read
Once in a chapter, press `r` to get into the rsvp mode. Press ^C to change the speed. Press ^C and then enter q to get out of the rsvp mode.

### Navigation
Press `tab` to see table of contents, and navigate.


### Keybindings
```
Key Binding:
    Help            : ?
    Quit            : q
    Scroll down     : DOWN      j
    Scroll up       : UP        k
    Half screen up  : C-u
    Half screen dn  " C-d
    Page down       : PGDN      RIGHT   SPC
    Page up         : PGUP      LEFT
    Next chapter    : n
    Prev chapter    : p
    Beginning of ch : HOME      g
    End of ch       : END       G
    Open image      : o
    Search          : /
    Next Occurence  : n
    Prev Occurence  : N
    Toggle width    : =
    Set width       : [count]=
    Shrink          : -
    Enlarge         : +
    ToC             : TAB       t
    Metadata        : m
    Mark pos to n   : b[n]
    Jump to pos n   : `[n]
    Switch colorsch : [default=0, dark=1, light=2]c
```

### Main Goals
- [x] Read txt
- [x] Read epubs
- [x] Pause
- [x] Save progress
- [x] Progress bar.
- [x] Chapter-wise Navigation

## Credits
- ebooklib by Aleksandar Erkalović (https://github.com/aerkalov/ebooklib)
- epy by Benawi Adha (https://github.com/wustho/epy)

### License
```
 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
 ```
