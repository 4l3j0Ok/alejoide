#!/bin/bash
# ./.venv/bin/python -m pip install --upgrade reflex
# rx_version=$(./.venv/bin/python -m reflex --version)
# sed -i "s/reflex==.*/reflex==$rx_version/" requirements.txt
pipenv update reflex
rx_version=$(pipenv run reflex --version)
sed -i "s/reflex==.*/reflex==$rx_version/" requirements.txt