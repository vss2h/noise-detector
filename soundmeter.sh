#! /bin/sh
# /etc/init.d/soundmeter

case "$1" in
  start)
    echo "Starting Sound Meter"
    /home/pi/soundmeter.py 2>&1 &
    ;;
  stop)
    echo "Stopping Sound Meter"
    # kill application you want to stop
    LP_PID=`ps auxwww|grep soundmeter.py|head -1|awk '{print $2}'`
    kill -9 $LP_PID
    ;;
  *)
    echo "Usage: /etc/init.d/soundmeter {start|stop}"
    exit 1
    ;;
esac


exit 0
