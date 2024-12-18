import load_csv as lc
import matplotlib.pyplot as plt


def main():
    """
    Plots the life expectancy in a country over the years
    with the data from the csv file
    """

    try:
        csv = lc.load("life_expectancy_years.csv")

        years = csv.columns[1:].values
        years = [int(year) for year in years]

        country = "Spain"
        row_country = csv.loc[csv["country"] == f"{country}"].values[0][1:]

        plt.plot(years, row_country)
        plt.title(f"{country} Life expectancy Projections")
        plt.xticks(range(min(years), max(years)+1, 40))
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.show()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
