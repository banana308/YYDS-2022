import pytest
import allure

def test_passing():
    allure.dynamic.title(554564156456)
    with allure.step(11255664556):
        assert (1, 2, 3) == (1, 2, 3)
    print("测试成功日志")
