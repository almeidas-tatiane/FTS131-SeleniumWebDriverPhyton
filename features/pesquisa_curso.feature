#language: pt
Funcionalidade: Pesquisa Curso
  Cenario: Pesquisar curso ao clicar na lupa
    Dado que acesso o site da Iterasys
    Quando pesquiso pelo curso 'Mantis'
    E clico na Lupa
    Entao exibe o curso 'Mantis' na pagina de resultados
    Quando clico no curso 'Mantis'
    Entao exibe a pagina do carrinho com o curso 'Mantis'e o preco de 'R$ 59,99'