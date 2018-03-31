#!/usr/bin/python
import os
import socket
import threading
import random
import sys

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan

print(''+C+'')
os.system ('color D')

print '''
            Welcome To AWS
[1] - Windows Version [SubDomain Bypass/Scanner]
[2] - Linux Version   [SubDomain Bypass/Scanner]
'''

choice = raw_input('AWS:')


if choice == '1':


        os.system('cls')

        subdomains = ["dc", "test", "api", "embed", "old", "ns2", "server1", "server2", "gateway", "app", "status", "media", "ts3", "ns1", "host", "dashboard", "blog", "autodiscovery", "beta", "dev", "wiki", "autoconfig", "irc", "irix", "fileserver", "backup", "agent", "c2c", "login", "mssql", "mysql", "localhost", "nameserver", "netstats", "mobile", "mobil",  "ftp", "webadmin", "uploads", "transfer", "tmp", "support", "smtp0#", "smtp#", "smtp", "sms", "shopping", "sandbox", "proxy", "manager", "cpanel", "webmail", "forum", "driect- connect", "vb", "forums", "pop#", "pop", "home", "direct", "mail", "access", "admin", "oracle", "monitor", "administrator", "email", "downloads", "ssh", "webmin", "paralel", "parallels", "www0", "www", "www1", "www2", "www3", "www4", "www5", "autoconfig.admin", "autoconfig", "autodiscover.admin", "autodiscover", "sip", "msoid", "lyncdiscover"]
        os.system ('color D')
        url = raw_input('Enter Hostname:')
        os.system ('color C')

        for cso in subdomains:
                try:
                        host = str(cso) + "." + str(url)
                        ip = socket.gethostbyname(str(host))
                        print 'Loading: ' + host + ' | ' + ip
                except:
                        pass

if choice == '2':

        subdomains = ["dc", "test", "api", "old", "ns2", "server", "server1", "server2", "gateway", "app", "media", "help", "embed", "status", "ns1", "host", "dashboard", "blog", "autodiscovery", "beta", "dev", "wiki", "autoconfig", "secure", "irc", "irix", "fileserver", "backup", "agent", "c2c", "ts3", "login", "mssql", "mysql", "localhost", "nameserver", "netstats", "mobile", "mobil",  "ftp", "webadmin", "uploads", "transfer", "tmp", "support", "smtp0#", "smtp#", "smtp", "sms", "shopping", "sandbox", "proxy", "manager", "cpanel", "webmail", "forum", "driect- connect", "vb", "forums", "pop#", "pop", "home", "direct", "mail", "access", "admin", "oracle", "monitor", "administrator", "email", "downloads", "ssh", "webmin", "paralel", "parallels", "www0", "www", "www1", "www2", "www3", "www4", "www5", "autoconfig.admin", "autoconfig", "autodiscover.admin", "autodiscover", "sip", "msoid", "lyncdiscover"]
        url = raw_input(''+C+'Enter Hostname'+P+':')
        print(''+C+'')

        for cso in subdomains:
                try:
                        host = str(cso) + "." + str(url)
                        ip = socket.gethostbyname(str(host))
                        print 'Loading: ' + host + ' | ' + ip
                except:
                        pass


