from load_csv import load
import matplotlib.pyplot as plt


def covert_num(data_list):
    """
    Converts the numbers in the list to floats
    if contains 'k' or 'M' it converts them to 1000 or 1000000
    """
    try:
        for i in range(len(data_list)):
            if isinstance(data_list[i], str):
                if 'k' in data_list[i]:
                    data_list[i] = (float(data_list[i].replace('k', ''))
                                    * 1000)
                elif 'M' in data_list[i]:
                    data_list[i] = (float(data_list[i].replace('M', ''))
                                    * 1000000)
                else:
                    data_list[i] = float(data_list[i])
        return data_list
    except ValueError:
        return None


def main():
    """
    Plots the population of two countries over the years
    with the data from the csv file
    """
    try:
        csv = load("population_total.csv")

        years = csv.columns[1:].values
        years = [int(year) for year in years if int(year) <= 2050]

        country_1 = "Spain"
        country_2 = "France"
        c1_row = csv.loc[csv["country"] == country_1].values[0][1:len(years)+1]
        c2_row = csv.loc[csv["country"] == country_2].values[0][1:len(years)+1]
        covert_num(c1_row)
        covert_num(c2_row)

        plt.plot(years, c1_row, label=country_1, color='blue')
        plt.plot(years, c2_row, label=country_2, color='green')

        y_max = max(max(c1_row), max(c2_row))
        y_range = range(0, int(y_max), 20_000_000)

        plt.gcf().canvas.manager.set_window_title("Compare My Country")
        plt.yticks(y_range, [f"{i//1_000_000}M" for i in y_range])
        plt.xticks(range(min(years), max(years)+1, 40))
        plt.legend(loc='lower right')
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.show()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
