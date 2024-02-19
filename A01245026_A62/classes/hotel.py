'''Hotel Class'''

import datetime
from A01245026_A62.classes.customer import Customer
from A01245026_A62.classes.reservation import Reservation


class Hotel:
    '''Hotel Class'''

    def __init__(self, hotel_id, nombre, ubicacion, num_habitaciones):
        """Inicializa un nuevo hotel"""
        self.id = hotel_id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.num_habitaciones = num_habitaciones
        self.habitaciones_disponibles = num_habitaciones
        self.reservations = []

    def get_id(self):
        """Devuelve el identificador del hotel."""
        return self.id

    def get_nombre(self):
        """Devuelve el nombre del hotel."""
        return self.nombre

    def set_nombre(self, nombre):
        """Establece un nuevo nombre para el hotel."""
        self.nombre = nombre

    def get_ubicacion(self):
        """Devuelve la ubicación del hotel."""
        return self.ubicacion

    def set_ubicacion(self, ubicacion):
        """Establece una nueva ubicación para el hotel."""
        self.ubicacion = ubicacion

    def get_num_habitaciones(self):
        """Devuelve el número total de habitaciones del hotel."""
        return self.num_habitaciones

    def set_num_habitaciones(self, num_habitaciones):
        """Establece el número total de habitaciones del hotel."""
        self.num_habitaciones = num_habitaciones

    def get_habitaciones_disponibles(self):
        """Devuelve el número de habitaciones disponibles."""
        return self.habitaciones_disponibles

    def set_habitaciones_disponibles(self, habitaciones_disponibles):
        """Establece el número de habitaciones disponibles."""
        self.habitaciones_disponibles = habitaciones_disponibles

    def actualizar_habitaciones_disponibles(self, cantidad):
        """
        Actualiza el número de habitaciones disponibles.

        Aumenta el conteo con números positivos y lo disminuye con negativos.
        """
        self.habitaciones_disponibles += cantidad

    def mostrar_informacion(self):
        """Imprime la información detallada del hotel, incluye disponibilidad
        de habitaciones.
        """
        print(f"Hotel ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Número total de habitaciones: {self.num_habitaciones}")
        print(f"Habitaciones disponibles: {self.habitaciones_disponibles}")

    def reservar_cuarto(self, customer: Customer):
        """
        Permite a un cliente reservar una habitación, actualizando la lista
        de reservaciones y la disponibilidad.

        Args:
            customer: La instancia del cliente que realiza la reserva.

        Returns:
            Una instancia de la reserva creada.
        """

        reservation_id = len(self.reservations) + 1
        start_date = datetime.date.today()
        end_date = start_date + datetime.timedelta(days=1)

        reservation = Reservation(reservation_id=reservation_id,
                                  customer=customer, hotel=self,
                                  start_date=start_date,
                                  end_date=end_date, status="activa")
        self.reservations.append(reservation)
        return reservation
    