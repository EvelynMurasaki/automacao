#!/bin/bash

log_file="wifi_monitor.log"

networks=$(sudo iwlist wlan0 scan | grep 'ESSID')

while read -r network; do
	ssid=$(echo "$network" | awk -F '"' '{print $2}')
	current_time=$(date '+%Y-%m-%d %H:%M:%S')

	if grep -q "$ssid" "$log_file"; then
	    sed -i "s/^$ssid .*/$ssid $current_time/" "$log_file"
	else
	   echo "$ssid $current_time $current_time" >> "$log_file"
	fi 
done <<< "$networks"
