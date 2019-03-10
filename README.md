# Cryptocurreny HFT Bot #

A relatively simple high frequency trading bot build to handle the volatile nature of cryptocurrency,

### Instructions ###
Download python3 here:
https://www.python.org/downloads/

Create and activate your virtual environment
```
virtualenv -p python3 path/to/new/environment
source path/to/new/environment/bin/activate
```
Install the dependencies
`pip install -r requirements.txt`

Run the bot
`./run.py`

### Saved Files & Data Structures ###
- `config.json` - configuration options for files, model parameters.

### Important Files ###
- `run.py` - main script, controls the model training and etl pipeline.
- `lstm.py` - LSTM built in Keras.
- `etl.py` - ETL pipeline class for standardizing the data.


This project is inspired by and build upon this project
https://github.com/jaungiers/Multidimensional-LSTM-BitCoin-Time-Series
