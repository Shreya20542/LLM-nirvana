# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import example as module_0


def test_case_0():
    bytes_0 = b""
    var_0 = module_0.dig_perms(bytes_0, bytes_0, bytes_0)


def test_case_1():
    str_0 = "=XSw;^+dk:}w\x0b"
    var_0 = module_0.solve(str_0)


def test_case_2():
    str_0 = "=XSw^+dk:}w\x0b"
    var_0 = module_0.solve(str_0)


def test_case_3():
    tuple_0 = ()
    str_0 = "`,~5~0PXqRoCqs)/_:M"
    set_0 = {tuple_0, str_0, str_0}
    var_0 = module_0.dig_perms(set_0, str_0, set_0)
    str_1 = "sqSw;^+dk\\_w\x0b"
    var_1 = module_0.solve(str_1)


def test_case_4():
    str_0 = "=XSw^+dk:w7"
    var_0 = module_0.solve(str_0)
