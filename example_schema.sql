drop table if exists examples;


create table examples
(
    id   serial
        constraint examples_pk
            primary key,
    name varchar
);
