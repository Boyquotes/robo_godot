# Simulação de robô

Este trabalho simula a comunicação com um braço robótico vagamente inspirado no modelo Dobot Magician Lite. Ele é composto de três partes:

1. Frontend: HTML servido pelo backend, que permite a entrada das coordenadas desejadas para a posição do robô na simulação.
2. Backend: servidor desenvolvido em Flask, que serve um template HTML como frontend e se comunica com um banco de dados SQLite utilizando a ORM SQLAlchemy, para guardar as posições do robô.
3. Simulação: adaptação do código de braço robótico 3D desenvolvido em Godot por @bborncr (https://github.com/bborncr/RobotArmTest)

Apesar de o frontend aceitar 8 entradas (x, y, z, r, j1, j2, j3, j4), apenas as coordenadas x, y e z são utilizadas para movimentação do robô na simulação. As outras aparecem na interface em Godot, mas não influenciam o movimento do objeto 3D. 

## Rodando o programa
1. Clone este repositório

### Frontend e backend
1. Acesse a pasta raiz deste repositório na sua linha de comando e ative o ambiente virtual
2. Instale as dependências necessárias listadas em requirements.txt
3. Acesse a subpasta /src
4. Rode o servidor

```
python3 main.py
```

Acesse o frontend no link http://127.0.0.1:5000/

#### Documentação da API
As rotas da API para comunicação com o banco de dados se encontram no caminho http://127.0.0.1:5000/api/.

A documentação completa está descrita nesta coleção do Postman: https://documenter.getpostman.com/view/23245053/2s93RWPr7t

### Simulação
1. Faça o download do software Godot na versão 3.
2. Importe o arquivo 'project.godot' disponível no caminho src/simulacao
3. Execute a simulação clicando no botão de play, no canto superior direito da interface do Godot

Agora, ao enviar novas coordenadas pelo frontend, o objeto 3D da simulação se movimentará de acordo.

## Lógica do programa

Quando o usuário envia coordenadas pelo frontend, um JSON é gerado com os atributos x, y, z, r, j1, j2, j3, j4. Esse JSON é encaminhado para o servidor, que o salva no banco de dados em SQLite. Ao mesmo tempo, o Javascript da página faz requisições regulares (de 1 em 1 segundo) para a rota de API que retorna todas as posições salvas no banco. O resultado dessa requisição é utilizado para alimentar a tabela.

Paralelamente, a simulação em Godot também faz requisições regulares (1 em 1 segundo) para a rota que retorna a última posição adicionada. Quando a posição retornada é diferente da última posição assumida pelo robô, o programa movimenta o objeto 3D para a nova posição através de uma série de interpolações para estimar os pontos intermediários. Nesse caso, considera-se apenas as coordenadas x, y e z, de modo que os valores das juntas são inferidos através de uma função de cinemática inversa. As outras coordenadas (r, j1, j2, j3, j4) apenas aparecem na interface do Godot, mas não influenciam no movimento em si.