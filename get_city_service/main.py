from tools import *


# search name is in lower case!
def find_by_name(search_name: str, cities_array: np.array):
    for city in cities_array:
        lower_city = city.lower()

        if search_name == lower_city:
            return city

    # check additional names dict
    for additional_name in additional_names_dict:
        if search_name == additional_name.lower():
            return additional_names_dict[additional_name]

    return None


# search name is in lower case!
def find_by_min_hamming_dist(search_name: str, cities_array: np.array):
    min_dist = 1024
    most_similar = None

    for city in cities_array:
        lower_city = city.lower()
        cur_dist = calc_hamming_dist(search_name, lower_city)

        if cur_dist < min_dist:
            min_dist = cur_dist
            most_similar = city

    for additional_name in additional_names_dict:
        additional_name_lower = additional_name.lower()
        cur_dist = calc_hamming_dist(search_name, additional_name_lower)

        if cur_dist < min_dist:
            min_dist = cur_dist
            most_similar = additional_names_dict[additional_name]   # get full city name by additional name

    return most_similar, min_dist


# 1 - use complete matching
# 2 - if don't work - see min hamming distance
def find_city(message_text: str, country: str = None) -> str:
    if country is None:
        # select all cities
        cities_df = get_all_cities_df()
    else:
        if country not in countries:
            raise Exception(f"No country with such name - '{country}', select one of supported - {countries}")
        cities_df = get_country_cities_df(country)

    city_names_list = cities_df['name'].to_numpy()
    text_tokens = get_tokens(message_text.lower())

    # 1. find by complete matching:

    for token in text_tokens:
        result = find_by_name(token, city_names_list)

        if result is not None:
            return result

    # 2. no matches on the previous step - use min hamming distance:
    min_dist = 1024
    result = None

    for token in text_tokens:
        most_similar, cur_dist = find_by_min_hamming_dist(token, city_names_list)

        if cur_dist < min_dist:
            min_dist = cur_dist
            result = most_similar

    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        print(f"Choose country from list {countries}\n or press 'Enter' if you want search in CIS:")
        country = input()

        if country == "":
            country = None
            break
        elif country not in countries:
            print(f"No country with name '{country}' supported!")
        else:
            break

    while True:
        print("Enter the message, or 'end' if you want to exit application:")
        message = input()

        if len(message) == 0:
            print("message should not be an empty string!")
            continue
        elif message == 'end':
            print("exit app")
            break

        result = find_city(message, country)
        print(f"City - {result}")



