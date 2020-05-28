from schedule import Schedule
from course import CourseType, Course, Section
class Individual:
    def __init__(self, tag: int):
        self.tag = tag
        self.schedule = Schedule(tag)
        self.reqOffPeriods = 1
    
    def changeReqOff(self, newReq: int):
        self.reqOffPeriods = newReq
    
    def getReqOff(self) -> int:
        return self.reqOffPeriods
    
    def addSection(self, newSection: Section):
        self.schedule.addSection(newSection)
    
    def removeSection(self, section: Section):
        self.schedule.removeSection(section)
    
    def getSections(self):
        return self.schedule.getSections()
    
    def offDelta(self):
        """
        Positive when more scheduled off than required, negative when fewer scheduled off than required
        """
        return (len(self.schedule.getOpenPeriods()) - self.reqOffPeriods)
    
    def hasPotentialLunchSlot(self, lunchPeriods: list):
        for period in self.schedule.getOpenPeriods():
            if period in lunchPeriods:
                return True
        return False
    
        
class Teacher(Individual):
    def __init__(self, tag: int, qualifications: list, openPeriods: list):
        super().__init__(tag)
        self.qualifications = qualifications
        self.openPeriods = openPeriods
        # TODO: Consider checking if openPeriods and off add to 8?
    
    def isQualified(self, courseCode: str):
        return (courseCode in self.qualifications)
    
    def getOpenPeriods(self):
        return self.openPeriods
    
    def addSection(self, newSection: Section):
        self.schedule.addSection(newSection)
        self.openPeriods.remove(newSection.period)
    
    def removeSection(self, section: Section):
        self.schedule.removeSection(section)
        self.openPeriods.append(section.period)
    

class Student(Individual):
    def __init__(self, tag: int, grade: int):
        super().__init__(tag)
        self.grade = grade
        self.reqCores = []
        self.reqElectives = []
        self.reqOffPeriods = []
        # TODO: Consider checking if openPeriods and off add to 8?
    
    def addReqCore(self, newCore: course):
        if newCore not in self.reqCores:
            self.reqCores.append(newCore)
    
    def addReqElective(self, newElective: course):
        if newElective not in self.reqElectives:
            self.reqElectives.append(course)
    
    def addReqOffPeriod(self, newOff: int):
        if newOff not in self.reqOffPeriods:
            self.reqOffPeriods.append(newOff)
    
    def getGrade(self) -> int:
        return self.grade

    def getReqCore(self) -> list:
        return self.reqCores
    
    def getReqElectives(self) -> list:
        return self.reqElectives
    
    def getReqOff(self) -> list:
        return self.reqOffPeriods
    
    def removeReqCore(self, core: course):
        if core in self.reqCores:
            self.reqCores.remove(core)
    
    def removeReqElective(self, elective: course):
        if elective in self.reqElectives:
            self.reqCores.remove(elective)
    
    def removeReqOff(self, off: int):
        if off in self.reqOffPeriods:
            self.reqCores.remove(off)