# -*- coding: utf8 -*-

import argparse
import json

from sh import curl

from zabbix_kato.formatter import color


URL = 'https://{host}/rooms/{room_id}/simple'


parser = argparse.ArgumentParser()
parser.add_argument('room_id')
parser.add_argument('message')
parser.add_argument('--host', dest='host', default='api.kato.im')
parser.add_argument('--trigger_status', default='PROBLEM')
parser.add_argument('--trigger_severity', type=int, default=2)


def send(host, room_id, message, trigger_status, trigger_severity):

    print(curl(
        URL.format(host=host, room_id=room_id),
        d=json.dumps({
            'from': 'zabbix',
            'renderer': 'markdown',
            'text': message,
            'color': color(trigger_status, trigger_severity)
        }),
        H='Content-type: application/json'
    ))


def main():
    args = parser.parse_args()
    send(
        args.host,
        args.room_id,
        args.message,
        args.trigger_status,
        args.trigger_severity
    )


if __name__ == '__main__':
    main()
