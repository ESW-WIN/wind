create table wind (
id serial primary key,
time integer unique,
wind_speed real,
wind_direction real,
gust_speed real,
gust_direction real,
temperature real,
pressure real,
relative_humidity real
);
