# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import example as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -2978
    module_0.build_chain(int_0, int_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.build_chain(none_type_0, none_type_0)
    var_1 = module_0.build_chain(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 1774.36
    dict_0 = {float_0: float_0}
    module_0.can_chain(dict_0)


def test_case_3():
    none_type_0 = None
    var_0 = module_0.swap(none_type_0, none_type_0)
    var_1 = module_0.can_chain(var_0)
    var_2 = module_0.build_chain(none_type_0, var_0)


def test_case_4():
    object_0 = module_1.object()
    set_0 = {object_0, object_0, object_0}
    var_0 = module_0.swap(set_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = ",V5BY4MqY)H+!|a_"
    module_0.can_chain(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    none_type_0 = None
    var_0 = module_0.swap(none_type_0, none_type_0)
    module_0.build_chain(var_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bytes_0 = b"\xd0\xc6\xe4\xcf\xf0\xbf\xc6\xd6\xb03Y-\xa5\xc6\x1f-\x13$"
    tuple_0 = (bytes_0,)
    var_0 = module_0.can_chain(tuple_0)
    var_1 = module_0.swap(var_0, var_0)
    none_type_0 = None
    module_0.can_chain(none_type_0)


def test_case_8():
    bool_0 = True
    var_0 = module_0.swap(bool_0, bool_0)
    var_1 = module_0.swap(var_0, var_0)
    var_2 = module_0.swap(var_0, var_0)
    none_type_0 = None
    var_3 = module_0.swap(var_2, none_type_0)
    var_4 = module_0.can_chain(var_2)
    str_0 = ",V5BY4MqY)H+!|a_"
    int_0 = -733
    var_5 = module_0.build_chain(var_1, var_2)
    set_0 = {str_0}
    dict_0 = {str_0: int_0, int_0: set_0}
    var_6 = module_0.swap(dict_0, dict_0)


def test_case_9():
    bool_0 = True
    str_0 = ":orY.gPEh"
    set_0 = {str_0}
    tuple_0 = (bool_0, bool_0, str_0, set_0)
    tuple_1 = (bool_0, str_0, bool_0, tuple_0)
    var_0 = module_0.swap(tuple_1, tuple_0)
    var_1 = module_0.build_chain(var_0, str_0)
    dict_0 = {}
    object_0 = module_1.object(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    bool_0 = True
    var_0 = module_0.swap(bool_0, bool_0)
    set_0 = {var_0}
    var_1 = module_0.can_chain(set_0)
    var_2 = module_0.swap(var_0, set_0)
    var_3 = module_0.can_chain(var_1)
    module_0.build_chain(var_2, var_3)


@pytest.mark.xfail(strict=True)
def test_case_11():
    str_0 = '<yv3{$aH|V@S"98a'
    var_0 = module_0.swap(str_0, str_0)
    module_0.build_chain(var_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    none_type_0 = None
    var_0 = module_0.swap(none_type_0, none_type_0)
    set_0 = set()
    var_1 = module_0.can_chain(set_0)
    var_2 = module_0.swap(var_0, set_0)
    module_0.build_chain(var_2, var_0)


def test_case_13():
    bool_0 = True
    var_0 = module_0.swap(bool_0, bool_0)
    var_1 = module_0.swap(var_0, var_0)
    tuple_0 = (var_0, var_0, var_1)
    var_2 = module_0.can_chain(tuple_0)
    var_3 = module_0.swap(var_0, var_0)
    none_type_0 = None
    var_4 = module_0.swap(var_3, none_type_0)
    var_5 = module_0.can_chain(var_3)
    str_0 = ",V5BY4MqY)H+!|a_"
    int_0 = -733
    var_6 = module_0.build_chain(var_1, var_3)
    set_0 = {str_0}
    dict_0 = {str_0: int_0, int_0: set_0}
    var_7 = module_0.swap(dict_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_14():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.swap(bool_0, bool_0)
    bytes_0 = b"\x94\x01\x0c\x1a"
    var_1 = module_0.swap(bool_0, none_type_0)
    var_2 = module_0.swap(var_0, bytes_0)
    var_3 = module_0.swap(bool_0, bool_0)
    str_0 = "`E"
    list_0 = [var_3, str_0, var_3, str_0]
    tuple_0 = (str_0, var_3, list_0, var_3)
    var_4 = module_0.can_chain(tuple_0)
    var_5 = module_0.swap(var_3, var_3)
    var_6 = module_0.swap(var_2, var_5)
    var_7 = module_0.can_chain(var_6)
    var_8 = module_0.build_chain(none_type_0, var_4)
    var_9 = module_0.swap(tuple_0, var_2)
    var_10 = module_0.swap(var_3, var_3)
    none_type_1 = None
    var_11 = module_0.swap(var_10, none_type_1)
    var_12 = module_0.can_chain(var_10)
    var_13 = module_0.can_chain(var_5)
    module_0.can_chain(bool_0)
