# HospitalManagementSystem in Python. This system models a 
# hospital with patients, doctors, appointments, and medical records.
#  It aims to demonstrate encapsulation, multiple interactions,
#  and system management
class Patient:
    def __init__(self, patient_id, name, age):
        self._patient_id = patient_id
        self._name = name
        self._age = age
        self._appointments = []
        self._medical_records = []

    def schedule_appointment(self, doctor, date):
        appointment = Appointment(self, doctor, date)
        self._appointments.append(appointment)
        doctor.add_appointment(appointment)
        print(f"Appointment scheduled with Dr. {doctor._name} on {date}")

    def add_medical_record(self, medical_record):
        self._medical_records.append(medical_record)

    def display_info(self):
        print(f"Patient ID: {self._patient_id}")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")

    def display_appointments(self):
        print("Appointments:")
        for appointment in self._appointments:
            print(f"{appointment._doctor._name} - {appointment._date}")

    def display_medical_records(self):
        print("Medical Records:")
        for record in self._medical_records:
            print(f"Date: {record._date} - Diagnosis: {record._diagnosis}")


class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self._doctor_id = doctor_id
        self._name = name
        self._specialization = specialization
        self._appointments = []

    def add_appointment(self, appointment):
        self._appointments.append(appointment)

    def display_info(self):
        print(f"Doctor ID: {self._doctor_id}")
        print(f"Name: Dr. {self._name}")
        print(f"Specialization: {self._specialization}")

    def display_appointments(self):
        print("Appointments:")
        for appointment in self._appointments:
            print(f"{appointment._patient._name} - {appointment._date}")


class Appointment:
    def __init__(self, patient, doctor, date):
        self._patient = patient
        self._doctor = doctor
        self._date = date


class MedicalRecord:
    def __init__(self, patient, date, diagnosis):
        self._patient = patient
        self._date = date
        self._diagnosis = diagnosis


class HospitalManagementSystem:
    def __init__(self):
        self._patients = {}
        self._doctors = {}

    def add_patient(self, patient):
        self._patients[patient._patient_id] = patient
        print(f"Added patient {patient._name} to the system")

    def add_doctor(self, doctor):
        self._doctors[doctor._doctor_id] = doctor
        print(f"Added Dr. {doctor._name} to the system")

    def display_patients(self):
        print("Patients:")
        for patient in self._patients.values():
            print(f"Patient ID: {patient._patient_id} - Name: {patient._name}")

    def display_doctors(self):
        print("Doctors:")
        for doctor in self._doctors.values():
            print(f"Doctor ID: {doctor._doctor_id} - Dr. {doctor._name}")

    def get_patient(self, patient_id):
        return self._patients.get(patient_id)

    def get_doctor(self, doctor_id):
        return self._doctors.get(doctor_id)


# Creating instances of the Patient, Doctor, and HospitalManagementSystem classes
hospital = HospitalManagementSystem()

patient1 = Patient("P001", "Alice Johnson", 30)
patient2 = Patient("P002", "Bob Smith", 45)

doctor1 = Doctor("D001", "Emily Davis", "Cardiology")
doctor2 = Doctor("D002", "John Anderson", "Orthopedics")

hospital.add_patient(patient1)
hospital.add_patient(patient2)

hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)

patient1.schedule_appointment(doctor1, "2023-08-20")
patient2.schedule_appointment(doctor2, "2023-08-25")

record1 = MedicalRecord(patient1, "2023-08-20", "Hypertension")
record2 = MedicalRecord(patient2, "2023-08-25", "Fractured leg")

patient1.add_medical_record(record1)
patient2.add_medical_record(record2)

patient1.display_info()
patient1.display_appointments()
patient1.display_medical_records()

doctor1.display_info()
doctor1.display_appointments()

hospital.display_patients()
hospital.display_doctors()

# Additional patients and doctors
patient3 = Patient("P003", "Eva Martinez", 28)
patient4 = Patient("P004", "David Harris", 55)

doctor3 = Doctor("D003", "Sophia Miller", "Pediatrics")
doctor4 = Doctor("D004", "Daniel Wilson", "Neurology")

hospital.add_patient(patient3)
hospital.add_patient(patient4)

hospital.add_doctor(doctor3)
hospital.add_doctor(doctor4)

# More appointments and medical records
patient3.schedule_appointment(doctor3, "2023-09-10")
patient4.schedule_appointment(doctor4, "2023-09-15")

record3 = MedicalRecord(patient3, "2023-09-10", "Common cold")
record4 = MedicalRecord(patient4, "2023-09-15", "Migraine")

patient3.add_medical_record(record3)
patient4.add_medical_record(record4)

# Displaying information
patient3.display_info()
patient3.display_appointments()
patient3.display_medical_records()

doctor3.display_info()
doctor3.display_appointments()

hospital.display_patients()
hospital.display_doctors()
