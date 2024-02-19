'''Class para provar el módulo de hotel'''

import unittest
from A01245026_A62.classes.hotel import Hotel
from A01245026_A62.classes.customer import Customer


class TestHotel(unittest.TestCase):
    '''Class para provar el módulo de hotel'''

    def setUp(self):
        """Este método se ejecuta antes de cada prueba"""
        self.hotel = Hotel(1, "Hotel Prueba", "Ciudad Prueba", 100)

    def test_set_nombre(self):
        """Test para verificar la actualización del nombre del hotel."""
        self.hotel.set_nombre("Hotel Cambiado")
        self.assertEqual(self.hotel.get_nombre(), "Hotel Cambiado")

    def test_set_ubicacion(self):
        """Test para verificar la actualización de la ubicación del hotel."""
        self.hotel.set_ubicacion("Ubicación Cambiada")
        self.assertEqual(self.hotel.get_ubicacion(), "Ubicación Cambiada")

    def test_actualizar_habitaciones_disponibles(self):
        """Test para verificar la actualización de habitaciones disponibles."""
        self.hotel.actualizar_habitaciones_disponibles(-10)
        self.assertEqual(self.hotel.get_habitaciones_disponibles(), 90)
        self.hotel.actualizar_habitaciones_disponibles(5)
        self.assertEqual(self.hotel.get_habitaciones_disponibles(), 95)

    def test_reservar_cuarto(self):
        """Test para verificar la reserva de un cuarto."""
        customer = Customer("C001", "Octavio Sanchez", "octaviosanchez@example.com")
        initial_reservations_count = len(self.hotel.reservations)
        self.hotel.reservar_cuarto(customer)
        self.assertEqual(len(self.hotel.reservations),
                         initial_reservations_count + 1)
        # Verifica que la última reservación añadida tenga el cliente correcto
        self.assertEqual(self.hotel.reservations[-1].customer, customer)


if __name__ == '__main__':
    unittest.main()