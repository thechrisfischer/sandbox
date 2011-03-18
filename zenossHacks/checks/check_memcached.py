#!/bin/bash

usage() {
  echo "query_memcache -H hostname [-p port]"
}

while getopts "H:p:" OPT; do
  case $OPT in
    H)
      HOST=$OPTARG
      ;;
    p)
      PORT=$OPTARG
      ;;
    ?)
      usage
      exit
      ;;
  esac
done

if [[ -z "$HOST" ]] || [[ -z "PORT" ]]; then
  usage
  exit 1
fi

VALUES=`echo -e "stats\r\nquit\r\n" | nc $HOST $PORT | sed '/END/d' | sed 's/^STAT //g' | tr " " "=" | tr "\r\n" " " | sed 's/\s\s/;;;0 /g'`
if [ -z "$VALUES" ]; then 
  echo "CRITICAL - could not connect to $HOST port $PORT"
  exit 1
else
  echo "memcache stats |$VALUES"
  exit 0 
fi

