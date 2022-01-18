###########################################################################
#
#   Programming project #5
#
#       Algorithm
#
#       Function definitions
#       Prompt user for file name
#       Call open_file()
#       Open file
#           loop through every line of file
#               select specific records
#               Call str_plot()
#               Output results
#       Close file
#
###########################################################################

def open_file():
    ''' Takes no arguments, prompts for a file name and returns the file pointer to
that file. '''

    valid_filename = False
    filename = input("Please input a file to use: ")

    while valid_filename == False:

        # Check if file name exists
        try:
            with open(filename) as file:
                valid_filename = True
        except FileNotFoundError:
            print("Invalid filename, please try again")
            valid_filename = False
            filename = input("Please input a file to use: ")

    return filename


def str_plot(month_int, week_int, n_int, type_str):
    ''' This function uses the type_str argument to create the two different types of strings for
displaying either actual "deaths" or "expected" deaths. '''

    month = month_name(month_int)
    N = convert(n_int)

    # Plot deaths
    if type_str == "deaths":

        plot = N*"D"

    # Plot expected deaths
    elif type_str == "expected":

        plot = N * "E"

    # Return formatted data
    return "{:3s} ({:2d}) {:6,d}: {}".format(month, int(week_int), int(n_int), plot)


def convert(n):
    ''' Convert a 5-digit number into a 2-digit number by creating a decimal with one digit to the
right of the decimal point and then rounding. '''

    # Convert 5 digit number of deaths to specified float
    n_float = (int(n) // 1000) + ((int(n) - (int(n) // 1000)*1000)/1000)

    n_float_str = str(n_float)
    if n_float_str[3] == "5":
        return int(n_float_str[:2])
    else:
        return round(n_float)

def month_name(n):
    ''' This function takes as input an int representing a month and returns the three-character,
all-caps abbreviation for the month. '''

    n = str(n)

    MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV","DEC"]
    valid_months = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

    if n not in valid_months:

        print("Error in month_name, n={}".format(n))
        return "XXX"

    else:
        return MONTHS[int(n)-1]

def main():
    ''' This function calls open_file to get a file pointer and then using that file pointer reads
through the file one line at a time. '''

    fp = open_file()

    print("")

    # Formatting for data output
    print("Actual deaths (D) vs. Expected Deaths (E)")
    print("{:3s} ({:2s}) {:6s}".format("MTH", "WK", "Deaths"))

    with open(fp, "r") as file:

        # Skip header line of file
        first_line = file.readline()

        for line in file:

            line_list = line.split(",")

            # Select specific records
            if line_list[0] == "United States" and line_list[1] == "" and ("average" not in line_list[5]):

                # Output formatted data
                print(str_plot(line_list[6], line_list[7], line_list[8], "deaths"))
                print(str_plot(line_list[6], line_list[7], line_list[9], "expected"))

if __name__ == '__main__':
    main()
