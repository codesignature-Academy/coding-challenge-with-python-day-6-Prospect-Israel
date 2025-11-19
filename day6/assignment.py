while True:

    text = input("Enter a number (or type 'quit' to exit): ")

    if text.lower() == "quit":
        break

    numb = int(text)

    squares = []
    for n in range(1, numb + 1):
        squares.append(n ** 2)

    print(squares)