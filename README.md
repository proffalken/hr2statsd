# Heartrate to Statsd

## What does it do?

It connects to a Bluetooth LE heart-rate monitor and publishes the data to a
statsd server of your choosing.

## What doesn't it do?

   * Anything that could be considered "dynamic configuration".  Statsd is
     hard-coded into the script and must be changed there.
   * Reconnect gracefully. At the moment, if you walk out of range, you need to
     restart the program when you get back to the device running it

## Why does it even exist?!

Because I wanted a way to play around with https://github.com/markrages/ble, my
Arendo HRM
(https://www.amazon.co.uk/Arendo-transmitter-low-energy-technology-water-proof/dp/B00R7EVJ2A)
and statsd.

It's not meant for anything other than fun!
