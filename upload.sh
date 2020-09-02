#!/usr/bin/env bash

count=0
version=`cat webots/resources/version.txt`
version=${version/ revision /-rev}
until snapcraft upload webots_${version}_amd64.snap
do
  (( count ++ ))
  echo "Trying again ($count)"
done
