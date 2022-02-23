```sql
insert into tracks (
	Name,
	MediaTypeId ,
	Milliseconds ,
	UnitPrice 
) values (
	'TestNamne',
	5,
	8374658,
	45.6
);

select * from tracks where TrackId = 3497;
delete from tracks where TrackId = 3497;


select tracks.TrackId , tracks.Name, genres.Name , albums.Title 
from tracks
	join genres on tracks.GenreId = genres.GenreId
	join albums on tracks.AlbumId = albums.AlbumId 
;


select g.Name as "N" , SUM(t.Milliseconds) / 1000 / 60 as "Delay", count(g.GenreId) as "Cnt"
from tracks as t
	inner join genres as g on t.GenreId = g.GenreId 
group by g.GenreId
order by "Delay" desc;

select t.Name , g.Name 
from tracks as t
	right join genres as g on t.GenreId = g.GenreId;
-- where g.GenreId is null;
	
select t.Name, g.Name
from genres as g
	left join tracks as t on g.GenreId = t.GenreId ;









```