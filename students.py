lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

class_list = [lloyd, alice, tyler]
# Add your function below!
def average(numbers):
 
  total = sum(numbers)
  total = float(total)
  average = total/len(numbers)
  return average

def get_average(student):
  homework = average(student["homework"])
  quiz = average(student["quizzes"])
  test = average(student["tests"])
  homework = homework * 1/10
  quiz = quiz* 3/10
  test = test * 6/10
  grade = homework + quiz + test
  return grade
def get_letter_grade(score):
 
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
  	return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
  return letter_grade  

print "Lloyd got a " + get_letter_grade(get_average(lloyd))
 
def get_class_average(class_list):
  results = []
  for student in class_list:
    avg = get_average(student)
    results.append(avg)
  return average(results)  
    
