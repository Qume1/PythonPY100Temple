def count_even_numbers(list_numbers: list) -> int:
    return len([even_num for even_num in list_numbers if even_num % 2 == 0])


if __name__ == "__main__":
    print(count_even_numbers(list(range(1, 25))))
