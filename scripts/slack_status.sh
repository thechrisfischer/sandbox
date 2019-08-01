#!/bin/bash

function validate_ip {
    local iparray=()
    local valid_octet
    for arg in "$@"
    do
        # check if the ip address has is in valid octect format - has 3 "." nad has 4 different character sets
        if [[ $(echo $arg | grep -o '\.' | wc -l) -eq 3 ]] && [[ $(echo $arg | tr '.' ' ' | wc -w) -eq 4 ]]; then
            valid_octet="true"

            for octet in $(echo $arg | tr '.' ' '); do
                if ! [[ $octet =~ ^[0-9]+$ ]]; then
                    valid_octet="false"
                fi

                if ! [[ $octet -ge 0 && $octet -le 255 ]]; then
                    valid_octet="false"
                fi

            done

            if [[ "$valid_octet" == "true" ]]; then
                iparray+=("$arg")
            fi

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
    ip="172.kjhfdjk.192.55.2"
    local hostname
    hostname=$(get_hostname)
    local slack_url="https://hooks.slack.com/services/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"
    local payload="{\"text\":\"$hostname :: $ip\"}"
    curl -X POST -H "Content-type: application/json" --data "$payload" $slack_url
}

post_slack
