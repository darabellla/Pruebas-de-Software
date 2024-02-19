'''Reservation Class'''

from A01245026_A62.classes.hotel import Hotel
from A01245026_A62.classes.customer import Customer


class Reservation:
    '''Reservation Class'''
    # pylint: disable=too-many-arguments
    def __init__(self,
                 reservation_id,
                 customer: Customer,
                 hotel: Hotel,
                 start_date,
                 end_date,
                 status="activa"):
        '''Inicializa una nueva reservación'''
        self.reservation_id = reservation_id
        self.customer = customer
        self.hotel = hotel
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def get_reservation_id(self):
        """Devuelve el identificador único de la reservación."""
        return self.reservation_id

    def get_customer(self) -> Customer:
        """Devuelve la instancia del cliente asociada con la reservación."""
        return self.customer

    def get_hotel(self) -> Hotel:
        """Devuelve la instancia del hotel asociada con la reservación."""
        return self.hotel

    def get_start_date(self):
        """Devuelve la fecha de inicio de la reservación."""
        return self.start_date

    def get_end_date(self):
        """Devuelve la fecha de fin de la reservación."""
        return self.end_date

    def get_status(self):
        """Devuelve el estado actual de la reservación."""
        return self.status

    def set_status(self, status):
        """Establece el estado de la reservación."""
        self.status = status

    def mostrar_informacion(self):
        """Imprime en consola la información detallada de la reservación."""
        print(f"ID de la Reservación: {self.reservation_id}")
        print(f"ID del Cliente: {self.customer.get_customer_id()}")
        print(f"ID del Hotel: {self.hotel.get_id()}")
        print(f"Fecha de Inicio: {self.start_date}")
        print(f"Fecha de Fin: {self.end_date}")
        print(f"Estado: {self.status}")
