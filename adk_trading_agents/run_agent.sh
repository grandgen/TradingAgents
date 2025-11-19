#!/bin/bash
export $(cat .env | xargs)
python3 -m adk run . --replay replay_team.json
