#! /bin/bash
path=$1
cd "$path" || exit
status=-1
while [ $status -ne 0 ]
do
  git commit -a -m "here."
  status=$?
done
