select a.*, b.count as Vendas from datageo A inner join (
SELECT product_category_name, count(*) FROM olist_products_dataset A INNER JOIN olist_order_items_dataset B ON 
A.product_id = B.product_id group by product_category_name order by count(*) DESC ) B on A.product_category_name
= B.product_category_name