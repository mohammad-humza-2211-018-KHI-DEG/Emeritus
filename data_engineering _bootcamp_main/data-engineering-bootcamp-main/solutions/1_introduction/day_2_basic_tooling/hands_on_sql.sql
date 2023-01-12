SELECT COUNT(*) AS cnt, u.name FROM articles a LEFT JOIN users u ON a.author_id = u.id GROUP BY u.id;
