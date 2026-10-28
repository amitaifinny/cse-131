
# 1. Name:
#      Amitai Finlayson
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      This program receives a month and year as input and displays
#      the calendar for that given month and year.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of the program was remembering how to do error
#      handling and re-prompting. I had to figure out how to handle
#      non-integer input and numbers outside the valid range while
#      continuing to prompt the user until valid input was entered.
# 5. How long did it take for you to complete the assignment?
#      2 hours and 15 minutes.


def get_month():
    """Get month from the user, validate the input, and return the month."""

    # Track whether the user has entered a valid month.
    valid_start_month = False

    # Continue prompting until a valid month is entered.
    while not valid_start_month:
        try:
            # Get input from the user and convert it to an integer.
            month = int(input("Enter the month number: "))

            # Check whether the month is outside the valid range.
            if month < 1 or month > 12:
                print("Month must be between 1 and 12.")
            else:
                # Valid input allows the loop to terminate.
                valid_start_month = True

        # Handle input that cannot be converted to an integer.
        except ValueError:
            print("Month must be an integer.")

    # Verify that the returned month is within the valid range.
    assert isinstance(month, int)
    assert 1 <= month <= 12

    # Return the validated month to the caller.
    return month


def get_year():
    """Get year from the user, validate the input, and return the year."""

    # Track whether the user has entered a valid year.
    valid_start_year = False

    # Continue prompting until a valid year is entered.
    while not valid_start_year:
        try:
            # Get input from the user and convert it to an integer.
            year = int(input("Enter year: "))

            # The calendar only supports years from 1753 onward.
            if year < 1753:
                print("Year must be 1753 or later.")
            else:
                # Valid input allows the loop to terminate.
                valid_start_year = True

        # Handle input that cannot be converted to an integer.
        except ValueError:
            print("Year must be an integer.")

    # Verify that the returned year is valid.
    assert isinstance(year, int)
    assert year >= 1753

    # Return the validated year to the caller.
    return year


def is_leap_year(year: int) -> bool:
    """Return True if the given year is a leap year, False otherwise."""

    # Verify that the year is an integer in the supported range.
    assert isinstance(year, int)
    assert year >= 1753

    # Leap years are divisible by 4, except century years that
    # are not divisible by 400.
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def number_days_in_month(month, year):
    """Return the number of days in a given month, accounting for leap years."""

    # Verify that the arguments are valid integers.
    assert isinstance(month, int)
    assert isinstance(year, int)

    # Verify that the month and year are within the supported range.
    assert 1 <= month <= 12
    assert year >= 1753

    # February requires a leap-year check to determine its day count.
    if month == 2:
        return 29 if is_leap_year(year) else 28

    # Store the standard number of days for each month.
    standard_days = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    # Subtract 1 because Python lists use zero-based indexing.
    return standard_days[month - 1]


def compute_offset(month, year):
    """Return the weekday of the first day of the requested month."""

    # Verify that the requested month and year are valid.
    assert isinstance(month, int)
    assert isinstance(year, int)
    assert 1 <= month <= 12
    assert year >= 1753

    # Accumulate the days elapsed since January 1, 1753.
    elapsed_days = 0

    # Count all complete years before the requested year.
    for current_year in range(1753, year):

        # Leap years contribute 366 days.
        if is_leap_year(current_year):
            elapsed_days += 366
        else:
            # Non-leap years contribute 365 days.
            elapsed_days += 365

    # Count all complete months before the requested month.
    for current_month in range(1, month):

        # Add the number of days in each preceding month.
        elapsed_days += number_days_in_month(current_month, year)

    # Determine the weekday shift after complete weeks are removed.
    position_shift = elapsed_days % 7

    # January 1, 1753 was a Monday, represented by weekday 1.
    beginning_day = 1 + position_shift

    # Return a weekday number from 0 (Sunday) to 6 (Saturday).
    return beginning_day % 7


def display_table(dow, num_days):
    """Display a calendar table."""

    # Verify that both arguments are integers.
    assert(type(num_days) == type(dow) == type(0))

    # Verify that the weekday is between Sunday and Saturday.
    assert(0 <= dow <= 6)

    # Verify that the month contains between 28 and 31 days.
    assert(28 <= num_days <= 31)

    # Display the weekday header.
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent the first week to align the first day correctly.
    for indent in range(dow):
        print("    ", end='')

    # Display each day of the requested month.
    for dom in range(1, num_days + 1):

        # Print the day right-aligned in a four-character field.
        print(repr(dom).rjust(4), end='')

        # Advance the current weekday.
        dow += 1

        # Start a new line after Saturday.
        if dow % 7 == 0:
            print("")

    # End the final week with a newline if necessary.
    if dow % 7 != 0:
        print("")


def main():
    """Coordinate user input, calendar calculations, and output."""

    # Prompt the user for a valid month.
    month = get_month()

    # Prompt the user for a valid year.
    year = get_year()

    # Determine the number of days in the requested month.
    num_days = number_days_in_month(month, year)

    # Determine the weekday on which the month begins.
    dow = compute_offset(month, year)

    # Display the calendar using the calculated values.
    display_table(dow, num_days)


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    main()