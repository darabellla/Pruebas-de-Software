'''Reservation Class'''

from A01245026_A62.classes.hotel import Hotel
from A01245026_A62.classes.customer import Customer

class Reservation:
    def __init__(self, reservation_id, customer: Customer, hotel: Hotel, start_date, end_date, status="activa"):
        self.reservation_id = reservation_id
        self.customer = customer  # Almacena la referencia al objeto Customer
        self.hotel = hotel  # Almacena la referencia al objeto Hotel
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def get_reservation_id(self):
        return self.reservation_id

    # Actualiza este método para devolver la instancia de Customer
    def get_customer(self) -> Customer:
        return self.customer

    # Actualiza este método para devolver la instancia de Hotel
    def get_hotel(self) -> Hotel:
        return self.hotel

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def mostrar_informacion(self):
        print(f"ID de la Reservación: {self.reservation_id}")
        # Utiliza los métodos de las instancias para obtener la información
        print(f"ID del Cliente: {self.customer.get_customer_id()}")
        print(f"ID del Hotel: {self.hotel.get_id()}")
        print(f"Fecha de Inicio: {self.start_date}")
        print(f"Fecha de Fin: {self.end_date}")
        print(f"Estado: {self.status}")
