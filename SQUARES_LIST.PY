def square_numbers(start, end):
    squares = []

    for num in range(start, end + 1):
        squares.append(num ** 2)

    even_squares = []
    odd_squares = []

    for sq in squares:
        if sq % 2 == 0:
            even_squares.append(sq)
        else:
            odd_squares.append(sq)

    print("All Squares:", squares)
    print("Even Squares:", even_squares)
    print("Odd Squares:", odd_squares)

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

square_numbers(start, end)