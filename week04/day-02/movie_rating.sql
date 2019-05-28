--Q1:Find the titles of all movies directed by Steven Spielberg
select title from movie where director = 'Steven Spielberg'


--Q2:Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order. 
select distinct(m.year) from movie m join rating r on m.mid = r.mid where r.stars in (4, 5) order by m.year ASC;


--Q3:Find the titles of all movies that have no ratings.
select title from movie m where m.mid not in (select distinct mid from rating );


--Q4:Some reviewers didn't provide a date with their rating. Find the names of all reviewers who have ratings with a NULL value for the date. 
select re.name from reviewer re left join rating r on re.rid = r.rid where r.ratingdate is null;


--Q5:Write a query to return the ratings data in a more readable format: reviewer name, movie title, stars, and ratingDate. Also, sort the data, first by reviewer name, then by movie title, and lastly by number of stars. 
select re.name as reviewer_name, 
m.title as movie_title, 
r.stars as stars, 
r.ratingdate as ratingDate 
from movie m join rating r on m.mid = r.mid 
join reviewer re on re.rid = r.rid
order by reviewer_name, movie_title, stars;



--Q1:Find the names of all reviewers who rated Gone with the Wind. 
select distinct re.name
from movie m join rating r on m.mid = r.mid 
join reviewer re on re.rid = r.rid
where m.title = 'Gone with the Wind';


--Q2:For any rating where the reviewer is the same as the director of the movie, return the reviewer name, movie title, and number of stars.
select re.name, m.title, r.stars
from movie m join rating r on m.mid = r.mid 
join reviewer re on re.rid = r.rid
where re.name = m.director;


--Create a view where you display the reviewer's name and the amount of their review
create view amount_of_review as select re.name, count(r.rid) from rating r join reviewer re on r.rid = re.rid 
group by r.rid, re.name;


--Create a view where you display the movies which have no review
create view movies_with_no_review as 
select * from movie m where m.mid not in(select distinct mid from rating);


--Create a view where you display all the directors (do not include null values)
create view all_directors as
select distinct director from movie where director is not null;


--Create a view where you display the movie title and the average rating
create view movie_avg_rating as
select m.title, avg(stars) as avg_rating from rating r join movie m on r.mid = m.mid group by m.title



--Joins and subqueries - PostgreSQL Exercises
--Retrieve the start times of members' bookings 
select b.starttime from cd.bookings b left join cd.members m on b.memid = m.memid where m.firstname = 'David' 
and surname = 'Farrell';


--Work out the start times of bookings for tennis courts
select b.starttime as start, f.name from cd.bookings b 
inner join cd.facilities f on b.facid = f.facid 
where f.name like 'Tennis Court%'
and b.starttime >= '2012-09-21'
and b.starttime < '2012-09-22'
order by b.starttime ASC;

--Produce a list of all members who have recommended another member
select m.firstname, m.surname from cd.members m 
where m.memid in (select distinct recommendedby from cd.members)
order by m.surname, m.firstname;

--Produce a list of all members, along with their recommender
select m.firstname as memfname, m.surname as memsname, rec.firstname as recfname, rec.surname as recsname
from cd.members m
left join cd.members rec on rec.memid = m.recommendedby
order by memsname, memfname;

--Produce a list of all members who have used a tennis court 
select distinct concat(m.firstname, ' ', m.surname)as member, f.name as facility 
from cd.members m 
join cd.bookings b on m.memid = b.memid
join cd.facilities f on b.facid = f.facid
where f.name like 'Tennis Court%'
order by member;

--Produce a list of costly bookings 
select concat(m.firstname, ' ', m.surname) as member, f.name as facility, f.membercost*b.slots as cost
from cd.members m
join cd.bookings b on m.memid = b.memid
join cd.facilities f on f.facid = b.facid
where b.starttime >= '2012-09-14' and b.starttime < '2012-09-15'
and b.memid <> 0
and f.membercost*b.slots > 30

union all

select concat(m.firstname, ' ', m.surname) as member, f.name as facility, f.guestcost*b.slots as cost
from cd.members m
join cd.bookings b on m.memid = b.memid
join cd.facilities f on f.facid = b.facid
where b.starttime >= '2012-09-14' and b.starttime < '2012-09-15'
and b.memid = 0
and f.guestcost*b.slots > 30
order by cost desc;


--Produce a list of all members, along with their recommender, using no joins. 
select distinct concat(m.firstname, ' ', m.surname) as member,
(select concat(mm.firstname, ' ', mm.surname)as recommender 
from cd.members mm
where mm.memid = m.recommendedby)

from cd.members m 
order by member;

--Produce a list of costly bookings, using a subquery
select member, facility, cost from
(
  select concat(m.firstname, ' ', m.surname) as member,f.name as facility, f.guestcost*b.slots as cost
  from cd.members m
  join cd.bookings b on m.memid = b.memid
   join cd.facilities f on f.facid = b.facid
   where b.starttime >= '2012-09-14' and b.starttime < '2012-09-15'
   and b.memid = 0
  
  union all
  
  select concat(m.firstname, ' ', m.surname) as member, f.name as facility, f.membercost*b.slots as facility
  from cd.members m
  join cd.bookings b on m.memid = b.memid
   join cd.facilities f on f.facid = b.facid
   where b.starttime >= '2012-09-14' and b.starttime < '2012-09-15'
   and b.memid <> 0
 )as booking_cost
 where booking_cost.cost > 30;
  

