#!/bin/bash

while true; do
    sudo tshark -i eth0 -w capture.pcap -a duration:60

    tshark -r capture.pcap -T fields -E header=y -E separator=, -E quote=d -E occurrence=f -e ip.src -e ip.dst -e ip.len -e ip.flags.df -e ip.flags.mf -e ip.fragment -e ip.fragment.count -e ip.fragments -e ip.ttl -e ip.proto -e tcp.window_size -e tcp.ack -e tcp.seq -e tcp.len -e tcp.stream -e tcp.urgent_pointer -e tcp.flags -e tcp.analysis.ack_rtt -e tcp.segments -e tcp.reassembled.length -e http.request -e udp.port -e frame.time_relative -e frame.time_delta -e tcp.time_relative -e tcp.time_delta > capture_df.csv

    python3 cleanup.py capture_df.csv

done
