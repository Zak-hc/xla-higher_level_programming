#!/bin/bash
#script that takes in aURL, sends GETrequest to theURL,anddisplaythe bodyoftherespons
curl -s -L GET "$1"
