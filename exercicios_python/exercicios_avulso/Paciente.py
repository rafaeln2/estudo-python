import builtins

class Paciente:
    def __init__(self, full_name: str, age: int, is_new_patient: bool):
        self.name = "John"
        self.age = 20
        self.isNewPatient = True

    def __str__(self):
        return "Meu nome é {}, tenho {} anos e sou {}.".format(self.name, self.age,
                                                               "novo paciente" if self.isNewPatient else "paciente veterano" )
pessoaA = Paciente("John", 20, True)

print(pessoaA.__str__())


