#! /bin/sh

PROG_DIR="${PWD}"
DATA_DIR=$PROG_DIR/data

PROG=$PROG_DIR/PotatoRage.py
RC_PIDFILE=$DATA_DIR/potatorage.pid

OPTS="--daemon --pidfile=$RC_PIDFILE"
echo "executing: $PROG $OPTS"
echo "	check logs in: $DATA_DIR"

python $PROG $OPTS