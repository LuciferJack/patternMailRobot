#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
import email
import imaplib
import logging
import sys

mail = imaplib.IMAP4_SSL('imap.gmail.com')
(retcode, capabilities) = mail.login('email','pass')
mail.list()
mail.select('inbox')

def get_unread_mail():
    """
    get unread msg from inbox
    :return:
    """
    n=0
    (retcode, messages) = mail.search(None, '(UNSEEN)')
    if retcode == 'OK':

        for num in messages[0].split() :
            print 'Processing '
            n=n+1
            typ, data = mail.fetch(num,'(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    original = email.message_from_string(response_part[1])

                    print original['From']
                    print original['Subject']
                    typ, data = mail.store(num,'+FLAGS','\\Seen')

print n

# MAIN
# ===============================================
if __name__ == '__main__':
    logging.info('main starts...')
    logging.info('main stop')
    sys.exit(0)