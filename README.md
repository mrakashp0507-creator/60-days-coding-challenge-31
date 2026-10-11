# Day 31 – Sorting Systems: Sort Colors

## Overview
This project sorts red, white, and blue capsules on a simulated factory conveyor belt. It implements the Dutch National Flag algorithm without using built-in sorting functions.

## Color Mapping
- `0` = Red
- `1` = White
- `2` = Blue

## Example

**Input**
```text
2 0 2 1 1 0
```

**Output**
```text
0 0 1 1 2 2
```

The program also visualizes pointer movements and counts actual swaps.

## Algorithm: Dutch National Flag

Three pointers are used:

- `low`: boundary for red capsules.
- `mid`: current capsule being examined.
- `high`: boundary for blue capsules.

### Rules
1. If the current value is `0`, swap it toward the red section and advance `low` and `mid`.
2. If the current value is `1`, advance `mid`.
3. If the current value is `2`, swap it toward the blue section and decrease `high`. Re-examine the current position because the swapped capsule has not been checked yet.

## Complexity Analysis
- **Time:** O(n)
- **Auxiliary space:** O(1)
- **Built-in sorting:** Not used.

The algorithm is scalable because it processes the array in one pass using constant extra working space.

## Swap Optimization
The program performs a swap only when the two indexes differ. It counts these actual swaps and displays the final total.

The Dutch National Flag algorithm uses efficient in-place swaps, but it does not guarantee the globally minimum possible number of swaps for every input.

## How to Run
1. Install Python 3.
2. Open the project folder in VS Code.
3. Create `day31_sort_colors.py` and paste the code.
4. Open the terminal and execute:

```bash
python day31_sort_colors.py
```

## Test Cases

| Input | Expected output |
|---|---|
| `[2, 0, 2, 1, 1, 0]` | `[0, 0, 1, 1, 2, 2]` |
| `[2, 0, 1]` | `[0, 1, 2]` |
| `[0, 0, 0]` | `[0, 0, 0]` |
| `[2, 2, 1, 1]` | `[1, 1, 2, 2]` |
| `[1]` | `[1]` |

## Real-World Applications
- Robotics and conveyor-belt sorting
- Inventory categorization
- Partitioning data into groups
- Efficient array processing

## Learning Outcomes
- Implemented the Dutch National Flag algorithm.
- Practiced three-pointer optimization.
- Avoided built-in sorting.
- Visualized pointer movements.
- Analyzed time and auxiliary-space complexity.
