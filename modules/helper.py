# -*- coding: UTF-8 -*-
# ircbot.py - A simple IRC bot
#
# (C) 2009 by MokSec Project
# Written by Alex Oberhauser <oberhauseralex@networld.to>
# All Rights Reserved
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>
import socket
import datetime
import ConfigParser
import time
import string
import sys

def readConfig():
    config = ConfigParser.SafeConfigParser()
    config.read('conf/ircbot.cfg')
    readConfig.HOST = config.get('server', 'host')
    readConfig.PORT = config.getint('server', 'port')
    readConfig.PASS = config.get('server', 'password')
    readConfig.SSL = config.get('server', 'ssl')
    readConfig.NICKNAME = config.get('bot', 'nickname')
    readConfig.FULLNAME = config.get('bot', 'fullname')
    readConfig.IDENT = config.get('bot', 'ident')
    readConfig.CHANNEL = config.get('channel', 'mainchannel')
    readConfig.DBFILE = config.get('quotes', 'dbfile')
    readConfig.DBNAME = config.get('quotes', 'dbname')
    readConfig.LOGGING = config.getboolean('server', 'logging')
    if readConfig.LOGGING:
        readConfig.LOGFILE = config.get('server', 'logfile')

def connect():
    readConfig()
    if readConfig.SSL == "false":
        connect.soc = socket.socket()
        connect.soc.connect( (readConfig.HOST, readConfig.PORT) )
        connect.soc.send('PASS ' + readConfig.PASS + '\r\n')
        checkForPing(connect.soc)
        connect.soc.send('NICK ' + readConfig.NICKNAME + '\r\n')
        checkForPing(connect.soc)
        connect.soc.send('USER ' + readConfig.IDENT + ' 8 * :' + readConfig.FULLNAME + '\r\n')
        checkForPing(connect.soc)
        connect.starttime = datetime.datetime.now()
        joinMainchannel()
    else:
        #from M2Crypto import SSL, httpslib
        #context = SSL.Context("sslv3")
        ## ATTENTION: The server certificate is not checked!!!
        #context.set_verify(0, depth = 0)
        #connect.soc = httpslib.HTTPSConnection(readConfig.HOST, readConfig.PORT, ssl_context=context)
        #SSL.Connection.postConnectionCheck = None
        #connect.soc.connect()
        sys.exit("SSL support currently broken... Sorry for the inconvenience!")

def checkForPing(soc):
    readbuffer = soc.recv(1024)
    tmp = string.split(readbuffer, '\n')
    readbuffer = tmp.pop()
    for line in tmp:
        line = string.rstrip(line)
        line = string.split(line)
        if ( line[0] == 'PING' ):
            soc.send('PONG ' + line[1] + '\r\n')

def joinMainchannel():
    time.sleep(2)
    connect.soc.send('JOIN ' + readConfig.CHANNEL + '\r\n')

def getSocket():
    return connect.soc

def getSSL():
    return readConfig.SSL

def getNickname():
    return readConfig.NICKNAME

def getChannel():
    return readConfig.CHANNEL

def getDbfile():
    return readConfig.DBFILE

def getDbname():
    return readConfig.DBNAME

def getLogging():
    return readConfig.LOGGING

def getLogfile():
    assert readConfig.LOGGING
    return readConfig.LOGFILE

def getStarttime():
    return connect.starttime

def getTime():
    dt = datetime.datetime.now()
    return dt.strftime("%A, %d. %B %Y %H:%M")

def getUser(line):
    user = line.strip(':')
    user = user.split('!')
    return user[0]

def getVersion():
    msg = []
    msg.append("Master Yoda (IRC Bot)")
    msg.append("          .--.")
    msg.append("::\`--._,'.::.`._.--'/::::")
    msg.append("::::.  ` __::__ '  .::::::")
    msg.append("::::::-:.`'..`'.:-::::::::")
    msg.append("::::::::\ `--' /::::::::::")
    msg.append("          `--'")
    msg.append("by Alex Oberhauser")
    msg.append("http://irc.networld.to")

    return msg

def getHelp():
    msg = []
    msg.append('-= Channel/Query commands')
    msg.append('   * !version')
    msg.append('   * !uptime')
    msg.append('   * !quote')
    msg.append('   * !tweet username')
    msg.append('   * !header website')
    msg.append('   * !search searchterm')
    msg.append('   * !msg user msg')
    msg.append('   * !feed, !feed name, !feed name x')
    msg.append('-= CTCP commands')
    msg.append('   * /CTCP ' + readConfig.NICKNAME + ' VERSION')
    msg.append('   * /CTCP ' + readConfig.NICKNAME + ' USERINFO')
    msg.append('   * /CTCP ' + readConfig.NICKNAME + ' TIME')

    return msg

