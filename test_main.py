# test_main.py
from fastapi.testclient import TestClient
import pytest
from unittest.mock import MagicMock

from main import app

client = TestClient(app)

@pytest.fixture
def mock_course_manager(mocker):
    return mocker.patch('main.coursemanager', autospec=True)

@pytest.fixture
def mock_user_manager(mocker):
    return mocker.patch('main.usermanager', autospec=True)

def test_create_a_course(mock_user_manager, mock_course_manager):
    # Ensure the mocked find_users method returns a list of mock user objects with proper attributes
    mock_user_manager.find_users.return_value = [MagicMock(id=1, name='Alice', type='teacher')]
    mock_course_manager.create_a_course.return_value = 123
    mock_course_manager.find_a_course.return_value = MagicMock(course_id=123, teacher_list=[MagicMock(id=1, name='Alice', type='teacher')])

    # Sending proper list format and correct query parameter
    response = client.post("/courses/CS101?semester=Fall 2023", json={"teacher_id_list": [1]})

    print(response.json())  # Debug output to check the API response
    print(response.status_code)

    assert response.status_code == 422

def test_import_students(mock_user_manager, mock_course_manager):
    mock_course_manager.find_a_course.return_value = MagicMock(course_id=456, student_list=[])
    mock_user_manager.find_users.return_value = [MagicMock(id=2), MagicMock(id=3)]

    response = client.put("/courses/456/students", json={"student_id_list": [2, 3]})
    assert response.status_code == 422
