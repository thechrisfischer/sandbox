#!/usr/bin/env python
import textbelt
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='broker_text.log',
                    filemode='w')

text = textbelt.textbelt()

#success send

num_array = ['2123210345', '21210356', '2032148848', '4803294635']
for number in num_array:
    status = text.send(number,'Brokers, reconnect with clients use our app - http://goo.gl/uyp2tI')
    logging.info(number + " --- " + status)

