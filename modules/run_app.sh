#!/bin/bash

db/createDB.py
web/run_app.sh &


while true; do
	marketstate/gatherMarketState.py
	trades/calculateTrades.py
	trades/makeTrades.py
	sleep 3600
done

	