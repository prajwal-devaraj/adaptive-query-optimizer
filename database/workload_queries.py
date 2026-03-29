QUERIES = [
    "SELECT COUNT(*) FROM orders WHERE order_date >= '2025-01-01';",
    "SELECT category, AVG(price) FROM products GROUP BY category;",
    "SELECT c.segment, COUNT(o.order_id) FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.segment;",
    "SELECT p.category, SUM(oi.quantity * oi.unit_price) AS revenue FROM order_items oi JOIN products p ON oi.product_id = p.product_id GROUP BY p.category ORDER BY revenue DESC;",
    "SELECT w.city, AVG(s.delivery_days) FROM shipments s JOIN warehouses w ON s.warehouse_id = w.warehouse_id GROUP BY w.city;",
    "SELECT c.state, COUNT(r.review_id) FROM reviews r JOIN customers c ON r.customer_id = c.customer_id GROUP BY c.state ORDER BY COUNT(r.review_id) DESC;",
    "SELECT p.category, AVG(r.rating) FROM reviews r JOIN products p ON r.product_id = p.product_id GROUP BY p.category;",
    "SELECT o.order_status, AVG(o.total_amount) FROM orders o GROUP BY o.order_status;",
    "SELECT c.city, SUM(o.total_amount) FROM customers c JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.city ORDER BY SUM(o.total_amount) DESC LIMIT 20;",
    "SELECT p.product_name, SUM(oi.quantity) AS qty_sold FROM order_items oi JOIN products p ON oi.product_id = p.product_id GROUP BY p.product_name ORDER BY qty_sold DESC LIMIT 10;"
]