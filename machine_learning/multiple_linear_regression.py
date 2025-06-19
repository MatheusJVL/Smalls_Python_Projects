import numpy as np
import matplotlib.pyplot as plt

# Dados de entrada (metros quadrados e número de quartos)
x = np.array([
    [50, 3],  # Exemplo 1: 50m², 3 quartos
    [80, 2],  # Exemplo 2: 80m², 2 quartos
    [120, 4]  # Exemplo 3: 120m², 4 quartos
])

# Valores esperados (preço em milhares)
y = np.array([300, 450, 600])

# Normalização dos dados
x_max = np.max(x, axis=0)
y_max = np.max(y)
x = x / x_max
y = y / y_max

# Inicialização dos parâmetros
w = np.zeros(x.shape[1])
b = 0
alpha = 0.01  # Taxa de aprendizado
epochs = 100000  # Número de iterações

# Função de predição


def predict_function(x, w, b):
    return np.dot(x, w) + b

# Função de custo


def cost_function(x, y, w, b):
    m = len(y)
    error = np.sum((predict_function(x, w, b) - y) ** 2) / m
    return error

# Função de descida de gradiente


def descent_gradient(w, b, x, y, alpha):
    m = len(y)
    predictions = predict_function(x, w, b)
    error = predictions - y
    dw = np.dot(x.T, error) / m
    db = np.sum(error) / m
    w -= alpha * dw
    b -= alpha * db
    return w, b

# Função de treinamento


def train(x, y, w, b, alpha, epochs):
    errors = []
    for i in range(epochs):
        w, b = descent_gradient(w, b, x, y, alpha)
        if i % 10000 == 0:
            error = cost_function(x, y, w, b)
            errors.append(error)
            print(f"Iteração {i}: Erro = {error:.6f}")
    return w, b, errors

# Treinamento do modelo


w, b, errors = train(x, y, w, b, alpha, epochs)

# Fazendo previsões
novo_imovel = np.array([100, 3])  # 100m², 3 quartos
novo_imovel_normalizado = novo_imovel / x_max
preco_predito = predict_function(novo_imovel_normalizado, w, b) * y_max

# Gráfico de erro durante o treinamento
plt.plot(errors)
plt.xlabel('Iterações')
plt.ylabel('Erro')
plt.title('Evolução do Erro durante o Treinamento')
plt.show()

# Resultado final da previsão
print(f"Para um imóvel de {novo_imovel[0]}m² e {novo_imovel[1]} '\
'quartos, o preço previsto é {preco_predito:.3f} mil")
