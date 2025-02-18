WITH cleaned_data AS (
    SELECT 
        "Country/Region" AS country,
        "Province/State" AS province,
        "Lat" AS latitude,
        "Long" AS longitude,
        *
    FROM covid_cases
)
SELECT * FROM cleaned_data;
