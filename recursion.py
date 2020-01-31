def bottles_of_bear(bob):
    """Prints 99 Bottle
       of Bear on the
       Wall lyrics.
       :param bob: Must
       be a positive
       integer.
    """
    if bob < 1:
        print("""No more
                 bottles
                 of bear
                 on the wall.
                 No more
                 bottles of 
                 bear.""")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of
             bear on the
             wall. {} bottles
             of bear. Take one
             down, pass it
             around, {} bottles
             of bear on the
             wall.
             """.format(tmp,tmp,bob))

    bottles_of_bear(bob)

bottles_of_bear(99)