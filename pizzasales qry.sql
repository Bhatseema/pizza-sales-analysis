select * from pizza_sales

SELECT SUM(total_price) AS total_revenue
FROM pizza_sales;

SELECT SUM(total_price) / COUNT(DISTINCT order_id) AS avg_order_value
FROM pizza_sales;


SELECT SUM(quantity) AS total_pizzas_sold
FROM pizza_sales;

SELECT COUNT(DISTINCT order_id) AS total_orders
FROM pizza_sales;

SELECT SUM(quantity) / COUNT(DISTINCT order_id) AS avg_pizzas_per_order
FROM pizza_sales;


SELECT 
    DATENAME(WEEKDAY, order_date) AS day_name,
    COUNT(DISTINCT order_id) AS total_orders
FROM pizza_sales
GROUP BY DATENAME(WEEKDAY, order_date)
ORDER BY total_orders DESC;

SELECT 
    MONTH(order_date) AS month_no,
    DATENAME(MONTH, order_date) AS month_name,
    COUNT(DISTINCT order_id) AS total_orders
FROM pizza_sales
GROUP BY 
    MONTH(order_date),
    DATENAME(MONTH, order_date)
ORDER BY total_orders DESC;



SELECT 
    pizza_category,
    SUM(total_price) AS category_revenue,
    ROUND(
        SUM(total_price) * 100.0 / (SELECT SUM(total_price) FROM pizza_sales),
        2
    ) AS percentage_sales
FROM pizza_sales
GROUP BY pizza_category
ORDER BY percentage_sales DESC;

SELECT 
    pizza_size,
    SUM(total_price) AS size_revenue,
    ROUND(
        SUM(total_price) * 100.0 / (SELECT SUM(total_price) FROM pizza_sales),
        2
    ) AS percentage_sales
FROM pizza_sales
GROUP BY pizza_size
ORDER BY percentage_sales DESC;

SELECT 
    pizza_category,
    SUM(quantity) AS total_pizzas_sold
FROM pizza_sales
GROUP BY pizza_category
ORDER BY total_pizzas_sold DESC;

SELECT TOP 5
    pizza_name,
    SUM(total_price) AS total_revenue,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT order_id) AS total_orders
FROM pizza_sales
GROUP BY pizza_name
ORDER BY total_revenue DESC;

SELECT TOP 5
    pizza_name,
    SUM(total_price) AS total_revenue,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT order_id) AS total_orders
FROM pizza_sales
GROUP BY pizza_name
ORDER BY total_revenue ASC;