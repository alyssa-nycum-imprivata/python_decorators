class Queries:

    def sort_by_name(query_func):
        def additional_func(*args, **kwargs):
            original_func = query_func(*args, **kwargs)
            return original_func + " ORDER BY last_name ASC, first_name ASC"
        return additional_func

    @sort_by_name
    def customers(self):
        return "SELECT * FROM Customer"

    def coffins(self):
        return "SELECT * FROM Coffin"

    @sort_by_name
    def employees(self):
        return "SELECT * FROM Employee"

    def gravestones(self):
        return "SELECT * FROM GraveStones"

    @sort_by_name
    def deceased(self):
        return "SELECT * FROM Deceased"

    def obelisks(self):
        return "SELECT * FROM Obelisk"

    @sort_by_name
    def vendors(self):
        return "SELECT * FROM Vendor"