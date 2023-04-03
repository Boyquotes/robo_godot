# Simulação de robô

Este trabalho simula a comunicação com um braço robótico vagamente inspirado no modelo Dobot Magician Lite. Ele é composto de três partes:

1. Frontend: HTML servido pelo backend, que permite a entrada das coordenadas desejadas para a posição do robô na simulação.
2. Backend: servidor desenvolvido em Flask, que serve um template HTML como frontend e se comunica com um banco de dados SQLite utilizando a ORM SQLAlchemy, para guardar as posições do robô.
3. Simulação: adaptação do código de braço robótico 3D desenvolvido em Godot por @bborncr (https://github.com/bborncr/RobotArmTest)

Apesar de o frontend aceitar 8 entradas (x, y, z, r, j1, j2, j3, j4), apenas as coordenadas x, y e z são utilizadas para movimentação do robô na simulação. As outras aparecem na interface em Godot, mas não influenciam o movimento do objeto 3D. 

## Rodando o programa

## Documentação da API