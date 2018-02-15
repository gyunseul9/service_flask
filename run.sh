#!/bin/bash

source /workspace/gyunseul9/bin/activate


NEW_RELIC_CONFIG_FILE=/workspace/gyunseul9/newrelic.ini /usr/bin/newrelic-admin run-program /usr/bin/python3 /workspace/gyunseul9/app.py
