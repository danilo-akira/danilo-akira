  
EXEC sp_rename 'olist_customers.["customer_id"]', 'customer_id', 'COLUMN'
EXEC sp_rename 'olist_customers.["customer_unique_id"]', 'customer_unique_id', 'COLUMN'
EXEC sp_rename 'olist_customers.["customer_zip_code_prefix"]', 'customer_zip_code_prefix', 'COLUMN'
EXEC sp_rename 'olist_customers.["customer_city"]', 'customer_city', 'COLUMN'
EXEC sp_rename 'olist_customers.["customer_state"]', 'customer_state', 'COLUMN'

EXEC sp_rename 'olist_geolocation.["geolocation_zip_code_prefix"]', 'geolocation_zip_code_prefix', 'COLUMN'
EXEC sp_rename 'olist_geolocation.["geolocation_lat"]', 'geolocation_lat', 'COLUMN'
EXEC sp_rename 'olist_geolocation.["geolocation_lng"]', 'geolocation_lng', 'COLUMN'
EXEC sp_rename 'olist_geolocation.["geolocation_city"]', 'geolocation_city', 'COLUMN'
EXEC sp_rename 'olist_geolocation.["geolocation_state"]', 'geolocation_state', 'COLUMN'

EXEC sp_rename 'olist_order_item.["order_item_id"]', 'order_item_id', 'COLUMN'
EXEC sp_rename 'olist_order_item.["order_id"]', 'order_id', 'COLUMN'
EXEC sp_rename 'olist_order_item.["product_id"]', 'product_id', 'COLUMN'
EXEC sp_rename 'olist_order_item.["seller_id"]', 'seller_id', 'COLUMN'
EXEC sp_rename 'olist_order_item.["shipping_limit_date"]', 'shipping_limit_date', 'COLUMN'
EXEC sp_rename 'olist_order_item.["price"]', 'price', 'COLUMN'
EXEC sp_rename 'olist_order_item.["freight_value"]', 'freight_value', 'COLUMN'

EXEC sp_rename 'olist_order_payments.["order_id"]', 'order_id', 'COLUMN'
EXEC sp_rename 'olist_order_payments.["payment_sequential"]', 'payment_sequential', 'COLUMN'
EXEC sp_rename 'olist_order_payments.["payment_type"]', 'payment_type', 'COLUMN'
EXEC sp_rename 'olist_order_payments.["payment_installments"]', 'payment_installments', 'COLUMN'
EXEC sp_rename 'olist_order_payments.["payment_value"]', 'payment_value', 'COLUMN'

EXEC sp_rename 'olist_orders.["customer_id"]', 'customer_id', 'COLUMN'
EXEC sp_rename 'olist_orders.["order_id"]', 'order_id', 'COLUMN'
EXEC sp_rename 'olist_orders.["order_status"]', 'order_status', 'COLUMN'
EXEC sp_rename 'olist_orders.["order_purchase_timestamp"]', 'order_purchase_timestamp', 'COLUMN'
EXEC sp_rename 'olist_orders.["order_approved_at"]', 'order_approved_at', 'COLUMN'
EXEC sp_rename 'olist_orders.["order_delivered_carrier_date"]', 'order_delivered_carrier_date', 'COLUMN'
EXEC sp_rename 'olist_orders.["order_delivered_customer_date"]', 'order_delivered_customer_date', 'COLUMN'
EXEC sp_rename 'olist_orders.["order_estimated_delivery_date"]', 'order_estimated_delivery_date', 'COLUMN'

EXEC sp_rename 'olist_products.["product_id"]', 'product_id', 'COLUMN'
EXEC sp_rename 'olist_products.["product_category_name"]', 'product_category_name', 'COLUMN'
EXEC sp_rename 'olist_products.["product_name_lenght"]', 'product_name_lenght', 'COLUMN'
EXEC sp_rename 'olist_products.["product_description_lenght"]', 'product_description_lenght', 'COLUMN'
EXEC sp_rename 'olist_products.["product_photos_qty"]', 'product_photos_qty', 'COLUMN'
EXEC sp_rename 'olist_products.["product_weight_g"]', 'product_weight_g', 'COLUMN'
EXEC sp_rename 'olist_products.["product_length_cm"]', 'product_length_cm', 'COLUMN'
EXEC sp_rename 'olist_products.["product_height_cm"]', 'product_height_cm', 'COLUMN'
EXEC sp_rename 'olist_products.["product_width_cm"]', 'product_width_cm', 'COLUMN'

EXEC sp_rename 'olist_sellers.["seller_id"]', 'seller_id', 'COLUMN'
EXEC sp_rename 'olist_sellers.["seller_zip_code_prefix"]', 'seller_zip_code_prefix', 'COLUMN'
EXEC sp_rename 'olist_sellers.["seller_city"]', 'seller_city', 'COLUMN'
EXEC sp_rename 'olist_sellers.["seller_state"]', 'seller_state', 'COLUMN'

alter table olist_order_payments alter column payment_value float null  
alter table olist_order_item alter column price float null
alter table olist_order_item alter column freight_value float null
alter table olist_order_item alter column shipping_limit_date date null
alter table olist_orders alter column order_purchase_timestamp date null
alter table olist_orders alter column order_approved_at date null
alter table olist_orders alter column order_delivered_carrier_date date null
alter table olist_orders alter column order_delivered_customer_date date null
alter table olist_orders alter column order_estimated_delivery_date date null

-- When occured the most and least recent order in the dataset?

SELECT min(order_purchase_timestamp) as least_recent, max(order_purchase_timestamp) as most_recent FROM olist_orders

	-- The dataset contains orders FROM 2016-09-04 to 2018-10-17
--------------------------------------------------------------------------------------------------------------------------------------------------

-- How many orders are in the dataset?

SELECT COUNT(order_id) FROM olist_order_item

	-- There are 112.650 orders in the dataset
--------------------------------------------------------------------------------------------------------------------------------------------------

-- Main statistics of order value

SELECT 
Min(payment_value) as Min,
Avg(payment_value) as Avg,
Max(payment_value) as Max
FROM olist_order_payments

SELECT top (1)
PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY payment_value) over() AS Q1,
PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY payment_value) over() AS Median,
PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY payment_value) over() AS Q3
FROM olist_order_payments

	-- Minimum = 0; Average = 154, Maximum = 13664
	-- 25th percentile = 56; Median = 100; 75th percentile = 171

--------------------------------------------------------------------------------------------------------------------------------------------------

-- WHERE are the customers FROM?

SELECT customer_city, COUNT (customer_city) as total_clients,  CONVERT(DECIMAL(18, 2), COUNT(*) * 100.0 / SUM(COUNT(*)) OVER ()) AS 'percentage'
FROM olist_customers
GROUP BY customer_city
ORDER BY total_clients desc

	-- Customers are all FROM Brazil, specially São Paulo city, which represents 15% of the total customers. 6.9% of the customers live in Rio de Janeiro and 2.8% live in Belo Horizonte
--------------------------------------------------------------------------------------------------------------------------------------------------

-- What are the most ordered product categories?

WITH query (order_id, product_id, product_category_name) as

(SELECT X.order_id, X.product_id, Y.product_category_name
FROM olist_order_item as X
inner join olist_products as Y
on X.product_id = Y.product_id)

SELECT product_category_name, COUNT(product_category_name) as 'number'
FROM query
GROUP BY product_category_name
ORDER BY 'number' desc

	-- The most ordered product category is bedding & bath, with 12% of the total orders, followed by health & beauty with 9% and sports with 8%. Furnitures represents 8% of the total and technology accessories, 6%.
	-- Other categories such as auto, perfumery, toys and fashion accessories represent a minor percentage of the total orders

--------------------------------------------------------------------------------------------------------------------------------------------------

-- When are people most likely to buy online?

SELECT DATEPART(month, shipping_limit_date) as Month, SUM(price) as total
FROM olist_order_item
GROUP BY DATEPART(month, shipping_limit_date)
ORDER BY total desc

	-- The top 3 months with the highest total orders value is August, May and March. The bottom 3 months are September, October and November. December, despite having Christimas, is positioned in 9th place.

--------------------------------------------------------------------------------------------------------------------------------------------------

	-- Which products are most sold in these months?

--August
WITH query(order_id, product_id, shipping_limit_date, product_category_name) as 

(SELECT X.order_id, X.product_id, X.shipping_limit_date, Y.product_category_name
FROM olist_order_item as X
inner join olist_products as Y
on X.product_id = Y.product_id
WHERE DATEPART(month, shipping_limit_date) = 8)

SELECT product_category_name, COUNT(product_category_name) as 'number'
FROM query
GROUP BY product_category_name
ORDER BY 'number' desc

--May
WITH query(order_id, product_id, shipping_limit_date, product_category_name) as 

(SELECT X.order_id, X.product_id, X.shipping_limit_date, Y.product_category_name
FROM olist_order_item as X
inner join olist_products as Y
on X.product_id = Y.product_id
WHERE DATEPART(month, shipping_limit_date) = 5)

SELECT product_category_name, COUNT(product_category_name) as 'number'
FROM query
GROUP BY product_category_name
ORDER BY 'number' desc

--March
WITH query(order_id, product_id, shipping_limit_date, product_category_name) as 

(SELECT X.order_id, X.product_id, X.shipping_limit_date, Y.product_category_name
FROM olist_order_item as X
inner join olist_products as Y
on X.product_id = Y.product_id
WHERE DATEPART(month, shipping_limit_date) = 3)

SELECT product_category_name, COUNT(product_category_name) as 'number'
FROM query
GROUP BY product_category_name
ORDER BY 'number' desc

	-- The queries of May and August show that the top product categories are the same: health & beauty, bedding & bath and housewares. There's not much difference between this podium and the year's podium that we saw before.
	-- The query of March brings technology accessories to the top of the list.
	-- Products that belong to these categories should have special attention in these months of the year.

--------------------------------------------------------------------------------------------------------------------------------------------------

-- What is the average delivery time for each month of the year and for each category? Does it have significant difference?

-- Average delivery time
SELECT (AVG(DATEDIFF(day, order_approved_at, order_delivered_customer_date))) as delivery_time
FROM olist_orders
WHERE DATEDIFF(day, order_approved_at, order_delivered_customer_date) between 0 and 1000

-- Average delivery time by month
SELECT  datepart(month, order_approved_at) as Month, (AVG(DATEDIFF(day, order_approved_at, order_delivered_customer_date))) as delivery_time
FROM olist_orders
WHERE DATEDIFF(day, order_approved_at, order_delivered_customer_date) between 0 and 1000
GROUP BY datepart(month, order_approved_at)
ORDER BY Month

-- Average delivery time by category
WITH 

query1(order_id, product_category_name) as

(SELECT X.order_id, Y.product_category_name
FROM olist_order_item as X
inner join olist_products as Y
on X.product_id = Y.product_id),

query2(product_category_name, delivery_time) as

(SELECT product_category_name, DATEDIFF(day, order_approved_at, order_delivered_customer_date)
FROM query1
join olist_orders
on query1.order_id = olist_orders.order_id)

SELECT product_category_name, AVG(delivery_time) as AVG_delivery_time
FROM query2
WHERE delivery_time between 0 and 1000
GROUP BY product_category_name
ORDER BY AVG_delivery_time desc

	-- The average delivery time is 11 days.
	-- Delivery time varies between 1 and 2 weeks throughout the months of the year. 
	-- Delivery time varies between 4 and 20 days depending on the product category. Bigger products such as furnitures and home appliances take longer to be delivered.
	
--------------------------------------------------------------------------------------------------------------------------------------------------

-- How often do orders delay?

-- Creating temporary table
create table query

(order_estimated_delivery_date date,
order_delivered_customer_date date,
delivery_time int)

insert into query
SELECT order_estimated_delivery_date, order_delivered_customer_date, DATEDIFF(day, order_estimated_delivery_date, order_delivered_customer_date)
FROM olist_orders
WHERE DATEDIFF(day, order_estimated_delivery_date, order_delivered_customer_date) between -1000 and 1000

-- Min, Avg and Max delivery time
SELECT MIN(delivery_time) as Min, AVG(delivery_time) as Avg, MAX(delivery_time) as Max
FROM query

--25th percentile (Q1), Median and 75th percentile (q3)
SELECT top (1)
PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY delivery_time) over() AS Q1,
PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY delivery_time) over() AS Median,
PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY delivery_time) over() AS Q3
FROM query

	-- Min = -147; Avg = -11; Max = 188
	-- 25th = -17; Median = -12; 75th = -7
	-- Orders are usually delivered before the estimated date. Some few cases reveal that the order was delivered months before or after the estimated date, which, in both cases, is not good

--------------------------------------------------------------------------------------------------------------------------------------------------

-- Let's try to understand why those orders were delivered with delay or in advance. We'll create a table that gathers information about delivery time, product category and seller and customer states.

with x(order_id, delivery_time, product_id, seller_id) as

(SELECT query.order_id, query.delivery_time, olist_order_item.product_id, olist_order_item.seller_id
FROM query
inner join olist_order_item
on query.order_id = olist_order_item.order_id
WHERE delivery_time > 90 or delivery_time < -90),

-- Adding product category name
y(order_id, delivery_time, product_id, seller_id, product_category_name) as
(SELECT x.order_id, x.delivery_time, x.product_id, x.seller_id, olist_products.product_category_name
FROM x
inner join olist_products
on x.product_id = olist_products.product_id),

-- Adding customer id to get customer state afterwards
z(order_id, delivery_time, product_id, seller_id, product_category_name, customer_id) as
(SELECT y.order_id, y.delivery_time, y.product_id, y.seller_id, y.product_category_name, olist_orders.customer_id
FROM y 
inner join olist_orders
on y.order_id = olist_orders.order_id),

-- Adding customer state
u(order_id, delivery_time, product_id, seller_id, product_category_name, customer_id, customer_state) as
(SELECT z.order_id, z.delivery_time, z.product_id, z.seller_id, z.product_category_name, z.customer_id, olist_customers.customer_state
FROM z
inner join olist_customers
on z.customer_id = olist_customers.customer_id),

-- Adding seller state
v(order_id, delivery_time, product_id, seller_id, product_category_name, customer_id, customer_state, seller_state) as
(SELECT u.order_id, u.delivery_time, u.product_id, u.seller_id, u.product_category_name, u.customer_id, u.customer_state, olist_sellers.seller_state
FROM u
inner join olist_sellers
on u.seller_id = olist_sellers.seller_id)

-- Final query
SELECT order_id, delivery_time, product_category_name, seller_state, customer_state FROM v
ORDER BY delivery_time

	-- The final query shows that late delivered orders usually travel through states in Brazil. Most of them have sellers located, but the customers live in other states.
	-- It's not accurate to say that this is the main and/or only reason for delays, but maybe it is something to be aware of. 
	-- There is not a product category that draws attention when speaking of orders that were delivered with considerable delay.
	-- About orders that were delivered months before the estimated delivery date, there's no clear signal of a common factor between them. 
	-- 3 of them were furniture items, so maybe the estimated delivery dates were more flexible to consider supply issues. It's not a bad thing but perhaps the estimates could be more precise.