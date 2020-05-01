def bottles_of_beer(bob):
    if bob < 1:
        print("""
            No more bottles of beer on the wall.
            NO more bottles of beer.
        """)
        return

    tmp = bob
    bob -= 1
    print("""
        {0} bottles of beer on the wall.
        {0} bottles of beer.
        Take one down, pass it around,
        {0} bottles of beer on the wall.
    """.format(tmp))

    bottles_of_beer(bob)

bottles_of_beer(99)
