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
    try:
        csv = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        csv1 = load("life_expectancy_years.csv")

        years = csv1["1900"].values
        gdp = csv["1900"].values
        covert_num(years)
        covert_num(gdp)

        plt.gcf().canvas.manager.set_window_title("Draw My Year")
        plt.scatter(gdp, years, marker='o')
        plt.xscale('log')
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
        plt.title("1900")
        plt.xlabel("Gross doomestic product")
        plt.ylabel("Life Expectancy")
        plt.show()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
