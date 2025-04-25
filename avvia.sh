#!/bin/bash

cd src/server/backend
sudo python server.py &
BACKEND_PID=$!
echo "Backend online!"
cd ../../.. 

sleep 2

cd src/server/frontend
python api.py &
FRONTEND_PID=$!
echo "API online!"
cd ../../..
pwd

cleanup() {
    kill $BACKEND_PID
    kill $FRONTEND_PID
    echo "Uscito."
}

# Trap SIGINT (Ctrl+C) and call cleanup
trap cleanup SIGINT


wait $BACKEND_PID
wait $FRONTEND_PID