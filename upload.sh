#!/usr/bin/env bash

count=0
until snapcraft push webots_R2019b-rev1_amd64.snap
do
  (( count ++ ))
  echo "Trying again ($count)"
done
