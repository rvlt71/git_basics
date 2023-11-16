# A dict is a key-value store, here's an example
apex_dict = {
    'bangalore': 'A legend with smoke grenades for tactical and artillery barrage for ultimate.',
    'wattson': 'A french elf.',
    'caustic': 'Stinky gas goes brrrrr...'
}

if __name__ == '__main__':

    print(apex_dict.items())

    # Print out the definition of 'wattson' from the dictionary:
    print(apex_dict['wattson'])

    for key, value in apex_dict.items():
        print(key, 'is defined as: ', value)