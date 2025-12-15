# gui.py
"""
Módulo da interface gráfica (GUI) do sistema.

Aqui você cria:
- Janela principal
- Abas (registro, saldos, relatórios)
- Campos, botões, labels
- E conecta as ações às funções de lógica e Excel.
"""

import tkinter as tk
from tkinter import ttk, messagebox
# depois você importa as funções reais:
# from excel_io import registrar_movimentacao
# from logica import calcular_saldo_diario, calcular_saldo_mensal, calcular_saldo_cliente


class AppControleRestaurante(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Controle de Caixa - Restaurante")
        self.geometry("800x600")

        self._criar_componentes()

    def _criar_componentes(self):
        """
        Cria as abas principais usando ttk.Notebook:
        - Registrar movimentação
        - Consultar saldos
        - Relatórios
        """
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        # Aba 1: Registro
        frame_registro = ttk.Frame(notebook)
        notebook.add(frame_registro, text="Registrar movimentação")

        # Aba 2: Saldos
        frame_saldos = ttk.Frame(notebook)
        notebook.add(frame_saldos, text="Consultar saldos")

        # Aba 3: Relatórios
        frame_relatorios = ttk.Frame(notebook)
        notebook.add(frame_relatorios, text="Relatórios")

        self._criar_aba_registro(frame_registro)
        self._criar_aba_saldos(frame_saldos)
        self._criar_aba_relatorios(frame_relatorios)

    def _criar_aba_registro(self, frame):
        """
        Aba de registro de movimentações.
        Campos:
            - Cliente
            - Valor
            - Data
            - Hora
            - Tipo de transação
            - Observação
        Botão:
            - Registrar movimentação
        """

        # Cliente
        ttk.Label(frame, text="Cliente:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_cliente = ttk.Entry(frame)
        self.entry_cliente.grid(row=0, column=1, padx=5, pady=5)

        # Valor
        ttk.Label(frame, text="Valor (R$):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_valor = ttk.Entry(frame)
        self.entry_valor.grid(row=1, column=1, padx=5, pady=5)

        # Data
        ttk.Label(frame, text="Data (dd/mm/aaaa):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_data = ttk.Entry(frame)
        self.entry_data.grid(row=2, column=1, padx=5, pady=5)

        # Hora
        ttk.Label(frame, text="Hora (hh:mm):").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_hora = ttk.Entry(frame)
        self.entry_hora.grid(row=3, column=1, padx=5, pady=5)

        # Tipo de transação
        ttk.Label(frame, text="Tipo de transação:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.combo_tipo = ttk.Combobox(frame, values=["Consumo", "Pagamento", "Fiado"])
        self.combo_tipo.grid(row=4, column=1, padx=5, pady=5)

        # Observação
        ttk.Label(frame, text="Observação:").grid(row=5, column=0, sticky="nw", padx=5, pady=5)
        self.text_obs = tk.Text(frame, width=40, height=4)
        self.text_obs.grid(row=5, column=1, padx=5, pady=5)

        # Botão registrar
        btn_registrar = ttk.Button(frame, text="Registrar movimentação", command=self._acao_registrar)
        btn_registrar.grid(row=6, column=0, columnspan=2, pady=10)

    def _acao_registrar(self):
        """
        Lê os dados dos campos, faz validações básicas
        e depois chama registrar_movimentacao (quando implementado).

        Por enquanto, você pode só:
        - Ler os valores
        - Dar um print no terminal
        - Mostrar uma mensagem de sucesso
        pra testar a GUI antes de conectar ao Excel.
        """
        # Exemplo de leitura (para usar depois):
        cliente = self.entry_cliente.get()
        valor = self.entry_valor.get()
        data = self.entry_data.get()
        hora = self.entry_hora.get()
        tipo = self.combo_tipo.get()
        observacao = self.text_obs.get("1.0", tk.END).strip()

        # TODO: aqui você vai adicionar validações
        # TODO: e depois chamar registrar_movimentacao(...)

        messagebox.showinfo("Info", "Função de registrar ainda será implementada.")

    def _criar_aba_saldos(self, frame):
        """
        Aqui você vai criar:
        - Campos para consultar saldo diário (campo data + botão)
        - Campos para consultar saldo mensal (mês/ano + botão)
        - Campos para consultar saldo por cliente
        - Labels para exibir os resultados
        """
        pass

    def _criar_aba_relatorios(self, frame):
        """
        Aqui você vai criar:
        - Botões para gerar relatório mensal/anual
        - Área para exibir algum resumo ou status
        """
        pass


def rodar_app():
    app = AppControleRestaurante()
    app.mainloop()
