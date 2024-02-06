class Robot():
    pass

if __name__ == "__main__":
    x = Robot()
    y = Robot()
    # we have created a reference y2 to y, i.e. y2 is an alias name for y.
    y2 = y
    print(y == y2)
    print(y == x)