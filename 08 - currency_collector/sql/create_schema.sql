create schema currency_statistics;

create table currency_statistics.bank
(
	id serial not null constraint bank_pkey primary key,
	full_name varchar(100) not null constraint bank_full_name_key unique,
	short_name varchar(100),
	description varchar(1024),
	url varchar(1024),
	is_enabled boolean default true,
	created timestamp default CURRENT_TIMESTAMP
);

create table currency_statistics.currency
(
	id serial not null constraint currency_pkey primary key,
	international_name varchar(100) not null,
	current_name varchar(100) not null constraint currency_current_name_key unique,
	description varchar(1024),
	is_enabled boolean default false,
	created timestamp default CURRENT_TIMESTAMP
);

create table currency_statistics.parsers
(
	id serial not null constraint parsers_pkey primary key,
	bank_id bigint not null constraint parsers_bank_id_fkey references currency_statistics.bank,
	module_name varchar(256) not null,
	class_name varchar(256) not null,
	created timestamp default CURRENT_TIMESTAMP
);

create table currency_statistics.rate
(
	id serial not null constraint rate_pkey primary key,
	bank_id bigint not null constraint rate_bank_id_fkey references currency_statistics.bank,
	currency_id bigint not null constraint rate_currency_id_fkey references currency_statistics.currency,
	sale numeric(12,2) not null,
	purchase numeric(12,2) not null,
	created timestamp default CURRENT_TIMESTAMP
);
