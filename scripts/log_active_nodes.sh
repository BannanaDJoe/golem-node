#!/bin/bash
script_full_path=$(dirname "$0")
while true;
do
    echo -n "$(date +"[%F %H:%M:%S]") "
    echo -n "Nodes active: $("$script_full_path"/utils/get_active_nodes.sh) - "
    echo "Total processed last 1h: $("$script_full_path"/utils/get_processed_last_hr.sh)"
    sleep 60
done
