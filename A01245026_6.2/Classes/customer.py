class Customer:
    def __init__(self, customer_id, name, contact):
        self.customer_id = customer_id
        self.name = name
        self.contact = contact

    def get_customer_id(self):
        return self.customer_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_contact(self):
        return self.contact

    def set_contact(self, contact):
        self.contact = contact

    def mostrar_informacion(self):
        print(f"ID del Cliente: {self.customer_id}")
        print(f"Nombre: {self.name}")
        print(f"Contacto: {self.contact}")
        
