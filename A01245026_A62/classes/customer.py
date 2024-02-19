'''Customer Class'''


class Customer:
    '''Customer Class'''

    def __init__(self, customer_id, name, contact):
        '''Inicia nueva instancia de customer'''
        self.customer_id = customer_id
        self.name = name
        self.contact = contact

    def get_customer_id(self):
        """Devuelve el identificador único del cliente."""
        return self.customer_id

    def get_name(self):
        """Devuelve el nombre del cliente."""
        return self.name

    def set_name(self, name):
        """Establece el nombre del cliente."""
        self.name = name

    def get_contact(self):
        """Devuelve la información de contacto del cliente."""
        return self.contact

    def set_contact(self, contact):
        """Establece la información de contacto del cliente."""
        self.contact = contact

    def mostrar_informacion(self):
        """Imprime la información del cliente."""
        print(f"ID del Cliente: {self.customer_id}")
        print(f"Nombre: {self.name}")
        print(f"Contacto: {self.contact}")
        