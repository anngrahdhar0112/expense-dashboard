-- SECTION A

-- 1. List total sales for each product category. Sort highest to lowest.
SELECT "Category",
       SUM("Sales") AS sales_of_each_product
FROM dashboard.sales_raw
GROUP BY "Category"
ORDER BY sales_of_each_product DESC;

-- 2. Find total profit made in each region.
SELECT "Region", SUM("Profit") as Region_Wise_Profit
from dashboard.sales_raw
group by "Region";

-- 3. Which 5 cities generated the highest total sales?
select "City", SUM("Sales") as City_Wise_Sales
from dashboard.sales_raw
group by "City"
Order by City_Wise_Sales desc
LIMIT 5;

-- 4. What is the average discount given for each customer segment?
select "Segment", avg("Discount") as Avg_Disc_to_Each_Segment
from dashboard.sales_raw
group by "Segment";


-- 5. Find the total number of unique customers in each region.
select "Region", count(distinct("Customer ID")) as Unique_Customers 
from dashboard.sales_raw
group by "Region";

-- 6. Calculate the total sales and total quantity for the category ‘Furniture’.
SELECT "Category", sum("Sales") as Total_Sales, sum("Quantity") as Total_Quantity
from dashboard.sales_raw
where "Category" = 'Furniture'
group by "Category";

-- 7. Show monthly total sales (month-by-month) across the entire dataset.
select EXTRACT(MONTH FROM "Ship Date") as Month_value, sum("Sales") as Monthly_Sales
from dashboard.sales_raw
group by Month_value
order by Month_value;

-- 8. Find the top 10 most profitable products.
select "Product Name", sum("Profit") as Total_Profit
from dashboard.sales_raw
group by "Product Name"
order by Total_Profit DESC 
LIMIT 10;

-- 9. Which sub-category has the highest average sales per order?
select "Order ID", "Sub-Category", sum(select avg("Sales") from dashboard.sales_raw)
from dashboard.sales_raw
group by "Sub-Category", "Order ID";

-- 10. For each state, calculate the total number of orders.
select "State", count("Order ID")
from dashboard.sales_raw
group by "State";