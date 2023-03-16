#Question 1: 

def problem_two(request):
  student = Instructor.objects.filter(hire_date__lt = '2010-01-01').order_by('hire_date')
  for student in student:
      print(f'Full Name: {Instructor.first_name} {Instructor.last_name} Hire Date: {Instructor.hire_date}')
  
  
           
      return complete(request)
  
  

#Question 2: 
def problem_two(request):
  student = Instructor.objects.filter(hire_date__lt = '2010-01-01').order_by('hire_date')
  for student in student:
      print(f'Full Name: {Instructor.first_name} {Instructor.last_name} Hire Date: {Instructor.hire_date}')
  
  
           
      return complete(request)







#Quesion 3:

  def problem_three(request):
    teacher = Instructor.objects.get(id=2)
    shared_course = Course.objects.filter(instructor_id='2')
    print(
              f' Instructor Name: {teacher}, Courses: {shared_course}')
    return complete(request)
  

  #Question 4:

  def problem_four(request):
  kids = Student.objects.count()
  classes = Course.objects.count()
  professors = Instructor.objects.count()

  print(kids, classes, professors)
  return complete(request)

#Question 5: 

def problem_five(request):
    new_student = Student.objects.create(Student.first_name("Cornelius"),Student.last_name("Phillips"), Student.year("2023", Student.gpa("4.0")) )
    return complete(request)

#Question 6:

def problem_six(request):
    new_update = Student.objects.get(pk=11).update(Student.gpa("4.2"))
    new_student = Student.objects.get(pk=11)
    print(new_student)
    # Make sure to set this equal to the primary key of the row you just created!
    student_id = 11

    return complete(request)

