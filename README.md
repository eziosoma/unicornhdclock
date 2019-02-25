# unicornhdclock
Create a scrolling calendar with date and time, italian localized.
Python program derived from text.py original Pimoroni sample for Unicorn HD Hat, for Raspberry Pi.

https://shop.pimoroni.com/producuts/unicorn-hat-hd

The program solved the pretty printing of week days:
lunedì
martedì
mercoledì
giovedì
venerdì

that have "i" plus accent at the end

For having the program starting at the boot, for a Raspberry "headless", use crontab as described at this URL:

https://www.dexterindustries.com/howto/auto-run-python-programs-on-the-raspberry-pi/

With few row of code the clock now shows short Italian 'fortune' quotes.
You have to install the fortune program
        sudo apt-get install fortune 
take from here the sentences in Italian (debian packaging):
        https://packages.qa.debian.org/f/fortunes-it.html


