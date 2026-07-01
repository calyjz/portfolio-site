#!/bin/bash

tmux kill-server 2>/dev/null

cd portfolio-site

git fetch && git reset origin/main --hard

tmux new-session -d -s flask -c ~/portfolio-site 'source python3-virtualenv/bin/activate && pip install -r requirements.txt && flask run --host=0.0.0.0'
