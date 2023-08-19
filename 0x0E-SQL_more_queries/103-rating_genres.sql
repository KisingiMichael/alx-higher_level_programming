-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement

SELECT name, SUM(rate) AS rating
  FROM tv_genres AS tg
       INNER JOIN tv_show_genres AS ts
       ON ts.genre_id = tg.id
       INNER JOIN tv_show_ratings AS r
       ON r.show_id = ts.show_id
 GROUP BY name
 ORDER BY rating DESC;
