# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import either as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    none_type_1 = None
    right_0 = module_0.Right(none_type_0)
    assert f"{type(right_0).__module__}.{type(right_0).__qualname__}" == "either.Right"
    assert right_0.value is None
    bool_0 = right_0.__eq__(none_type_1)
    assert bool_0 is False
    right_0.to_try()


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    none_type_1 = None
    right_0 = module_0.Right(none_type_1)
    assert f"{type(right_0).__module__}.{type(right_0).__qualname__}" == "either.Right"
    assert right_0.value is None
    right_0.case(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    left_0 = module_0.Left(bool_0)
    assert f"{type(left_0).__module__}.{type(left_0).__qualname__}" == "either.Left"
    assert left_0.value is True
    str_0 = "3:od0:g)eqM[Xy\x0cc\x0b"
    str_1 = "\\"
    left_1 = module_0.Left(str_1)
    left_1.case(left_0, str_0)


def test_case_3():
    float_0 = -63.05
    right_0 = module_0.Right(float_0)
    assert f"{type(right_0).__module__}.{type(right_0).__qualname__}" == "either.Right"
    assert right_0.value == pytest.approx(-63.05, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_4():
    none_type_0 = None
    none_type_1 = None
    either_0 = module_0.Either(none_type_1)
    assert (
        f"{type(either_0).__module__}.{type(either_0).__qualname__}" == "either.Either"
    )
    assert either_0.value is None
    either_0.ap(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = -3768
    left_0 = module_0.Left(int_0)
    assert f"{type(left_0).__module__}.{type(left_0).__qualname__}" == "either.Left"
    assert left_0.value == -3768
    left_0.to_box()


@pytest.mark.xfail(strict=True)
def test_case_6():
    int_0 = 532
    left_0 = module_0.Left(int_0)
    assert f"{type(left_0).__module__}.{type(left_0).__qualname__}" == "either.Left"
    assert left_0.value == 532
    left_0.to_try()


@pytest.mark.xfail(strict=True)
def test_case_7():
    none_type_0 = None
    left_0 = module_0.Left(none_type_0)
    assert f"{type(left_0).__module__}.{type(left_0).__qualname__}" == "either.Left"
    assert left_0.value is None
    left_0.to_lazy()


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "N#)\x0crr"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    either_0 = module_0.Either(dict_0)
    assert (
        f"{type(either_0).__module__}.{type(either_0).__qualname__}" == "either.Either"
    )
    assert either_0.value == {"N#)\x0crr": "N#)\x0crr"}
    var_0 = either_0.is_right()
    var_0.to_validation()


def test_case_9():
    str_0 = "|@W!#2(\r*@CWOQ\\A\\"
    none_type_0 = None
    left_0 = module_0.Left(none_type_0)
    assert f"{type(left_0).__module__}.{type(left_0).__qualname__}" == "either.Left"
    assert left_0.value is None
    left_1 = left_0.bind(str_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    list_0 = []
    left_0 = module_0.Left(list_0)
    assert f"{type(left_0).__module__}.{type(left_0).__qualname__}" == "either.Left"
    assert left_0.value == []
    var_0 = left_0.ap(list_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "either.Left"
    assert var_0.value == []
    bool_0 = var_0.is_left()
    right_0 = module_0.Right(list_0)
    right_1 = module_0.Right(list_0)
    right_0.to_maybe()


def test_case_11():
    none_type_0 = None
    left_0 = module_0.Left(none_type_0)
    assert f"{type(left_0).__module__}.{type(left_0).__qualname__}" == "either.Left"
    assert left_0.value is None
    bool_0 = left_0.is_left()


@pytest.mark.xfail(strict=True)
def test_case_12():
    none_type_0 = None
    list_0 = [none_type_0]
    bool_0 = True
    left_0 = module_0.Left(list_0)
    assert f"{type(left_0).__module__}.{type(left_0).__qualname__}" == "either.Left"
    assert left_0.value == [None]
    var_0 = left_0.ap(none_type_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "either.Left"
    assert var_0.value == [None]
    var_1 = var_0.bind(bool_0)
    var_1.to_maybe()


@pytest.mark.xfail(strict=True)
def test_case_13():
    none_type_0 = None
    none_type_1 = None
    left_0 = module_0.Left(none_type_1)
    assert f"{type(left_0).__module__}.{type(left_0).__qualname__}" == "either.Left"
    assert left_0.value is None
    right_0 = module_0.Right(none_type_0)
    bool_0 = left_0.is_left()
    left_1 = module_0.Left(right_0)
    bool_1 = left_1.__eq__(right_0)
    assert bool_1 is False
    left_0.to_validation()


@pytest.mark.xfail(strict=True)
def test_case_14():
    none_type_0 = None
    right_0 = module_0.Right(none_type_0)
    assert f"{type(right_0).__module__}.{type(right_0).__qualname__}" == "either.Right"
    assert right_0.value is None
    bool_0 = right_0.__eq__(none_type_0)
    assert bool_0 is False
    right_0.map(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_15():
    none_type_0 = None
    none_type_1 = None
    right_0 = module_0.Right(none_type_1)
    assert f"{type(right_0).__module__}.{type(right_0).__qualname__}" == "either.Right"
    assert right_0.value is None
    right_0.bind(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_16():
    int_0 = -2944
    right_0 = module_0.Right(int_0)
    assert f"{type(right_0).__module__}.{type(right_0).__qualname__}" == "either.Right"
    assert right_0.value == -2944
    bool_0 = right_0.is_left()
    right_0.to_validation()


@pytest.mark.xfail(strict=True)
def test_case_17():
    float_0 = 519.206
    right_0 = module_0.Right(float_0)
    assert f"{type(right_0).__module__}.{type(right_0).__qualname__}" == "either.Right"
    assert right_0.value == pytest.approx(519.206, abs=0.01, rel=0.01)
    right_0.to_maybe()


@pytest.mark.xfail(strict=True)
def test_case_18():
    int_0 = -217
    right_0 = module_0.Right(int_0)
    assert f"{type(right_0).__module__}.{type(right_0).__qualname__}" == "either.Right"
    assert right_0.value == -217
    right_0.to_validation()


@pytest.mark.xfail(strict=True)
def test_case_19():
    bool_0 = True
    left_0 = module_0.Left(bool_0)
    assert f"{type(left_0).__module__}.{type(left_0).__qualname__}" == "either.Left"
    assert left_0.value is True
    var_0 = left_0.ap(left_0)
    left_1 = left_0.map(var_0)
    left_0.to_maybe()


@pytest.mark.xfail(strict=True)
def test_case_20():
    float_0 = -2472.4
    right_0 = module_0.Right(float_0)
    assert f"{type(right_0).__module__}.{type(right_0).__qualname__}" == "either.Right"
    assert right_0.value == pytest.approx(-2472.4, abs=0.01, rel=0.01)
    bool_0 = right_0.is_right()
    assert bool_0 is True
    right_1 = module_0.Right(float_0)
    left_0 = module_0.Left(float_0)
    bool_1 = right_0.__eq__(right_0)
    assert bool_1 is True
    right_0.to_box()
