#!/bin/python3

# validate json-schema. Include format-checker for email and ip-address checks.

import jsonschema
import json
import sys

if len(sys.argv) != 3:
    print("usage:\t./validate.py $JSON_FILE $JSON_SCHEMA")
    exit(1)

string = json.load(open(sys.argv[1]))
schema = json.load(open(sys.argv[2]))

jsonschema.validate(
    instance=string,
    schema=schema,
    format_checker=jsonschema.FormatChecker()
)

print("The JSON-String looks like it's valid. :)")