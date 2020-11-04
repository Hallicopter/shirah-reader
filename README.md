# Shirah
A terminal RSVP speed reader.

![Alt text](/assets/shirah.gif "Optional Title")

Caution, early stage software.

### What is an RSVP reader?
RSVP stands for [Rapid Serial Visual presentiation](https://en.wikipedia.org/wiki/Rapid_serial_visual_presentation).
Its a controversial method to enable speedreading. I have been using this on my devices, and it has given me great results. I wanted to have an option to do this in the terminal too.
Ignore the haters, and try it for yourself.
Also, I don't like that the best options on a computer are paid softwares.

### Usage
To install, use either 

```pip install shirah-reader==0.1.1```

or

```pip3 install shirah-reader==0.1.1```

To run a test, just enter `shirah`.

To read a book, and set a speed, enter

```shirah -f <path/to/book> -s <speed>```

eg: `shirah -f alice.epub -s 600`

### Goals
- [x] Read txt
- [x] Read epubs
- [x] Pause
- [ ] Save progress
- [ ] Progress bar.
- [ ] Chapter-wise Navigation
