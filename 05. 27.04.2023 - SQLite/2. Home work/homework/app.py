import datetime
import random
from entities.Appointment import Appointment
from entities.Doctor import Doctor
from entities.Patient import Patient
from entities.Person import Person
from entities.Speciality import Speciality
from infrastructure import utils
from models.AppointmentDateStatistic import AppointmentDateStatistic
from models.AppointmentWithDoctorSalary import AppointmentWithDoctorSalary
from models.SpecialityStatistic import SpecialityStatistic

from repositories.AppointmentsRepository import AppointmentsRepository
from repositories.DoctorsRepository import DoctorsRepository
from repositories.PatientsRepository import PatientsRepository
from repositories.PeopleRepository import PeopleRepository
from repositories.SpecialitiesRepository import SpecialitiesRepository


# 1	Запрос к данным	    Выбирает информацию о пациентах с фамилиями, начинающимися на заданную параметром 
# последовательность букв
def show_query01():
    surname = random.choice(PatientsRepository.get_all()).person.surname[0:3]
    data = PatientsRepository.get_all_by_surname_start_with(surname)
    Patient.show_table(data, f'Пациенты у которых фамилия начинается с "{surname}"')


# 2	Запрос к данным 	Выбирает информацию о врачах, для которых значение в поле Процент отчисления на зарплату, 
# больше 2.3% (задавать параметром)
def show_query02():
    min_v = 2
    max_v = 6
    percent = random.uniform(min_v, max_v)

    data = DoctorsRepository.get_all_by_percent_over(percent)
    Doctor.show_table(data, f'Доктора с процентом отчислений за приём выше {percent:.1f}%')


# 3	Запрос к данным	    Выбирает информацию о приемах за некоторый период, заданный параметрами
def show_query03():
    min_v = utils.get_date('2022-10-01') + datetime.timedelta(days=random.randint(10, 15))
    max_v = min_v + datetime.timedelta(days=random.randint(10, 20))

    data = AppointmentsRepository.get_all_by_appointment_date_range(min_v, max_v)
    Appointment.show_table(
        data,
        f'Приёмы за период от {utils.get_local_format_date(min_v)} до {utils.get_local_format_date(max_v)}'
    )


# 4	Запрос к данным 	Выбирает информацию о докторах, специальность которых задана параметром 
def show_query04():
    speciality_name = random.choice(SpecialitiesRepository.get_all()).name

    data = DoctorsRepository.get_all_by_speciality(speciality_name)
    Doctor.show_table(data, f'Доктора со специальностью "{speciality_name}"')


# 5	Запрос к данным 	Вычисляет размер заработной платы врача за каждый прием. Включает поля Фамилия врача, 
# Имя врача, Отчество врача, Специальность врача, Стоимость приема, Зарплата. Сортировка по полю Специальность врача
def show_query05():
    data = AppointmentsRepository.get_all_with_salary()
    AppointmentWithDoctorSalary.show_table(data, f'Приёмы с вычисленной платой врачу за каждый приём')


# 6	Итоговый запрос 	Выполняет группировку по полю Дата приема. Для каждой даты вычисляет максимальную стоимость приема
def show_query06():
    data = AppointmentsRepository.group_by_appointment_date()
    AppointmentDateStatistic.show_table(data, f'Статистика по дате приёма')


# 7	Итоговый запрос 	Выполняет группировку по полю Специальность. Для каждой специальности вычисляет средний 
# Процент отчисления на зарплату от стоимости приема
def show_query07():
    data = AppointmentsRepository.group_by_speciality()
    SpecialityStatistic.show_table(data, f'Статистика по специальности')


# вывод Приёмов
def show_appointments():
    data = AppointmentsRepository.get_all()
    Appointment.show_table(data)


# вывод Докторов
def show_doctors():
    data = DoctorsRepository.get_all()
    Doctor.show_table(data)


# вывод Пациентов
def show_patients():
    data = PatientsRepository.get_all()
    Patient.show_table(data)


# вывод Персон
def show_people():
    data = PeopleRepository.get_all()
    Person.show_table(data)


# вывод Специальностей
def show_specialities():
    data = SpecialitiesRepository.get_all()
    Speciality.show_table(data)


if __name__ == "__main__":
    from main import main

    main()
