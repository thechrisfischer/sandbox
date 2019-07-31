#!/bin/bash

function check_ip {
    local ip=$1
    local iparray=()
    if [ `echo $ip | grep -o '\.' | wc -l` -eq 3 ] && [ `echo $ip | tr '.' ' ' | wc -w` -eq 4 ]; then
        iparray+=($ip)
    else
        exit 1
#            for OCTET in echo $1 | tr '.' ' '; do
#                    if ! [[ $OCTET =~ ^[0-9]+$ ]]; then
#                            echo "Parameter '$1' does not look like in IP Address (octet '$OCTET' is not numeric).";
#                            exit 1;
#                    elif [[ $OCTET -lt 0 || $OCTET -gt 255 ]]; then
#                            echo "Parameter '$1' does not look like in IP Address (octet '$OCTET' in not in range 0-255).";
#                            exit 1;
#                    fi
#            done
    fi
    echo ${iparray[*]}
}


function get_ip {
    local ip_address=`ifconfig | grep inet | awk {'print $2'}`
    local value=$(check_ip $ip_address)
    echo $value
}


function post_slack {
    local ip=$(get_ip)
    local slack_url="https://hooks.slack.com/services/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"
    local payload="{\"text\":\"$ip\"}"
    curl -X POST -H "Content-type: application/json" --data "$payload" $slack_url
}

post_slack