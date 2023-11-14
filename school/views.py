from django.shortcuts import get_object_or_404, render, redirect
from .models import Student, Course

def students(request):
    students_list = Student.objects.all()
    return render(request, 'students.html', {'students': students_list})

def courses(request):
    courses_list = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses_list})

def details(request, student_id):
    student = Student.objects.get(id=student_id)
    available_courses = Course.objects.exclude(students=student)
    return render(request, 'details.html', {'student': student, 'available_courses': available_courses})

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        student = Student.objects.create(name=name)
        return redirect('students')
    return render(request, 'add_student.html')

def add_course(request):
    if request.method == 'POST':
        name = request.POST['name']
        course = Course.objects.create(name=name)
        return redirect('courses')
    return render(request, 'add_course.html')

def add_course_to_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        # Get the selected course from the form data
        course_id = request.POST.get('course')
        if course_id:
            course = get_object_or_404(Course, id=course_id)
            # Add the selected course to the student's courses
            student.courses.add(course)

    # Redirect back to the student details page after adding the course
    return redirect('details', student_id=student.id)
