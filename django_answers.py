#Question 1: 

def problem_two(request):
  student = Instructor.objects.filter(hire_date__lt = '2010-01-01').order_by('hire_date')
  for student in student:
      print(f'Full Name: {Instructor.first_name} {Instructor.last_name} Hire Date: {Instructor.hire_date}')
  
  
           
      return complete(request)
  
  

  #Question 2: 

  def problem_three(request):
    teacher = Instructor.objects.get(id=2)
    shared_course = Course.objects.filter(instructor_id='2')
    print(
              f' Instructor Name: {teacher}, Courses: {shared_course}')
    return complete(request)
  
  