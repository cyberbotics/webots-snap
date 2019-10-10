#!/usr/bin/env bash

until snapcraft push webots_R2019b-rev1_amd64.snap
do
  echo "Trying again"
done
