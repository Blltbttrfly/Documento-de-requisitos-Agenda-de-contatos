#RF01 cadastrar contato

class Contato:
    def __init__(self, nome, telefone, nacionalidade, email, vinculo, aniversario):
        self.nome = nome    
        self.telefone = telefone
        self.nacionalidade = nacionalidade
        self.email = email
        self.vinculo = vinculo
        self.aniversario = aniversario

    def mostrar_contato(self):
        print(f"""
INFORMAÇÕES DO CONTATO:
{self.nome}
{self.telefone}
{self.nacionalidade}
{self.email}
{self.vinculo}
{self.aniversario}

""")


    def novo_contato(self):
        novo_nome = input("Nome:")
        novo_telefone = input("Telefone:")
        novo_nacional = input("Nacionalidade:")
        novo_email = input("E-mail:")
        novo_vinculo = input("Vínculo:")
        novo_aniversario = input("Aniversário:")
        
        novo_ctt = Contato(novo_nome, novo_telefone, novo_nacional, novo_email, novo_vinculo, novo_aniversario)

        return novo_ctt