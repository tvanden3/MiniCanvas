# test_course.py
import pytest
from course import CourseManager, Course
from unittest.mock import MagicMock

@pytest.fixture
def course_manager():
    return CourseManager()

def test_create_a_course(course_manager):
    course_manager.create_a_course("CS101", "Fall 2023", ["Alice", "Bob"])
    assert len(course_manager.course_list) == 1
    assert course_manager.course_list[0].course_code == "CS101"

def test_find_a_course(course_manager):
    course_id = course_manager.create_a_course("CS101", "Fall 2023", ["Alice", "Bob"])
    course = course_manager.find_a_course(course_id)
    assert course.course_code == "CS101"

def test_generate_id(course_manager):
    assert course_manager.generate_id() == 1
    assert course_manager.generate_id() == 2
