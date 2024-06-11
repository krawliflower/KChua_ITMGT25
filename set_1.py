import math 

def savings(gross_pay,tax_rate,expenses):
    after_tax_pay = math.floor(gross_pay - gross_pay*tax_rate)
    pay = after_tax_pay - expenses
    return pay

def  material_waste(total_material, material_units, num_jobs, job_consumption):
    consume = num_jobs*job_consumption
    waste = total_material - consume
    total = str(waste) + material_units
    return total

def interest(principal, rate, periods):
    final = math.floor(principal + principal*(rate*periods))
    return final