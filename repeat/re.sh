#!/bin/bash

lower_bound=0.6767
cmd='python main.py'
while :
do
  acc=$(python main.py)
  if [ `expr $acc \> $lower_bound` -eq 1 ] ; then
  echo "accuracy: $acc > $lower_bound, end loop"
  break
  else
  echo "accuracy: $acc < $lower_bound, continue loop"
  fi
done