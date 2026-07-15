# Jared Morris
# Module 4 Assignment
# Sitka High and Low Temperatures Program
#
# Changes made:
# 1. Added a menu for Highs, Lows, or Exit.
# 2. Added low temperature graph in blue.
# 3. Allowed the program to loop until the user selects exit.
# 4. Added an exit message.

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt


def get_weather_data():
    filename = 'sitka_weather_2018_simple.csv'

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, highs, lows = [], [], []

        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])

            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows


def plot_highs(dates, highs):
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    plt.title("Daily High Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def plot_lows(dates, lows):
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')

    plt.title("Daily Low Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def main():
    dates, highs, lows = get_weather_data()

    while True:
        print("\nSitka Weather Menu")
        print("Type HIGHS to view high temperatures.")
        print("Type LOWS to view low temperatures.")
        print("Type EXIT to quit.")

        choice = input("jm: ").lower()

        if choice == "highs":
            plot_highs(dates, highs)
        elif choice == "lows":
            plot_lows(dates, lows)
        elif choice == "exit":
            print("Thank you for using the Sitka Weather Program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please type HIGHS, LOWS, or EXIT.")


main()