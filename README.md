IRC Bot
=======

From scratch written IRC bot in python.

Dependencies
------------

* twitter

Features
--------

* Multilanguage - de_DE/en_EN
* Database Backend (sqlite3)
* Configuration File
* UTF-8 encoding
* CTCP support for the following commands: VERSION, USERINFO, TIME
* Greeting (PRIVMSG) if new user joins channel. (DISABLED: distempering)
* Last twitter post of an user (if not protected)
* Quotes (Can be easily modified)
* Logging.
* Search on ssl.scroogle.org
* Returns the header of a given website
* Messaging system
* Feed Reader

How-To
-------

There are two possibilities to communicate with the Master Yoda. One is in the channel and the other is in a private conversation (QUERY). A command to the bot begins always with an "!" and the answer is only visible for you (NOTICE).

Channel/Query commands
----------------------

* !version
* !uptime
* !quote
* !tweet username
* !header url
* !search searchterm
* !msg user message

> user ... The user which should receive the message.<br/>
> message ... The message you want send.<br/>
> The user receives the message when he/she joins the channel where the bot is. After the message is send the message will be deleted from the server.

* !feed -- Show which feeds are available.

> -= Projects : moksec<br/>
> -= Security : milw0rm, heisesec, sectube, debsec<br/>
> -= News     : ntv, n24, spiegel, cnn, bbc, prolinux, slashdot<br/>
> -= Science  : sciencedaily, theregister<br/>
> -= Torrent  : isohunt, torrent<br/>

* !feed name -- Prints the last entries of the feed (at most 10)
* !feed name n -- Prints the nth article of the feed with the name name

CTCP Commands
-------------

* /CTCP botname VERSION
* /CTCP botname USERINFO
* /CTCP botname TIME

