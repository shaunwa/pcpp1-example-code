import pickle

default_settings = {
    'dark_mode_enabled': True,
    'sound_volume': 100,
    'brightness': 50
}

# Tuples (and other iterables)
# Functions in the top level module
# Classes in the top level module
# booleans, int, float, string

try:
    with open('pickle-data-types-output.pkl', 'rb') as file:
        settings = pickle.load(file)
except FileNotFoundError:
    settings = default_settings

print('Here are the current settings:')
print(settings)

new_volume = int(input('Enter a new value for the sound volume: '))
settings['sound_volume'] = new_volume

with open('pickle-data-types-output.pkl', 'wb') as file:
    pickle.dump(settings, file)