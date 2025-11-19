#!/bin/bash
export $(cat .env | xargs)
/home/jules/.pyenv/versions/3.10.19/bin/adk run . --replay replay_team.json
