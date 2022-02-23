# SQLite
# SELECT
# INSERT
# UPDATE
# DELETE

# CRUD - Create, Read, Update, Delete

"""
select *
from customers
where FirstName = 'Mark';

update customers
set PhoneNumber = '87436587236482', City = 'Odessa'
where CustomerId = 14;

insert into customers (
	FirstName,
	LastName
) values (
	'Ivan',
	'Petrov'
);

select *
from customers
where FirstName = 'Ivan';

delete from customers where CustomerId = 67;
"""