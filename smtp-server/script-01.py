#!/usr/bin/python

from smtpd import SMTPServer
import time

print('Starting the script...');

class MailServer(SMTPServer):
    def __init__(self, localAddr, remoteAddr):
        super(MailServer, self).__init__(localAddr, remoteAddr)
        print('Creation of a new mail server !')

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        """
        peer :  remote address
        mailfrom : envelope originator
        rcpttos : envelope recipients
        data : content of the e-mail
        **kwargs : dictionnaire conteant des informations supplémentaires
        """
        print('A new mail has been received from ' + peer);
        pass

server = MailServer(('localhost', 13130), ('192.168.1.67', 13130))

while True:
    time.sleep(2)


