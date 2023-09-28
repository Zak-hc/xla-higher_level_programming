#!/bin/bash
#script that takes in aURL, sends GETrequest to theURL,anddisplaythe bodyoftheresponse
a=$(curl -sI "$1");if [ "$a eq 200" ]; then echo "Route 2"; fi;
