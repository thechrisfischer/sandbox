#!/bin/bash

function validate_ip {
    local iparray=()
    for i in "$@"
    do
        if [ $(echo $i | grep -o '\.' | wc -l) -eq 3 ] && [ $(echo $i | tr '.' ' ' | wc -w) -eq 4 ]; then
            iparray+=($i)
#                for OCTET in echo $1 | tr '.' ' '; do
#                        if ! [[ $OCTET =~ ^[0-9]+$ ]]; then
#                                echo "Parameter '$1' does not look like in IP Address (octet '$OCTET' is not numeric).";
#                                exit 1;
#                        elif [[ $OCTET -lt 0 || $OCTET -gt 255 ]]; then
#                                echo "Parameter '$1' does not look like in IP Address (octet '$OCTET' in not in range 0-255).";
#                                exit 1;
#                        fi
#                done
        fi
    done
    local output=${iparray[*]}
    echo $output
}


function get_ip {
    local ip_address
    ip_address=$(ifconfig | grep inet | awk '{print $2}' | tr '\n' ' ')
    local output
    output=$(validate_ip $ip_address)
    echo $output
}

function get_hostname {
    local output
    output=$(hostname)
    echo $output
}
function post_slack {
    local ip
    ip=$(get_ip)
    local hostname
    hostname=$(get_hostname)
    local slack_url="https://hooks.slack.com/services/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"
    local payload="{\"text\":\"$hostname :: $ip\"}"
    curl -X POST -H "Content-type: application/json" --data "$payload" $slack_url
}

post_slack
