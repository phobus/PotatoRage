#! /bin/sh

# dirty scrip for ubuntu

NAME=potatorage
DESC=PotatoRage

#PROG_DIR="${PWD}"
PROG_DIR=/home/neganix/git/PotatoRage
DATA_DIR=$PROG_DIR/data

CONF_DIR=$DATA_DIR
PID_DIR=$DATA_DIR

CONFF=$CONF_DIR/potatorage.conf
PROG=$PROG_DIR/PotatoRage.py
RC_PIDFILE=$PID_DIR/potatorage.pid

# path to python bin
DAEMON=${PYTHON_BIN-/usr/bin/python}

OPTS="--daemon --pidfile=$RC_PIDFILE --config=$CONFF --datadir=$DATA_DIR"

start_potatorage() {
    echo "Starting $DESC"
    start-stop-daemon -d $PROG_DIR --start --pidfile $RC_PIDFILE --exec $DAEMON -- $PROG $OPTS
}

stop_potatorage() {
    echo "Stopping $DESC"
    start-stop-daemon --stop --pidfile $RC_PIDFILE --retry 15
}

case "$1" in
    start)
        start_potatorage
        ;;
    stop)
        stop_potatorage
        ;;

    restart|force-reload)
        stop_potatorage
        sleep 2
        start_potatorage
        ;;
    status)
        status_of_proc -p "$RC_PIDFILE" "$DAEMON" "$DESC"
        ;;
    *)
        N=/etc/init.d/$NAME
        echo "Usage: $N {start|stop|restart|force-reload}" >&2
        exit 1
        ;;
esac

exit 0
