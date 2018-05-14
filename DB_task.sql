drop table if exists Orders;
drop table if exists Shoppers;
drop table if exists Customers;

CREATE TABLE Shoppers (
    id bigint PRIMARY KEY,
    First_name VARCHAR(254) NOT NULL,
    Last_name VARCHAR(254) NOT NULL,
    Phone VARCHAR(254)
);

CREATE TABLE Customers (
    id bigint PRIMARY KEY,
    First_name VARCHAR(254) NOT NULL,
    Last_name VARCHAR(254) NOT NULL,
    Phone VARCHAR(254),
    Address VARCHAR(254)
);

CREATE TABLE Orders (
    id bigint NOT NULL,
    customer_id bigint REFERENCES Customers,
    shopper_id bigint REFERENCES Shoppers,
    Store VARCHAR(254)
);

INSERT INTO "customers"("id","first_name","last_name","phone","address") VALUES (1,E'Customer1_fn',E'Customer1_ln',E'408-000-00-12',E'Some Addres1'), (2,E'Customer2_fn',E'Customer2_ln',E'408-000-00-13',E'Some Addres2');

INSERT INTO "shoppers"("id","first_name","last_name","phone") VALUES (1,E'Shopper_fn_1',E'Shopper_ln_2',E'409-431-0000'),
(2,E'Shopper_fn_2',E'Shopper_ln_4',E'409-432-0000');

INSERT INTO "orders"("id","customer_id","shopper_id","store") VALUES
(1,1,1,E'Store1'),
(1,1,2,E'Store1'),
(1,2,2,E'Store2');

SELECT id, store from Orders where customer_id = 1 and shopper_id = 1;

/*
 Relations: 
    Customers to Orders -> 1 to * (Many)
    Shoppers to Orders ->  1 to * (Many)
    Customers to Shoppers -> * (Many) to * (Many)
 */
