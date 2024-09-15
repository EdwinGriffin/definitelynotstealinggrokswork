class Student:
  def __init__(self, name, maths, english, science, history):
    self.name = name
    self.comment = ""
    # add instance variables to store the subjects

  def calculate_average(self):
    # Your code here
    pass

  def print_report(self):
    # Your code here
    pass

if __name__ == '__main__':
  students = [
    Student('Alice', 85, 92, 88, 95),
    Student('Bob', 70, 80, 75, 85),
    Student('Charlie', 90, 88, 92, 82),
    Student('Diana', 95, 90, 88, 92)
  ]
  for student in students:
    student.print_report()