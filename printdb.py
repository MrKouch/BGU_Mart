from persistence import *

def main():
    # 1. printing the database
    print("Activities")
    repo.activities.print()
    print("Branches")
    repo.branches.print()
    print("Employees")
    repo.employees.print()
    print("Products")
    repo.products.print()
    print("Suppliers")
    repo.suppliers.print()

    # 2. employees report
    print("Employees report")
    employees_report = repo._conn.execute("""
        SELECT e.name, e.salary, b.location, IFNULL(SUM(a.quantity * p.price), 0) as total_sales_income
        FROM employees e
        JOIN branches b ON e.branche = b.id
        LEFT JOIN activities a ON e.id = a.activator_id AND a.quantity < 0
        LEFT JOIN products p ON a.product_id = p.id
        GROUP BY e.id
        ORDER BY e.name
    """).fetchall()
    for row in employees_report:
        print(" ".join(map(str, row)))

    # 3. activities report
    print("Activities report")
    activities_report = repo._conn.execute("""
        SELECT a.date, p.description, a.quantity,
               CASE WHEN a.quantity < 0 THEN e.name ELSE 'None' END as seller,
               CASE WHEN a.quantity > 0 THEN s.name ELSE 'None' END as supplier
        FROM activities a
        JOIN products p ON a.product_id = p.id
        LEFT JOIN employees e ON a.activator_id = e.id
        LEFT JOIN suppliers s ON a.activator_id = s.id
        ORDER BY a.date
    """).fetchall()
    for row in activities_report:
        print(" ".join(map(str, row)))

if __name__ == '__main__':
    main()