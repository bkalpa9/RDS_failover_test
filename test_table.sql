CREATE TABLE t_random AS
SELECT
    s,
    md5(random()::text)
FROM
    generate_Series(1, 5) s;

