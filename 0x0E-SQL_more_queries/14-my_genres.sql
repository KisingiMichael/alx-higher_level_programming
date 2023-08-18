-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter

SELECT tg.name
  FROM tv_genres AS tg
       INNER JOIN tv_show_genres AS ts
       ON tg.id = ts.genre_id
       INNER JOIN tv_shows AS t
       ON t.id = ts.show_id
       WHERE t.title = "Dexter"
 ORDER BY tg.name;
