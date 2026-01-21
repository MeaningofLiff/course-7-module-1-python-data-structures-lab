# lib/data_generator.py

def students_by_id(students):
    """Return a dict mapping student_id -> (name, major)."""
    return {sid: (name, major) for sid, name, major in students}
 