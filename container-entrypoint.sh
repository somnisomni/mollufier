#!/bin/bash
### Runner container entrypoint for Mollufier ###

# Start the frontend
npx http-server --port 8080 -P http://localhost:8080? ./frontend &

# Start the backend
FLASK_PORT=8081 FLASK_HOST=0.0.0.0 python3 ./backend/index.py &

# Wait for processes (remaining running status)
wait -n

# Exit with errorcode
exit $?
