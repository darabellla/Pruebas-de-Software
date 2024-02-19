'''Class para provar el módulo de reservation'''

import unittest
from unittest.mock import patch
from io import StringIO
from A01245026_A62.classes.hotel import Hotel
from A01245026_A62.classes.customer import Customer
from A01245026_A62.classes.reservation import Reservation


class TestReservation(unittest.TestCase):
    '''Class para provar el módulo de reservation'''

    def setUp(self):
        """Este método se ejecuta antes de cada prueba"""
        self.customer = Customer("C001", "Octavio Sánchez", "octaviosanchez@example.com")
        self.hotel = Hotel(1, "Hotel Prueba", "Ciudad Prueba", 100)
        self.reservation = Reservation("R01", self.customer,
                                       self.hotel, "2023-12-08", "2023-12-18")

    def test_creacion_reservation(self):
        """Test para verificar la correcta creación de un objeto Reservation"""
        self.assertEqual(self.reservation.reservation_id, "R01")
        self.assertEqual(self.reservation.customer, self.customer)
        self.assertEqual(self.reservation.hotel, self.hotel)
        self.assertEqual(self.reservation.start_date, "2023-12-08")
        self.assertEqual(self.reservation.end_date, "2023-12-18")
        self.assertEqual(self.reservation.status, "activa")

    def test_modificar_estado_reservacion(self):
        """Test para verificar la actualización del estado de la reservación"""
        nuevo_estado = "cancelada"
        self.reservation.set_status(nuevo_estado)
        self.assertEqual(self.reservation.get_status(), nuevo_estado)

    def test_mostrar_informacion(self):
        """Test para verificar que mostrar_informacion es correcta."""
        expected_output = (
            "ID de la Reservación: R01\n"
            "ID del Cliente: C001\n"
            "ID del Hotel: 1\n"
            "Fecha de Inicio: 2023-12-08\n"
            "Fecha de Fin: 2023-12-18\n"
            "Estado: activa\n"
        )
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.reservation.mostrar_informacion()
            self.assertEqual(fake_out.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()