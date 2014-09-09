Doga
====

> HTTP log monitoring console for Humans

* watch and log all HTTP traffic of system
* generate log in w3c log format
* show status about total requests, maximum hits, requests in a timespan
* alert when traffic is above a customizable threshold
* can log in a custom log file also


###Watch Doga in action

![Doga](https://raw.githubusercontent.com/pravj/Doga/master/docs/Doga.png)

###How to let Doga watch for your traffic

> wait is over and Doga is on pypi now : [Doga-0.0.7](https://pypi.python.org/pypi/Doga)

* use either `pip` or `easy_install` to install `Doga`
  * for `pip` : `sudo pip install doga`
* run it with `sudo doga` (as it require higher privilege than a regular user have)
* change between logs and history section in application using `Ctrl+N`
* exit of application by selecting `cancel`
* write logs to a custom log file using `sudo doga -f filename.txt`

###How it's made

* Doga's GUI is built on top of [npyscreen](https://pypi.python.org/pypi/npyscreen)
* Doga uses Python's [socket interface](https://docs.python.org/2/library/socket.html) library to deal with all TCP/IP/Packets and *Bla Bla Bla* things

---

###What?

> don't you know [Doga](http://en.wikipedia.org/wiki/Doga_(comics))? watch out then, **He is after you.**

![Doga_Rules](https://raw.githubusercontent.com/pravj/Doga/master/docs/Doga_Rules.jpg)

> *Doga Rules* by Promotional file released by Raj Comics for promotional purposes.
> Licensed under Fair use of copyrighted material in the context of Doga (comics) via [Wikipedia](http://en.wikipedia.org/wiki/File:Doga_Rules.jpg#mediaviewer/File:Doga_Rules.jpg)

---
> made with *Muzi* and *Appy* by [Pravendra Singh](https://pravj.github.io) at [29.865162, 77.892397](https://www.google.co.in/maps/place/29°51'54.6"N+77°53'32.6"E/@29.8651615,77.892397,2727)
