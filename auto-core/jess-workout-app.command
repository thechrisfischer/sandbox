#!/bin/sh

#TODO this file needs to be converted to python to run on windows and mac
workout_list=$(pwd)/Desktop/auto-core/workouts

function lets_workout {
    echo "How long are we working out for??"
    read time

    echo "We are going to workout for $time minutes"
    say "We are going to workout for $time minutes"

    exercises=$(($time*2))
    echo "`pwd`"
    while [ $exercises -gt 0 ]

    do
        exercise=`cat $workout_list | sort -R | head -n 1`
        echo "$exercise"
        say "lets do $exercise for 30 seconds"
        echo "\n\n"
        sleep 15
        say "15 seconds left"
        echo "15 seconds to go\n"
        sleep 7
        say "7 seconds left doing great"
        echo "7 seconds to go\n"
        sleep 8
        say "3 seconds you're an animal"
        echo "3 seconds to go\n"
        sleep 3
        exercises=$(($exercises-1))
    done
}

lets_workout
