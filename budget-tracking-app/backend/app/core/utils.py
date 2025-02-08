def generate_uuid():
    import uuid
    return str(uuid.uuid4())

def format_currency(amount):
    return "${:,.2f}".format(amount)

def validate_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def calculate_remaining_budget(total_budget, expenses):
    return total_budget - sum(expenses)