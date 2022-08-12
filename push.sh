#! /bin/bash
path=$1
cd "$path" || exit
status=-1
while [ $status -ne 0 ]
do
  git push -u origin main
  status=$?
done
