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
import helper
import datetime

def init():
    if helper.getLogging():

        logfile = helper.getLogfile()
        file = open(logfile, 'a')
        dt = datetime.datetime.now()
        now = dt.strftime("%A, %d. %B %Y %H:%M")
        str = '======================== BEGIN LOGIN: ' + now \
+ ' ========================\n'
        file.write(str)
        file.close()


def logging(line):
    if not helper.getLogging():
        return
    logfile = helper.getLogfile()
    file = open(logfile, 'a')
    file.write(line + '\n')
    file.close

