Doga
====

    HTTP log monitoring console for Humans

-  watch and log all HTTP traffic of system
-  generate log in w3c log format
-  show status about total requests, maximum hits, requests in a
   timespan
-  alert when traffic is above a customizable threshold
-  can log to a custom log file also

Watch Doga in action
~~~~~~~~~~~~~~~~~~~~

.. figure:: https://raw.githubusercontent.com/pravj/Doga/master/docs/Doga.png
   :alt: Doga

How to let Doga watch for your traffic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``sudo pip install doga``

    install ``doga`` to your machine, you can also use ``easy_install``

``using Doga requires sudo privilege to run as it explicitly uses socket interface``

``sudo doga``

    start watching for your traffic

``sudo doga -f filename.txt``

    write logs to a custom log file ``filename.txt`` also
    
``sudo doga -t VALUE``

    update threshold value to ``VALUE`` on which Doga start alerting

``Jump between 'Doga Logs' and 'Alert History' sections using 'Ctrl+N'``

``Doga's GUI is not responsive yet so it will raise exceptions on smaller screen size.``

How it's made
~~~~~~~~~~~~~

-  Doga's GUI is built on top of
   `npyscreen <https://pypi.python.org/pypi/npyscreen>`__
-  Doga uses Python's `socket
   interface <https://docs.python.org/2/library/socket.html>`__ library
   to deal with all TCP/IP/Packets and *Bla Bla Bla* things

What?
~~~~~

    don't you know
    `Doga <http://en.wikipedia.org/wiki/Doga_(comics)>`__? watch out
    then, **He is after you.**

.. figure:: https://raw.githubusercontent.com/pravj/Doga/master/docs/Doga_Rules.jpg
   :alt: Doga Rules
   
   "Doga Rules" by Promotional file released by Raj Comics for promotional purposes. Licensed under Fair use of copyrighted material in the context of Doga (comics) via `Wikipedia <http://en.wikipedia.org/wiki/File:Doga_Rules.jpg#mediaviewer/File:Doga_Rules.jpg>`__

------

built with *Muzi* and *Appy* by `Pravendra Singh <https://pravj.github.io>`__
