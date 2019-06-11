def decorator_name(func):

    def any_fun():
        print("ask me")

        func()
       
        print("asking")

    return any_fun


@decorator_name
def question():
    print("Just Im asking a quetion")


@decorator_name
def ans():
    print("Answering ")


question()
ans()