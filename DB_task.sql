
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Shoppers;
DROP TABLE IF EXISTS Customers;

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
    id bigint PRIMARY KEY,
    customer_id bigint NOT NULL,
    shopper_id bigint NOT NULL,
    Store VARCHAR(254),
    FOREIGN KEY (customer_id) REFERENCES Customers(id) ON UPDATE CASCADE ON
DELETE CASCADE,
    FOREIGN KEY (shopper_id) REFERENCES Shoppers(id) ON UPDATE CASCADE ON
DELETE CASCADE
);

INSERT INTO Customers
    (id,first_name,last_name,phone,address)
VALUES
    (1,'Customer1_fn','Customer1_ln','408-000-00-12','Some Addres1'),
    (2,'Customer2_fn','Customer2_ln','408-000-00-13','Some Addres2');

INSERT INTO Shoppers
    (id,first_name,last_name,phone)
VALUES
    (1,'Shopper_fn_1','Shopper_ln_2','409-431-0000'),
    (2,'Shopper_fn_2','Shopper_ln_4','409-432-0000');

INSERT INTO Orders
    (id,customer_id,shopper_id,store)
VALUES
    (1,1,1,'Store1'),
    (2,1,2,'Store1'),
    (3,2,2,'Store2');

SELECT id, store from Orders where customer_id = 1 and shopper_id = 1;

/*
 Relations:
    Customers to Orders -> 1 to * (Many)
    Shoppers to Orders ->  1 to * (Many)
    Customers to Shoppers -> * (Many) to * (Many)
 */
