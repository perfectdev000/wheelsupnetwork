#!/bin/bash

psql -U wheelsup -d postgres -c "DROP DATABASE wheelsup"
psql -U wheelsup -d postgres -c "CREATE DATABASE wheelsup"
