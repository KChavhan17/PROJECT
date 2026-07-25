class Employee:
    def display_info(self):
        print(f"[{self.emp_id}] {self.name} - {self.department}")

class Manager(Employee):
    def display_info(self):
        # Overriding display_info to include team size
        print(f"[{self.emp_id}] {self.name} - {self.department} (Team Size: {self.team_size})")

# Create Manager object
mgr = Manager()
mgr.emp_id = "MGR201"
mgr.name = "Rihan Kani"
mgr.department = "Engineering"
mgr.team_size = 12

# Call display_info
mgr.display_info()