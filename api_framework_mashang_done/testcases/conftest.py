import pytest
from commons.yaml_util import clear_yaml

#在每次执行之前清空extract.yaml文件
@pytest.fixture(scope="session",autouse=True)
def clear_extract():
    clear_yaml()