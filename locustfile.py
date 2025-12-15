import random
import time
from locust import HttpUser, TaskSet, task, between

class GradebookTasks(TaskSet):
    
    @task(1)
    def add_student(self):
        """Add a student with POST request"""
        students_names = ["John Smith", "Jane Doe", "Bob Johnson", "Alice Williams", "Charlie Brown"]
        subjects = ["Math", "English", "Science", "History", "Physics"]
        
        name = random.choice(students_names)
        subject = random.choice(subjects)
        grade = random.randint(60, 100)
        
        self.client.post("/add", data={
            "name": name,
            "subject": subject,
            "grade": str(grade)
        })
    
    @task(2)
    def load_homepage(self):
        """Load homepage with GET request"""
        self.client.get("/")
    
    @task(1)
    def get_api_students(self):
        """Call API endpoint to get all students"""
        self.client.get("/api/students")


class GradebookUser(HttpUser):
    """Load testing user that runs tasks sequentially"""
    tasks = [GradebookTasks]
    wait_time = between(2, 4)  # Wait 2-4 seconds between tasks
    
    def on_start(self):
        """Called when a user starts"""
        pass
