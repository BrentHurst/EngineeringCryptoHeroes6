#!/bin/bash

abort()
{
	killall -9 python3
	killall -9 flask
	killall -9 run_app.sh
	exit 1
}

trap 'abort' 0

if [ $# -eq 1 ] && [ "$1" = "clean" ]; then
	abort
fi

rm -f ech6.db
db/createDB.py

cd web
echo $PWD
./run_app.sh &
cd ..

while true; do
	marketstate/gatherMarketState.py
	trades/calculateTrades.py
	trades/makeTrades.py
	sleep 1h
done

	
