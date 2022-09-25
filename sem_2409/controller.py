import gui
import math_func
import db

def calc():
    value_a = gui.get_value()
    value_b = gui.get_value()
    act = gui.action()
    record = str(value_a) + ' ' + act + ' ' + str(value_b) + ' = '
    
    match act:
        case '+':
            result_sum = math_func.math_sum(value_a, value_b)
            gui.print_result(result_sum, "Сумма =")
            record += str(result_sum)
            db.writer(record)

        case '-':
            result_sub = math_func.math_sub(value_a, value_b)
            gui.print_result(result_sub, "Вычитание =")
            record += str(result_sub)
            db.writer(record)

        case '*':
            result_mult = math_func.math_mult(value_a, value_b)
            gui.print_result(result_mult, "Умножение =")
            record += str(result_mult)
            db.writer(record)
    
        case '/':
            result_div = math_func.math_div(value_a, value_b)
            gui.print_result(result_div, "Деление =")
            record += str(result_div)
            db.writer(record)