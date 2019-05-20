
import random
class Patient:
    def __init__(self,name, severity= 0):
        self.severity = severity
        self.name = name

    def RetrieveSeverity(self):
        self.severity = random.randint(1, 10)

    def TreatPatient(self):
        if self.severity >= 1:
            self.severity -= 1

class Queue:
    def __init__(self, patients = []):
        self.patients = patients
    
    def addPatient(self, Patient):
        self.patients.append(Patient)

    def theNextPatient(self):

        pass

class Hospital:
    def __init__(self, Queue):
        self.Queue = Queue

    def addPatient(self, Patient):
        self.Queue.addPatient(Patient)

    def treatNextPatient(self):
        nextSeverity = self.Queue.theNextPatient()
        for i in self.Queue:
            if i.severity == nextSeverity:
                i.TreatPatient()

class SafeQueue(Queue):
    def __init__(self, patients = [] ):
        Queue.__init__(self, patients)

    def theNextPatient(self):
        severity = {}
        for i in self.patients:
            if i.severity == 0:
                self.patients.remove(i)
            else:
                severity[i.name]= i.severity
        if len(self.patients) == 0:
            return None
        else:
            nextseverity = max(severity.values())
            return nextseverity
            for key in severity:
                if severity[key] == nextseverity:
                    return key

class ClassicQueue(Queue):
    def __init__(self, patients= []):
        Queue.__init__(self, patients)

    def theNextPatient(self):
        while len(self.patients) != 0:
            for i in self.patients:
                if i.severity == 0:
                    self.patients.remove(i)
                else:
                    print(f"{i.name}")
                    i.TreatPatient()
        
                       
patient1 = Patient("Sara")
patient1.RetrieveSeverity()
print(patient1.severity)
# patient1.TreatPatient()
# print(patient1.severity)   
patient2 = Patient("Daisy")
patient2.RetrieveSeverity()
print(patient2.severity)

queue = ClassicQueue()
queue.addPatient(patient1)
queue.addPatient(patient2)
queue.theNextPatient()



        
      