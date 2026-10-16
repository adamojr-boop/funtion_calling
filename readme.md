###############

source venv/bin/activate
poetry install

chainlit run tools/__init__.py -w

###############