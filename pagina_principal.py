import tkinter as tk
from tkinter import messagebox
from usuarios import Usuarios
from banco import Banco

class PaginaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gestão")
        self.master.geometry("800x600")

        tk.Button(self.master, text="Adicionar Usuário", command=self.adicionar_usuario).pack(pady=10)
        tk.Button(self.master, text="Alterar Usuário", command=self.alterar_usuario).pack(pady=10)
        tk.Button(self.master, text="Excluir Usuário", command=self.excluir_usuario).pack(pady=10)
        tk.Button(self.master, text="Gerenciar Usuários", command=self.gerenciar_usuarios).pack(pady=10)

    def adicionar_usuario(self):
        AdicionarUsuario(self.master)

    def alterar_usuario(self):
        AlterarUsuario(self.master)

    def excluir_usuario(self):
        ExcluirUsuario(self.master)

    def gerenciar_usuarios(self):
        GerenciarUsuarios(self.master)

class AdicionarUsuario:
    def __init__(self, master):
        self.master = tk.Toplevel(master)
        self.master.title("Adicionar Usuário")
        self.master.geometry("400x400")

        self.usuario = Usuarios()

        tk.Label(self.master, text="Nome:").pack(pady=5)
        self.nome_entry = tk.Entry(self.master)
        self.nome_entry.pack(pady=5)

        tk.Label(self.master, text="Telefone:").pack(pady=5)
        self.telefone_entry = tk.Entry(self.master)
        self.telefone_entry.pack(pady=5)

        tk.Label(self.master, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(self.master)
        self.email_entry.pack(pady=5)

        tk.Label(self.master, text="Usuário:").pack(pady=5)
        self.usuario_entry = tk.Entry(self.master)
        self.usuario_entry.pack(pady=5)

        tk.Label(self.master, text="Senha:").pack(pady=5)
        self.senha_entry = tk.Entry(self.master, show="*")
        self.senha_entry.pack(pady=5)

        tk.Label(self.master, text="Cidade:").pack(pady=5)
        self.cidade_entry = tk.Entry(self.master)
        self.cidade_entry.pack(pady=5)

        tk.Button(self.master, text="Salvar", command=self.salvar_usuario).pack(pady=10)
        tk.Button(self.master, text="Voltar", command=self.master.destroy).pack(pady=5)

    def salvar_usuario(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()
        cidade = self.cidade_entry.get()

        # Adiciona o usuário no banco de dados
        try:
            self.usuario.banco.cursor.execute(
                "INSERT INTO tbl_usuarios (nome, telefone, email, usuario, senha, cidade) VALUES (?, ?, ?, ?, ?, ?)",
                (nome, telefone, email, usuario, senha, cidade)
            )
            self.usuario.banco.conn.commit()
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso.")
            self.master.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar usuário: {e}")

class AlterarUsuario:
    def __init__(self, master):
        self.master = tk.Toplevel(master)
        self.master.title("Alterar Usuário")
        self.master.geometry("400x500")

        self.usuario = Usuarios()

        tk.Label(self.master, text="ID do Usuário:").pack(pady=5)
        self.id_entry = tk.Entry(self.master)
        self.id_entry.pack(pady=5)
        tk.Button(self.master, text="Carregar Dados", command=self.carregar_dados).pack(pady=5)

        tk.Label(self.master, text="Nome:").pack(pady=5)
        self.nome_entry = tk.Entry(self.master)
        self.nome_entry.pack(pady=5)

        tk.Label(self.master, text="Telefone:").pack(pady=5)
        self.telefone_entry = tk.Entry(self.master)
        self.telefone_entry.pack(pady=5)

        tk.Label(self.master, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(self.master)
        self.email_entry.pack(pady=5)

        tk.Label(self.master, text="Usuário:").pack(pady=5)
        self.usuario_entry = tk.Entry(self.master)
        self.usuario_entry.pack(pady=5)

        tk.Label(self.master, text="Senha:").pack(pady=5)
        self.senha_entry = tk.Entry(self.master, show="*")
        self.senha_entry.pack(pady=5)

        tk.Label(self.master, text="Cidade:").pack(pady=5)
        self.cidade_entry = tk.Entry(self.master)
        self.cidade_entry.pack(pady=5)

        tk.Button(self.master, text="Salvar Alterações", command=self.salvar_alteracoes).pack(pady=10)
        tk.Button(self.master, text="Voltar", command=self.master.destroy).pack(pady=5)

    def carregar_dados(self):
        usuario_id = self.id_entry.get()
        if usuario_id:
            try:
                self.usuario.banco.cursor.execute("SELECT * FROM tbl_usuarios WHERE idusuario = ?", (usuario_id,))
                usuario = self.usuario.banco.cursor.fetchone()
                if usuario:
                    self.nome_entry.delete(0, tk.END)
                    self.nome_entry.insert(tk.END, usuario[1])

                    self.telefone_entry.delete(0, tk.END)
                    self.telefone_entry.insert(tk.END, usuario[2])

                    self.email_entry.delete(0, tk.END)
                    self.email_entry.insert(tk.END, usuario[3])

                    self.usuario_entry.delete(0, tk.END)
                    self.usuario_entry.insert(tk.END, usuario[4])

                    self.senha_entry.delete(0, tk.END)
                    self.senha_entry.insert(tk.END, usuario[5])

                    self.cidade_entry.delete(0, tk.END)
                    self.cidade_entry.insert(tk.END, usuario[6])
                else:
                    messagebox.showwarning("Aviso", "Usuário não encontrado.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar dados: {e}")

    def salvar_alteracoes(self):
        usuario_id = self.id_entry.get()
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()
        cidade = self.cidade_entry.get()

        try:
            self.usuario.banco.cursor.execute(
                "UPDATE tbl_usuarios SET nome = ?, telefone = ?, email = ?, usuario = ?, senha = ?, cidade = ? WHERE idusuario = ?",
                (nome, telefone, email, usuario, senha, cidade, usuario_id)
            )
            self.usuario.banco.conn.commit()
            messagebox.showinfo("Sucesso", "Usuário alterado com sucesso.")
            self.master.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao alterar usuário: {e}")

class ExcluirUsuario:
    def __init__(self, master):
        self.master = tk.Toplevel(master)
        self.master.title("Excluir Usuário")
        self.master.geometry("400x300")

        self.banco = Banco()

        tk.Label(self.master, text="Selecione o usuário para excluir:").pack(pady=10)
        self.lista_usuarios = tk.Listbox(self.master, width=50)
        self.lista_usuarios.pack(pady=10)

        self.carregarUsuarios()

        tk.Button(self.master, text="Excluir", command=self.excluirUsuario).pack(pady=5)
        tk.Button(self.master, text="Voltar", command=self.master.destroy).pack(pady=5)

    def carregarUsuarios(self):
        self.lista_usuarios.delete(0, tk.END)
        usuarios = Usuarios().getAllUsers()
        for usuario in usuarios:
            self.lista_usuarios.insert(tk.END, f"ID: {usuario[0]} | Nome: {usuario[1]}")

    def excluirUsuario(self):
        selecao = self.lista_usuarios.curselection()
        if selecao:
            usuario_id = Usuarios().getAllUsers()[selecao[0]][0]
            msg = Usuarios().deleteUser(usuario_id)
            messagebox.showinfo("Resultado", msg)
            self.carregarUsuarios()
        else:
            messagebox.showwarning("Seleção", "Nenhum usuário selecionado.")

class GerenciarUsuarios:
    def __init__(self, master):
        self.master = tk.Toplevel(master)
        self.master.title("Gerenciar Usuários")
        self.master.geometry("600x400")

        tk.Label(self.master, text="Usuários:").pack(pady=10)
        self.lista_usuarios = tk.Listbox(self.master, width=80)
        self.lista_usuarios.pack(pady=10)

        self.carregarUsuarios()

        tk.Button(self.master, text="Voltar", command=self.master.destroy).pack(pady=20)

    def carregarUsuarios(self):
        usuarios = Usuarios().getAllUsers()
        for usuario in usuarios:
            self.lista_usuarios.insert(tk.END, f"ID: {usuario[0]} | Nome: {usuario[1]}")
