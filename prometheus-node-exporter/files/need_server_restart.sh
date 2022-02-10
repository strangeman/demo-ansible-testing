#!/bin/bash

/usr/bin/needs-restarting -r > /dev/null
NEED_RESTART=$?

# Adjust as needed.
TEXTFILE_COLLECTOR_DIR=/opt/textfile_collector/

mkdir -p $TEXTFILE_COLLECTOR_DIR

echo "need_server_restart $NEED_RESTART"
