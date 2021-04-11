#!/usr/bin/env bash
echo -en "Press q to exit \n"
while true; do
        python3 python/main.py

        read -t 60 -N 1 input
        if [[ $input = "q" ]] || [[ $input = "Q" ]]; then
                break
        fi
        #sleep 10
done
