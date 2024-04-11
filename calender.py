import calendar

def display_calendar(year, month):
    cal = calendar.month(year, month)
    print(f"Calendar for {calendar.month_name[month]} {year}:\n")
    print(cal)

def main():
    try:
        year = int(input("Enter the year: "))
        month = int(input("Enter the month (1-12): "))
        if 1 <= month <= 12:
            display_calendar(year, month)
        else:
            print("Please enter a valid month (1-12).")
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
