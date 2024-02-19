'''Class para provar el módulo de customer'''

import io
import unittest
from unittest.mock import patch
from A01245026_A62.classes.customer import Customer


class TestCustomer(unittest.TestCase):
    '''Class para provar el módulo de customer'''

    def setUp(self):
        """Este método se ejecuta antes de cada prueba."""
        self.customer = Customer("C001", "Octavio Sanchez", "octaviosanchez@example.com")

    def test_creacion_customer(self):
        """Test para verificar la correcta creación de un objeto Customer."""
        self.assertEqual(self.customer.customer_id, "C001")
        self.assertEqual(self.customer.name, "Octavio Sanchez")
        self.assertEqual(self.customer.contact, "octaviosanchez@example.com")

    def test_modificar_contacto(self):
        """Test para verificar la actualización del contacto del cliente."""
        nuevo_contacto = "octavio.sanchez_modificado@example.com"
        self.customer.set_contact(nuevo_contacto)
        self.assertEqual(self.customer.get_contact(), nuevo_contacto)

    def test_modificar_nombre(self):
        """Test para verificar la actualización del nombre del cliente."""
        nuevo_nombre = "Ana Espino"
        self.customer.set_name(nuevo_nombre)
        self.assertEqual(self.customer.get_name(), nuevo_nombre)

    def test_mostrar_informacion(self):
        """Test para verificar que mostrar_informacion sea correcta."""
        expected_output = ("ID del Cliente: C001\n"
                           "Nombre: Octavio Sanchez\n"
                           "Contacto: octaviosanchez@example.com\n")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.customer.mostrar_informacion()
            self.assertEqual(fake_out.getvalue(), expected_output)


# Si ejecutas este script directamente, corre los tests
if __name__ == '__main__':
    unittest.main()