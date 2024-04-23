# test_assignment.py
import pytest
from datetime import datetime
from assignment import Assignment, Submission

def test_assignment_initialization():
    assignment = Assignment(assignment_id=1, due_date=datetime.now(), course_id=101)
    assert assignment.assignment_id == 1

def test_submit_assignment():
    assignment = Assignment(assignment_id=1, due_date=datetime.now(), course_id=101)
    submission = Submission(student_id=123, content="My assignment")
    assignment.submit(submission)
    assert len(assignment.submission_list) == 1
    assert assignment.submission_list[0].student_id == 123
