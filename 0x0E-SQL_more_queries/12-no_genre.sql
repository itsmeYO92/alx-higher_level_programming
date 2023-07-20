-- select shows by genre

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
