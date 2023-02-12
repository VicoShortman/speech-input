# Test File
from speechinput import sinput


def main():
    # With prefix
    sinput('Say something:')

    # silence output
    inp = sinput('silent')
    print(f'You said: {inp}')


if __name__ == '__main__':
    main()
