# test_user.py
import pytest
from user import UserManager

@pytest.fixture
def user_manager():
    return UserManager()

def test_create_a_user(user_manager):
    user_id = user_manager.create_a_user("John", "pwd123", "student")
    assert user_id == None
    assert len(user_manager.user_list) == 1
    assert user_manager.user_list[0].name == "John"

def test_find_users(user_manager):
    user_manager.create_a_user("Alice", "pwd456", "teacher")
    found_users = user_manager.find_users([1])
    assert len(found_users) == 1
    assert found_users[0].name == "Alice"
