/*Where is this weather station?*/
select country_code  from weather_station where id = '724940:23234';

-- Show the temperature for June 1st, 2008.
select temperature from raw_weather_data where wsid = '724940:23234' and year = 2008 and month = 06 and day =1 allow filtering;

-- Show the temperatures for June 1st, 2008 from 9AM to 3PM.
select temperature from raw_weather_data where wsid = '724940:23234' and year = 2008 and month = 06 and day =1  and hour >= 9 and hour <= 13 allow filtering;

-- What is the average elevation of the weather stations in Indiana?
select AVG(elevation) from weather_station where country_code = 'IN'allow filtering;

-- What is the latitude of the northest weather station in Texas?
select max(lat) from weather_station where state_code = 'TX' allow filtering;

-- Insert the current temperature for today.

-- Fill the daily_aggregate_temperature table.