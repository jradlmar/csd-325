# Jared Morris
# Module 7 Assignment


def city_country(city, country, population=None, language=None):
    """Return a formatted city and country description."""

    location = f"{city}, {country}"

    if population is not None:
        location += f" - population {population}"

    if language is not None:
        location += f", {language}"

    return location


print(city_country("Santiago", "Chile"))
print(city_country("Atlanta", "United States", 510000))
print(city_country("Tokyo", "Japan", 14000000, "Japanese"))