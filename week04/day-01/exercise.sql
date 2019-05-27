--List the users who registered in 2018 with a .com email address and living in China
SELECT * FROM Users 
WHERE date_of_registration >= '2018-01-01' 
and date_of_registration <= '2018-12-31' 
and email like '%.com'
and country = 'China';

--How many users are there?
SELECT count(*) FROM Users 


--How many users registered in 2019?
SELECT count(*) FROM Users 
WHERE date_of_registration >= '2019-01-01'
AND date_of_registration <= '2019-12-31';


--How many users registered in January?
SELECT count(*) FROM Users
WHERE to_char(date_of_registration,'YYYY-mm-dd') like '%-01-%';


--Which country has the most users?
SELECT COUNT(ID) as user_num, country FROM Users 
group by country 
order by user_num DESC 
LIMIT 1;


--What is the gender ratio?
select count(gender), gender from Users group by gender;


--How many users left at least one field blank?
SELECT count(*) FROM Users
WHERE first_name is NUll
OR last_name is NULL
OR country is NULL
OR gender is Null;


--Which are the 3 most expensive products?
SELECT * FROM Products ORDER BY price DESC LIMIT 3;


--Which are the 4th and 5th cheapest products?
SELECT * FROM Products ORDER BY price ASC LIMIT 2 OFFSET 3 ;


--What is the average price for an electric product?
SELECT AVG(price) FROM Products WHERE category = 'Electronics';


--How much would it cost me to buy all the toys?
SELECT SUM(price) FROM Products WHERE category = 'Toys';


--What is the average rating?
SELECT AVG(rating) FROM reviews;


--Which product has the best average rating?
SELECT AVG(reviews.rating) AS avg_rating, reviews.product_id, Products.name
FROM reviews 
LEFT JOIN Products ON reviews.product_id = Products.id
GROUP BY reviews.product_id, Products.name
ORDER BY avg_rating DESC
LIMIT 1;


--Which product has the worst rating?
SELECT min(reviews.rating) AS worst_rating, reviews.product_id, Products.name
FROM reviews 
LEFT JOIN Products ON reviews.product_id = Products.id
GROUP BY reviews.product_id, Products.name
ORDER BY worst_rating ASC
LIMIT 1;


--Which products have no review?
SELECT * FROM Products 
WHERE id NOT IN
(SELECT DISTINCT(product_id) FROM reviews)

--How many reviews are 3 or below without comment?
select ccount(*) from reviews where rating <= 3 and comment is NULL;

--Which user reviewed the most?
SELECT count(*) as review_times, reviews.user_id, Users.username
FROM reviews
left join Users on Users.id = reviews.user_id
group by reviews.user_id, Users.username
order by review_times DESC
LIMIT 1;


--List the average rating for each product
SELECT AVG(reviews.rating) AS avg_rating, reviews.product_id, Products.name
FROM reviews 
LEFT JOIN Products ON reviews.product_id = Products.id
GROUP BY reviews.product_id, Products.name
ORDER BY product_id;

--How many days passed since the last review?
select current_date-max(date) as days_passed from reviews;