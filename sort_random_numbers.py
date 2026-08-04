import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def parse_numbers(s):
    return [float(x) for x in s.split()]  # supports integers and floats

def main():
    s = input("Enter numbers separated by spaces (or press Enter to generate random): ").strip()
    if not s:
        n = input("How many random numbers? (default 10): ").strip()
        n = int(n) if n.isdigit() and int(n) > 0 else 10
        arr = [round(random.uniform(-100, 100), 3) for _ in range(n)]
        print(f"Generated random list ({n} items):")
    else:
        try:
            arr = parse_numbers(s)
        except ValueError:
            print("Input contains invalid numbers. Use spaces to separate numbers.")
            return

    print("Unsorted:", arr)
    asc_builtin = sorted(arr)
    desc_builtin = sorted(arr, reverse=True)
    asc_quick = quicksort(arr)

    print("Sorted ascending (built-in):", asc_builtin)
    print("Sorted descending (built-in):", desc_builtin)
    print("Sorted ascending (quicksort):", asc_quick)

if __name__ == "__main__":
    main()
