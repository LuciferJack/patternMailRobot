#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
"""
can more mail ,more config
"""
db_config = {
    'local': {
        'smtp': "10.95.130.118", 'port': 8899,
        'user': "root", 'passwd': "***",
        'db': "marry", 'charset': "utf8",
        'pool': {
            #use = 0 no pool else use pool
            "use":1,
            # size is >=0,  0 is dynamic pool
            "size":0,
            #pool name
            "name":"local",
        }
    },
}