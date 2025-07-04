#!/bin/bash

cd clients/lgl_openapi_3.0_client
pip install -r test-requirements.txt
pip install -r requirements.txt
pytest