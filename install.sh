#!/bin/bash
sqlite3 db/quotes.db < install/create_quotes.sql
sqlite3 db/pm.db < install/create_pm.sql
