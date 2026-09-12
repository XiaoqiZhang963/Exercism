class School:
    def __init__(self):
        self.roster_dict = {}
        self.students = set()
        self.is_added = []

    def add_student(self, name, grade):
        if name in self.students:
            self.is_added.append(False)
        else:
            self.students.add(name)
            self.roster_dict.setdefault(grade,[]).append(name)
            self.is_added.append(True)

    def roster(self):
        return [
            student
            for grade in sorted(self.roster_dict)
            for student in sorted(self.roster_dict[grade])
        ]

    def grade(self, grade_number):
        return sorted(self.roster_dict.get(grade_number,[]))

    def added(self):
        return self.is_added
