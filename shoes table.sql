CREATE TABLE shoe(
	id SERIAL PRIMARY KEY,
	Brand VARCHAR(50),
	Model VARCHAR(50),
	Mins INT,
	price_usd FLOAT,
	Season TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

INSERT INTO shoe (Brand, Model, Mins, price_usd) VALUES
('Nike',   'Kobe 6 Protro',       63189, 190.00),
('Nike',   'Sabrina 2',           32822, 130.00),
('Nike',   'Air Zoom G.T. Cut 3', 29436, 190.00),
('Nike',   'Kobe 5 Protro',       25949, 190.00),
('Jordan', 'Air Jordan 39',       23647, 200.00),
('Nike',   'Nike Book 1',         21154, 140.00),
('Nike',   'Nike KD17',           17738, 160.00),
('Nike',   'Nike Kobe 4 Protro',  19496, 190.00),
('Nike',   'Nike Kobe 8 Protro',  14922, 180.00),
('Adidas', 'adidas D.O.N. Issue 6',13428, 120.00);

