
def color_name(value):
    names = {
        0: "Red",
        1: "White",
        2: "Blue"
    }
    return names[value]


def sort_colors(capsules):
    low = 0
    mid = 0
    high = len(capsules) - 1
    swaps = 0
    step = 1

    print("\n=== Conveyor Belt Sorting ===")
    print("Initial capsules:", capsules)

    while mid <= high:
        print(f"\nStep {step}:")
        print("Current belt:", capsules)
        print(f"Pointers -> low={low}, mid={mid}, high={high}")

        if capsules[mid] == 0:
            print(f"{color_name(capsules[mid])}: move to the red section.")
            if low != mid:
                capsules[low], capsules[mid] = capsules[mid], capsules[low]
                swaps += 1
                print(f"Swap indexes {low} and {mid}: {capsules}")
            low += 1
            mid += 1

        elif capsules[mid] == 1:
            print("White: already in the middle section.")
            mid += 1

        else:
            print(f"{color_name(capsules[mid])}: move to the blue section.")
            if mid != high:
                capsules[mid], capsules[high] = capsules[high], capsules[mid]
                swaps += 1
                print(f"Swap indexes {mid} and {high}: {capsules}")
            high -= 1
            # Do not advance mid here:
            # the swapped-in capsule still needs inspection.

        step += 1

    print("\n=== Final Results ===")
    print("Sorted capsules:", capsules)
    print("Total swaps:", swaps)
    print("Red capsules:", capsules.count(0))
    print("White capsules:", capsules.count(1))
    print("Blue capsules:", capsules.count(2))

    return capsules, swaps


def main():
    print("=" * 45)
    print("     ROBOTICS FACTORY: SORT COLORS")
    print("=" * 45)
    print("0 = Red | 1 = White | 2 = Blue")

    raw_input = input("\nEnter capsule colors separated by spaces: ")

    try:
        capsules = list(map(int, raw_input.split()))

        if not capsules:
            print("Please enter at least one capsule.")
            return

        if any(color not in (0, 1, 2) for color in capsules):
            print("Invalid input. Use only 0, 1, and 2.")
            return

        sort_colors(capsules)

    except ValueError:
        print("Invalid input. Enter integers separated by spaces.")


if __name__ == "__main__":
    main()
