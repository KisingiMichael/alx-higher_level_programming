-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement

SELECT DISTINCT name
  FROM tv_genres AS tg
       INNER JOIN tv_show_genres AS ts
       ON tg.id = ts.genre_id

       INNER JOIN tv_shows AS t
       ON ts.show_id = t.id
       WHERE tg.name NOT IN
             (SELECT name
                FROM tv_genres AS tg
	             INNER JOIN tv_show_genres AS ts
		     ON tg.id = ts.genre_id

		     INNER JOIN tv_shows AS t
		     ON ts.show_id = t.id
		     WHERE t.title = "Dexter")
 ORDER BY tg.name;
