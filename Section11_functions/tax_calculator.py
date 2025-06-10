
def tax_calculator(subtotal, sales_tax=0.06):
    """takes in a subtotal and tax rate and returns total owed
    
    Args:
        subtotal (float): cost of items in transaction
        tax_rate (float): tax rate at store location
        
    Returns:
        float: total amount owed on transaction
    """
    tax = round((subtotal * sales_tax), 2)
    total = round((subtotal + tax), 2)
    return [total, tax, subtotal]
