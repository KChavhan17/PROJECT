def calculate_hra(basic):
    return 0.40 * basic

def calculate_net_salary(basic):
    hra = calculate_hra(basic)
    da = 0.10 * basic
    deductions = 0.05 * basic
    return basic + hra + da - deductions