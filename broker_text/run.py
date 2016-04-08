#!/usr/bin/env python
import textbelt
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='broker_text.log',
                    filemode='w')

text = textbelt.textbelt()

#success send

num_array = ['2123210345', '21210356']
for number in num_array:
	logging.info(number + " --- " + text.send(number,'I sent this message from python through textbelt.com'))

