from course import CourseType, Course, Section
class Schedule:
    def __init__(self, tag: int):
        self.sections = []
        self.tag = tag
    
    def getOpenPeriods(self) -> list:
        occupied = []
        for section in self.sections:
            occupied.append(section.period)
        ret = [x for x in range(1, 9) if x not in occupied]  # 9 since range does not include last term
        return ret
    
    def getSections(self) -> list:
        return self.sections
    
    def addSection(self, newSection: Section):
        self.sections.append(newSection)
    
    def removeSection(self, section: Section):
        self.sections.remove(section)
    

        