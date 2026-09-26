# Smart Travel Planner

A beginner-friendly Python console program that estimates travel expenses for
a group and prints a formatted trip summary. It uses only Python's built-in
features and does not use files, databases, APIs, external libraries, or
classes.

## Run the program

Open a terminal in this folder and run:

```text
python smart_travel_planner.py
```

The program asks for the traveler's name, destination, number of travelers,
number of days, transportation cost per traveler, hotel cost per day, food cost
per traveler per day, and activity cost per traveler for the trip. Food is
entered separately because it is included in the requested cost summary.

## How it works

- Text details are stored as strings; traveler and day counts are integers;
	entered costs are converted to floating-point numbers.
- A dictionary groups related trip information under descriptive keys.
- Input helper functions reject blank names, invalid numbers, non-positive
	traveler/day counts, and negative costs.
- Separate calculation functions return each cost or average. The main
	function combines those returned values and displays the summary.

The totals use these formulas:

- Transportation = cost per traveler x travelers
- Hotel = hotel cost per day x days
- Food = food cost per traveler per day x travelers x days
- Activities = activity cost per traveler x travelers
- Overall trip cost = transportation + hotel + food + activities
- Cost per traveler = overall trip cost / travelers
- Average daily cost = overall trip cost / days

All amounts are shown in the currency entered by the user; the program does
not assume or convert a particular currency.