--- 1. Create the database
CREATE DATABASE IF NOT EXISTS RetailDB;

-- 2. Use the database
USE RetailDB;

-- 3. Create the Sales table
CREATE TABLE IF NOT EXISTS Sales (
    SaleID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    Product TEXT,
    Quantity INTEGER,
    Price REAL,
    SaleDate DATE
);

-- 4. Insert dummy sales data
INSERT INTO Sales (SaleID, CustomerID, Product, Quantity, Price, SaleDate) VALUES
(1, 101, 'Laptop', 1, 1000.00, '2025-01-10'),
(2, 102, 'Headphones', 2, 150.00, '2025-01-15'),
(3, 103, 'Mouse', 3, 25.00, '2025-02-05'),
(4, 101, 'Laptop', 1, 950.00, '2025-02-20'),
(5, 104, 'Keyboard', 2, 75.00, '2025-03-08'),
(6, 102, 'Monitor', 1, 300.00, '2025-03-12'),
(7, 105, 'Mouse', 4, 25.00, '2025-04-01'),
(8, 106, 'Keyboard', 1, 70.00, '2025-04-10'),
(9, 107, 'Laptop', 2, 980.00, '2025-05-03'),
(10, 108, 'Headphones', 1, 145.00, '2025-05-18'),
(11, 109, 'Monitor', 2, 290.00, '2025-06-05'),
(12, 110, 'Mouse', 5, 30.00, '2025-06-22'),
(13, 101, 'Keyboard', 3, 75.00, '2025-07-10'),
(14, 102, 'Laptop', 1, 990.00, '2025-07-22'),
(15, 103, 'Monitor', 1, 310.00, '2025-08-14'),
(16, 104, 'Headphones', 2, 160.00, '2025-08-29'),
(17, 105, 'Mouse', 3, 30.00, '2025-09-06'),
(18, 106, 'Monitor', 1, 320.00, '2025-09-21'),
(19, 107, 'Laptop', 1, 1000.00, '2025-10-03'),
(20, 108, 'Keyboard', 2, 80.00, '2025-10-19');



-- 1. Total revenue (Quantity × Price) for each product
SELECT Product, SUM(Quantity * Price) AS TotalRevenue
FROM Sales
GROUP BY Product;

-- 2. Top 3 customers who spent the most
SELECT CustomerID, SUM(Quantity * Price) AS TotalSpent
FROM Sales
GROUP BY CustomerID
ORDER BY TotalSpent DESC
LIMIT 3;

-- 3. Monthly sales totals for 2025
SELECT 
    DATE_FORMAT(SaleDate, '%Y-%m') AS Month,
    SUM(Quantity * Price) AS MonthlyTotal
FROM Sales
WHERE YEAR(SaleDate) = 2024
GROUP BY Month
ORDER BY Month;


-- 4. Product with the highest number of sales (by quantity)
SELECT Product, SUM(Quantity) AS TotalQuantity
FROM Sales
GROUP BY Product
ORDER BY TotalQuantity DESC
LIMIT 1;
