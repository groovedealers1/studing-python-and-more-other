import time


def one():
    print('start one')
    time.sleep(5)
    print('stop one')


def two():
    print('start two')
    time.sleep(5)
    print('stop two')


def third():
    print('start third')
    time.sleep(5)
    print('stop third')


def main():
    one()
    two()
    third()


if __name__ == '__main__':
    main()
