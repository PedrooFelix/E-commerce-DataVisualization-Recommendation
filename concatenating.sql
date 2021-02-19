
SELECT 
	product_category_name as Categoria,
	d.customer_state as Estado,
	count(*) as Vendas
FROM olist_products_dataset A 
INNER JOIN olist_order_items_dataset B ON A.product_id = B.product_id
INNER JOIN olist_orders_dataset C ON B.order_id = C.order_id
INNER JOIN olist_customers_dataset D ON c.customer_id = D.customer_id
group by product_category_name,d.customer_state 
order by count(*) DESC


select 
	a.*, 
	b.vendas as Vendas 
	from datageo A inner join (SELECT 
	product_category_name as Categoria,
	d.customer_state as Estado,
	count(*) as Vendas
FROM olist_products_dataset A 
INNER JOIN olist_order_items_dataset B ON A.product_id = B.product_id
INNER JOIN olist_orders_dataset C ON B.order_id = C.order_id
INNER JOIN olist_customers_dataset D ON c.customer_id = D.customer_id
group by product_category_name,d.customer_state 
order by count(*) DESC) B on A.product_category_name
= B.categoria and A."ST" = B.estado

select * from datageo
SELECT product_category_name, count(*) FROM olist_products_dataset A INNER JOIN olist_order_items_dataset B ON 
A.product_id = B.product_id group by product_category_name order by count(*) DESC