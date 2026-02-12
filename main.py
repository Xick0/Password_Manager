# from datetime import datetime
# from typing import Optional


# class PasswordEntry:
#     """
#     Classe que representa uma entrada de senha no gestor de senhas.
    
#     Esta classe encapsula todos os dados relacionados a uma senha individual,
#     incluindo informações de autenticação e metadados.
#     """
    
#     def __init__(
#         self, 
#         service_name: str, 
#         username: str, 
#         password: str, 
#         email: Optional[str] = None,
#         notes: Optional[str] = None,
#         entry_id: Optional[str] = None
#     ):
#         """
#         Inicializa uma nova entrada de senha.
        
#         Args:
#             service_name (str): Nome do serviço/aplicação (ex: "Gmail", "GitHub")
#             username (str): Nome de utilizador para autenticação
#             password (str): Senha do utilizador (será encriptada depois)
#             email (Optional[str]): Email associado à conta
#             notes (Optional[str]): Notas adicionais sobre a entrada
#             entry_id (Optional[str]): ID único (gerado automaticamente se não fornecido)
#         """
#         self.entry_id = entry_id or self._generate_id()
#         self.service_name = service_name
#         self.username = username
#         self.password = password
#         self.email = email
#         self.notes = notes
#         self.created_at = datetime.now()
#         self.updated_at = datetime.now()
    
#     @staticmethod
#     def _generate_id() -> str:
#         """
#         Gera um ID único para a entrada usando timestamp.
        
#         Returns:
#             str: ID único base no timestamp
#         """
#         return str(int(datetime.now().timestamp() * 1000))
    
#     def update_password(self, new_password: str) -> None:
#         """
#         Atualiza a senha da entrada e registra o momento da atualização.
        
#         Args:
#             new_password (str): A nova senha
#         """
#         if not new_password or len(new_password) < 4:
#             raise ValueError("A senha deve ter pelo menos 4 caracteres")
        
#         self.password = new_password
#         self.updated_at = datetime.now()
    
#     def update_notes(self, new_notes: str) -> None:
#         """
#         Atualiza as notas da entrada.
        
#         Args:
#             new_notes (str): Novas notas
#         """
#         self.notes = new_notes
#         self.updated_at = datetime.now()
    
#     def get_info(self) -> dict:
#         """
#         Retorna um dicionário com as informações da entrada (sem exposição da senha).
        
#         Returns:
#             dict: Dicionário contendo as informações públicas da entrada
#         """
#         return {
#             "entry_id": self.entry_id,
#             "service_name": self.service_name,
#             "username": self.username,
#             "email": self.email,
#             "notes": self.notes,
#             "created_at": self.created_at.isoformat(),
#             "updated_at": self.updated_at.isoformat()
#         }
    
#     def __str__(self) -> str:
#         """
#         Representação em string da entrada (segura, sem expor a senha).
        
#         Returns:
#             str: Descrição legível da entrada
#         """
#         return f"PasswordEntry(service='{self.service_name}', username='{self.username}')"
    
#     def __repr__(self) -> str:
#         """
#         Representação técnica da entrada para debugging.
        
#         Returns:
#             str: Representação técnica
#         """
#         return f"PasswordEntry(id='{self.entry_id}', service='{self.service_name}')"


# # Exemplo de utilização
# if __name__ == "__main__":
#     # Criar uma nova entrada de senha
#     entry = PasswordEntry(
#         service_name="Gmail",
#         username="utilizador@example.com",
#         password="senha_forte_123",
#         email="utilizador@example.com",
#         notes="Conta pessoal de email"
#     )
    
#     # Exibir informações
#     print(entry)
#     print(entry.get_info())


from Password import Password

def main():

    pwd = Password()

    pwd.set_username("BISH")

    print(pwd.toString())

if __name__ == "__main__":
    main()