# pylint:disable=C0111,C0103
import sqlite3
conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()
def order_rank_per_customer(db):
    query = '''SELECT
    Orders.OrderID,
    Orders.CustomerID,
    Orders.OrderDate,
    RANK() OVER (PARTITION BY Orders.CustomerID ORDER BY Orders.OrderDate) AS OrderRank
    FROM Orders; '''
    db.execute(query)
    results = db.fetchall()
    return results
    # YOUR CODE HERE


def order_cumulative_amount_per_customer(db):
    query = '''SELECT DISTINCT
    Orders.OrderID, Orders.CustomerID, Orders.OrderDate,
    SUM(UnitPrice*Quantity) OVER (PARTITION BY Orders.CustomerID ORDER BY Orders.OrderDate) AS Order_cum_amount
    FROM Orders
    JOIN OrderDetails
    ON Orders.OrderID = OrderDetails.OrderID; '''
    db.execute(query)
    results = db.fetchall()
    return results
