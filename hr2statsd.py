#!/usr/bin/python2

import csv
import datetime
import time

import statsd
import ble


statsd_server = '<YOUR STATSD SERVER HERE>'
statsclient = statsd.StatsClient(statsd_server, 8125)

dev = ble.discover_device(lambda d: ble.uuids.heart_rate in d.uuids)
try:
    dev.connect()
    dev.heart_rate_service.heart_rate_measurement.notifying=True

    max_hr = 0
    min_hr = 90
    timer = 0
    while True:
        curr_hr = dev.heart_rate_service.heart_rate_measurement.value[1]

        if max_hr <= curr_hr:
            max_hr = curr_hr

        if min_hr >= curr_hr:
            min_hr = curr_hr

        statsclient.gauge('hr2statsd.current_hr', curr_hr)
        statsclient.gauge('hr2statsd.max_hr', max_hr)
        statsclient.gauge('hr2statsd.min_hr', min_hr)

        if timer < 60:
            timer = timer + 1
        else:
            timer = 0
except:
    pass
