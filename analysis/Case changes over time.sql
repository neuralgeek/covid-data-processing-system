SELECT date, SUM(cases) as daily_cases
FROM covid_cleaned
GROUP BY date
ORDER BY date;