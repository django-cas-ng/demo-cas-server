#!/bin/sh

#SCRIPTDIR=$(dirname $(readlink -f $0))
SCRIPTDIR=./demo_data

for f in ${SCRIPTDIR}/*.csv; do
  tablename=$(basename $f .csv)
  sqlite3 -separator ',' db.sqlite3 ".import $f $tablename"
done
