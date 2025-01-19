# yt-download-media
[ [English](README.md) | [PT-BR](./docs/README.br.md) ]

yt-download-media é uma ferramenta para baixar vídeos e áudios do YouTube de maneira simples e eficiente.

## Recursos

- Suporte para download de vídeos e áudios.
- Interface amigável e de fácil uso.
- Integração com a biblioteca yt-dlp para processamento de mídia. (https://github.com/yt-dlp/yt-dlp)

## Requisitos

Certifique-se de ter o seguinte instalado antes de usar o projeto:

- Python 3.10 ou superior
- yt-dlp (instalado via pip)

## Instalação

1. Clone o repositório:

   
bash
   git clone https://github.com/LucasAvela/yt-download-media.git
   cd yt-download-media


2. Instale as dependências necessárias:

   
bash
   pip install -r requirements.txt


## Uso

1. Execute o script principal:

   
bash
   python main.pyw


2. Insira o URL do vídeo do YouTube no campo "Video or Playlist URL".
3. Insira o caminho de saída no campo "Output PATH".
4. Escolha a o formato de saída.
5. Aguarde o término do processo. O arquivo será salvo no diretório especificado.

## Estrutura do Projeto

plaintext
yt-download-media/
├── main.pyw            # Arquivo principal do projeto
├── downloadManager.py  # Dependência do projeto
├── requirements.txt    # Dependências do Python
├── README.md           # Documentação do projeto


## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto.
2. Crie uma nova branch para sua funcionalidade ou correção de bug:

   
bash
   git checkout -b minha-branch


3. Faça as alterações e commit:

   
bash
   git commit -m "Descrição das alterações"


4. Envie suas alterações:

   
bash
   git push origin minha-branch


5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Feito com 💻 por [Lucas Avela](https://github.com/LucasAvela).
