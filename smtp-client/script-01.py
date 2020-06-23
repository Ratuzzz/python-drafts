#!/usr/bin/python

from smtplib import SMTP

MailClient = SMTP(host='192.168.1.67', port=13130)

# Problème de connexion, voir coté firewall
