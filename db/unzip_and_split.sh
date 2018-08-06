#!/bin/bash
# should be a suitable number
LINES='300000'
unzip './postcode.zip' && split -d -l ${LINES} './postcode.txt' --verbose
