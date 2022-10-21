<a href="https://github.com/IsaacAlves7/python-programming"><img src="https://user-images.githubusercontent.com/61624336/193806052-860b7136-6764-448d-91ef-a444427a26b3.png" width="100%"/></a>

# It's a repository of Python language 🐍
> 🐍 **Preparação**: Para este conteúdo, o aluno deverá dispor de um computador com acesso à internet, um web browser com suporte a HTML 5 (Google Chrome, Mozilla Firefox, Microsoft Edge, Safari, Opera etc.), um editor de texto ou IDE (VSCode etc.) e o software Python3, com a versão mais recente, instalado na sua máquina local.

<a href="https://github.com/IsaacAlves7/python-programming"><div align="center"><img src="https://user-images.githubusercontent.com/61624336/193809777-0c363bd5-112a-4707-8292-7e77eba6d858.png" height="177"/></div></a>

# 🐒 Linguagem de programação
<div align="center"><img src="https://user-images.githubusercontent.com/61624336/112900537-065ce480-90ba-11eb-86f7-f9006445876a.png"></div>

Um **programa** é um conjunto de instruções, também conhecidas como **algoritmos**, que descrevem uma tarefa a ser realizada por um computador. O termo pode ser uma referência ao **código fonte**, escrito em alguma linguagem de programação, ou ao arquivo que contém a forma executável deste código fonte. Um programa torna um computador utilizável, sem ele um computador, mesmo o mais poderoso, nada mais é do que um objeto.

Os **computadores** são capazes de executar tarefas muito complexas, mas essa capacidade não lhes é inata. A natureza de um computador é bastante diferente. Ele só pode executar operações extremamente simples, por exemplo, um computador não pode avaliar o valor de uma função matemática complicada por si só, embora isto não esteja fora do âmbito das possibilidades num futuro próximo.

> Os **computadores contemporâneos** só podem avaliar os resultados de operações muito fundamentais, como adicionar ou dividir, mas podem fazê-lo muito rapidamente, e podem repetir estas ações virtualmente um qualquer número de vezes.

Imagine que quer saber a velocidade média que alcançou durante uma longa viagem. Sabe a distância, sabe o tempo, precisa da velocidade. Naturalmente, o computador será capaz de calcular isto, mas o computador não está ciente de coisas como distância, velocidade ou tempo. Portanto, é necessário instruir o computador a:

- Aceitar um número que represente a distância;
- Aceitar um número que represente o tempo de viagem;
- Dividir o valor anterior pelo último e armazenar o resultado na memória;
- Exibir o resultado (representando a velocidade média) num formato legível.

Estas quatro simples ações formam um **programa**. É claro que estes exemplos não são formalizados, e estão muito longe do que o computador pode compreender, mas são suficientemente bons para serem traduzidos para uma **linguagem** que o computador possa aceitar.

Uma **Linguagem (Language)**, nossa palavra-chave, é um meio (e uma ferramenta) para expressar e registar pensamentos. Há muitas linguagens ao nosso redor e algumas delas não requerem nem a fala nem a escrita, como a *linguagem corporal*; é possível expressar os seus sentimentos mais profundos com muita precisão sem dizer uma palavra.

Outra linguagem que usa diariamente é a sua *língua materna*, que usa para manifestar a sua vontade e para pensar na realidade. Os computadores também têm a sua própria linguagem, chamada **linguagem de máquina**, que é muito rudimentar.

### Machine code - Linguagem de máquina
O **código de máquina** ou **linguagem de máquina** é uma linguagem de programação de baixo nível, constituída por dígitos/bits binários que o computador lê e compreende, ou seja, é um conjunto de instruções executadas diretamente pela unidade de processamento central (CPU) de um computador. Cada instrução executa uma tarefa muito específica, como uma carga, um salto ou uma operação ALU em uma unidade de dados em um registrador ou memória da CPU. Todo programa executado diretamente por uma CPU é composto por uma série de tais instruções.

O **código de máquina numérico** pode ser considerado como a representação de nível ainda mais baixo de um programa de computador compilado e/ou montado ou como uma linguagem de programação primitiva e dependente de hardware. Embora seja possível escrever programas diretamente em código de máquina numérico, é tedioso e propenso a erros gerenciar bits individuais e calcular endereços numéricos e constantes manualmente. Portanto, raramente é feito hoje, exceto em situações que exigem otimização ou depuração extremas.

> 🙉 **Nota**: O código de máquina numérico não é o código ou linguagem de montagem, conhecida como **Assembly** ou Assembler, cujo é uma linguagem de programação de baixo-nível superior. 

[![machine](https://img.shields.io/badge/-machine_code-fff?style=social&logo=AirPlay-Video&logoColor=000000)](#)

```machine
010010101010010
010010100110100
010101100111010
010101010101011
010101010100101
010101010010111
```

> 🙉 **Nota**: as linguagens de máquina são desenvolvidas por humanos e não pela própria máquina.

> Um computador, mesmo o mais sofisticado tecnicamente, é desprovido até mesmo de um vestígio de **inteligência**. Esse é um assunto muito abordado quando estudamos para Inteligência Artifical e Machine Learning.

Pode-se dizer que é como um 🐵 *macaco* bem treinado - responde apenas a um conjunto pré-determinado de comandos conhecidos. Os comandos que reconhece são muito simples. Podemos imaginar que o computador responde a ordens como "pega nesse número, divide-o por outro e guarda o resultado".

Um conjunto completo de comandos conhecidos é chamado de **lista de instruções**, por vezes abreviado para **IL** (do inglês, **Instruction List**). Os diferentes tipos de computadores podem variar em função do tamanho das suas IL, e as instruções podem ser completamente diferentes em diferentes modelos.

Atualmente, nenhum computador é capaz de criar uma nova linguagem. No entanto, isso pode mudar em breve. Por outro lado, as pessoas também utilizam uma série de línguas muito diferentes, mas estas línguas desenvolveram-se naturalmente. Além disso, ainda estão a evoluir. São criadas novas palavras todos os dias e as palavras antigas desaparecem. Estas línguas são chamadas **linguagens naturais**.

Podemos dizer que cada linguagem (de máquina ou natural, não importa) é constituída pelos seguintes elementos:

- um **alfabeto**: um conjunto de símbolos utilizados para construir palavras de uma determinada linguagem (por exemplo, o alfabeto latino para inglês, o alfabeto cirílico para russo, o Kanji para japonês, etc.)
- um **lexis**: (ou seja, um dicionário) um conjunto de palavras que a linguagem oferece aos seus utilizadores (por exemplo, a palavra "computador" vem do dicionário de língua inglesa, enquanto que "cmoptrue" não; a palavra "chat" está presente tanto nos dicionários de inglês como de francês, mas os seus significados são diferentes)
- uma **sintaxe**: um conjunto de regras (formais ou informais, escritas ou sentidas intuitivamente) utilizadas para determinar se uma determinada sequência de palavras forma uma frase válida (por exemplo, "Eu sou uma pitão" é uma frase sintaticamente correta, enquanto "Eu uma pitão sou" não é)
- **semântica**: um conjunto de regras que determinam se uma determinada frase faz sentido (por exemplo, "Comi um donut" faz sentido, mas "Um donut comeu-me" não faz)

O **IL** é, de facto, **o alfabeto de uma linguagem de máquina**. Este é o conjunto mais simples e primário de símbolos que podemos utilizar para dar comandos a um computador. É a língua materna do computador.

Infelizmente, esta língua está muito longe de ser uma língua materna humana. Todos nós (tanto computadores como humanos) precisamos de algo mais, uma linguagem comum para computadores e humanos, ou uma ponte entre os dois mundos diferentes.

<img src="https://estacio.webaula.com.br/cursos/go0374/galeria/aula1/img/figura1.svg" align="right" height="377" title="Figura 1: Processo de compilação de um programa escrito na linguagem C">

> Precisamos de uma linguagem em que os humanos possam escrever os seus programas e uma linguagem que os computadores possam utilizar para executar os programas, uma linguagem que seja muito mais complexa do que a linguagem das máquinas e, no entanto, muito mais simples do que a linguagem natural.

Tais linguagens são muitas vezes chamadas **linguagens de programação de alto nível**. São pelo menos um pouco semelhantes aos naturais na medida em que utilizam símbolos, palavras e convenções legíveis para os seres humanos. Estas linguagens permitem aos seres humanos expressar comandos a computadores que são muito mais complexos do que os oferecidos pelas ILs.

Um *programa* escrito numa *linguagem de programação de alto nível* é chamado **source code**, também conhecido como *código-fonte* (em contraste com o *ee* executado por computadores). Da mesma forma, o ficheiro que contém o *source code* chama-se **source file**, també conhecido como *arquivo-fonte*.

A programação informática é o ato de compor os elementos da linguagem de programação selecionada pela ordem que provocará o efeito desejado. O efeito pode ser diferente em cada caso específico - depende da imaginação, conhecimento e experiência do programador.

É claro que tal composição tem de ser correta em muitos sentidos:

- **alfabeticamente** - um programa precisa de ser escrito num guião reconhecível, tal como romano, cirílico, etc.
- **lexicamente** - cada linguagem de programação tem o seu dicionário e é preciso dominá-lo; felizmente, é muito mais simples e menor do que o dicionário de qualquer língua natural;
- **sintaticamente** - cada linguagem tem as suas regras, e estas devem ser obedecidas;
- **semanticamente** - o programa tem de fazer sentido.

Infelizmente, um programador também pode cometer erros com cada um dos quatro sentidos acima referidos. Cada um deles pode fazer com que o programa se torne completamente inútil. 

Vamos supor que tenha escrito um programa com sucesso. Como persuadir o computador a executá-lo? Tem de transformar o seu programa em linguagem de máquina. Felizmente, a tradução pode ser feita pelo próprio computador, tornando todo o processo rápido e eficiente.

Há duas formas diferentes de transformar um programa de uma linguagem de programação de alto nível em linguagem de máquina:

- **COMPILAÇÃO** - o source program é traduzido uma vez (no entanto, este ato deve ser repetido sempre que modificar o source code) obtendo um ficheiro (por exemplo, um `ficheiro.exe` se o código se destinar a ser executado no MS Windows) contendo o machine code; agora pode distribuir o ficheiro por todo o mundo; o programa que executa esta tradução chama-se **compilador** ou **tradutor**;

- **INTERPRETAÇÃO** - você (ou qualquer utilizador do código) pode traduzir o source program cada vez que este tem de ser executado; o programa que executa este tipo de transformação chama-se **intérprete** ou **interpretador**, pois interpreta o código cada vez que se pretende executá-lo; também significa que não pode simplesmente distribuir o source code tal como está, porque o utilizador final também precisa do intérprete para o executar.

> 🍌 **Aprenda mais**: O interpretador converte para código de máquina, em tempo de execução. O compilador traduz o programa inteiro em código de máquina e o executa, gerando um arquivo que pode ser executado. O compilador gera um relatório de erros e o interpretador interrompe o processo na medida em que localiza um erro.

Devido a algumas razões muito fundamentais, uma linguagem de programação particular de alto nível foi concebida para se enquadrar numa destas duas categorias.

Há muito poucas linguagens que possam ser compiladas e interpretadas. Normalmente, uma linguagem de programação é projetada com este fator na mente dos seus construtores - será ela compilada ou interpretada?

Vamos assumir mais uma vez que escreveu um programa. Agora, existe como um **ficheiro de computador** (computer file): um programa de computador é na realidade um pedaço de texto, por isso o source code é normalmente colocado em **ficheiros de texto** (text files).

> 🙉 **Nota**: tem de ser **texto puro**, sem quaisquer decorações como diferentes fontes, cores, imagens embutidas ou outros suportes. Agora tem de invocar o intérprete e deixá-lo ler o seu source file.

O intérprete lê o source code de uma forma que é comum na cultura ocidental: de cima para baixo e da esquerda para a direita, porém há algumas exceções.

Em primeiro lugar, o intérprete verifica se todas as linhas subsequentes estão corretas (utilizando os quatro aspetos abordados anteriormente). Se o compilador encontrar um erro, termina o seu trabalho imediatamente. O único resultado, neste caso, é uma **mensagem de erro**.

O intérprete informá-lo-á onde se encontra o erro e o que o causou. No entanto, estas mensagens podem ser enganadoras, uma vez que o intérprete não é capaz de seguir exatamente as suas intenções, e pode detectar erros a alguma distância das suas verdadeiras causas.

Por exemplo, se tentar utilizar uma entidade com um nome desconhecido, causará um erro, mas o erro será descoberto no local onde tenta utilizar a entidade, e não onde o nome da nova entidade foi introduzido.

<img src="https://user-images.githubusercontent.com/61624336/194624188-26a61771-a2b5-4908-9307-0ef35bdcad68.png" align="right" height="177" title="Diagrama de funcionamento de um interpretador">

Por outras palavras, a razão real está normalmente localizada um pouco mais cedo no código, por exemplo, no local onde teve de informar o intérprete de que ia utilizar a entidade do nome.

Se a linha parecer boa, o intérprete tenta executá-la (nota: cada linha é normalmente executada separadamente, pelo que o trio "read-check-execute" pode ser repetido muitas vezes - mais vezes do que o número real de linhas no source file, uma vez que algumas partes do código podem ser executadas mais de uma vez).

É também possível que uma parte significativa do código possa ser executada com sucesso antes de o intérprete encontrar um erro. Este é um comportamento normal neste modelo de execução.

Pode perguntar agora: o que é melhor? O modelo "compilador" ou o modelo "intérprete"? Não há uma resposta óbvia. Se houvesse, um destes modelos já teria deixado de existir há muito tempo. Ambos têm as suas vantagens e as suas desvantagens.

<div align="center">
<table>
  <tr>
    <th colspan="2">Vantagens</th>
  </tr>
  <tr>
    <td><b>COMPILAÇÃO</b></td>
    <td><b>INTERPRETAÇÃO</b></td>
  </tr>
  <tr>
    <td>A execução do código traduzido é geralmente mais rápida;</td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td>Apenas o utilizador tem de ter o compilador - o end-user (utilizador final) pode usar o código sem ele;</td>
    <td>Pode executar o código assim que o concluir - não há fases adicionais de tradução;</td>
  </tr>
  <tr>
    <td>O código traduzido é armazenado utilizando linguagem de máquina - como é muito difícil de entender, as suas próprias invenções e truques de programação provavelmente permanecerão segredo.</td>
    <td>o código é armazenado usando linguagem de programação, não de máquina - isto significa que pode ser executado em computadores utilizando diferentes linguagens de máquina; não se compila o código separadamente para cada arquitetura diferente.</td>
  </tr>
</table>
</div>

<div align="center">
<table>
  <tr>
    <th colspan="2">Desvantagens</th>
  </tr>
  <tr>
    <td><b>COMPILAÇÃO</b></td>
    <td><b>INTERPRETAÇÃO</b></td>
  </tr>
  <tr>
    <td>A compilação em si pode ser um processo muito demorado - pode não ser capaz de executar o seu código imediatamente após qualquer alteração;</td>
    <td>Não espere que a interpretação aumente o seu código para alta velocidade - o seu código irá partilhar o poder do computador com o intérprete, pelo que não pode ser realmente rápido;
</td>
  </tr>
  <tr>
    <td>Tem de ter tantos compiladores quanto plataformas de hardware em que queira que o seu código seja executado.</td>
    <td>Tanto você como o end-user têm de ter o intérprete para executar o seu código.</td>
  </tr>
</table>
</div>

Hoje em dia, o desenvolvimento de sistemas se baseia em vários e diferentes paradigmas, tais como os listados a seguir:

- **Imperativo (Procedural)**: Segue sequências de comandos ordenados segundo uma lógica.
- **Funcional**: Trabalha com a divisão de problemas através de funções, que resolvem separadamente problemas menores e que, ao serem organizados, resolvem o problema como um todo.
- **Lógico**: Voltado ao desenvolvimento de problemas de lógica e usado em sistemas de inteligência computacional.
- **Orientado a Objetos (OO)**: Define um conjunto de classes para dividir o problema e realiza a interação entre as diferentes classes para também resolver o problema como um todo.

# 🧍 Sistemas Híbridos
O **processo híbrido** de implementação de uma linguagem de programação combina a execução rápida dos tradutores (compiladores) com a portabilidade dos interpretadores. O segredo é a geração de um código intermediário mais facilmente interpretável, porém não preso a uma plataforma (SO/Hardware).

Esse código intermediário não é específico para uma plataforma, possibilitando aos programas já compilados para esse código serem portados em diferentes plataformas, sem alterar e nem fazer nada. Para cada plataforma desejada devemos ter um interpretador desse código.

<blockquote>Duas importantes linguagens implementaram essa solução, com diferentes formas usando máquinas virtuais: <b>Python</b> e <b>Java</b>.</blockquote>

# 🐍 The History of Python language
<div align="center">

| [<img src="https://avatars.githubusercontent.com/u/2894642?v=4" width="177"><br><sub>Guido Van Rossum</sub>](https://github.com/gvanrossum) 
|:-:|
 
</div>

A linguagem Python surgiu em 1989, criado por <a href="https://github.com/gvanrossum">Guido Van Rossum</a>, nascido em 1956 em Haarlem, Holanda. O desenvolvimento da linguagem foi como um hobby onde a ideia era dar continuidade a linguagem ABC que era desenvolvida no Centro de Pesquisa Holandês (CWI) chamado Centrum Voor Wiskunde en Informatica, em Amsterdã, na Holanda no ano de 1980. 

As circunstâncias em que o Python foi criado são um pouco confusas. De acordo com Guido van Rossum:

<img height="177" src="https://user-images.githubusercontent.com/61624336/193808960-f34bbd86-45e8-4208-955e-f0bfecbeebf1.jpg" align="right"/>

> Em Dezembro de 1989, estava à procura de um projeto de programação de "hobby" que me mantivesse ocupado durante a semana por volta do Natal. O meu escritório (...) estaria fechado, mas eu tinha um computador em casa, e não tinha muito mais nas mãos. Decidi escrever um intérprete para a nova linguagem de escrita em que tinha pensado ultimamente: um descendente do ABC que apelaria aos hackers Unix/C. Escolhi Python como título de trabalho para o projeto, estando de humor ligeiramente irreverente (e sendo um grande fã do Monty Python's Flying Circus). - Guido van Rossum

> **Curiosidade**: A origem do nome foi inspirado na comédia televisiva inglesa da BBC chamada "Monty Python and the Flying Circus", na década de 1970. A logo de uma serpente da espécie python surgiu após a publicação do livro "" e após isso foi aderida pelo fundador.
  
Uma das características espantosas de Python é o fato de ser realmente o trabalho de uma pessoa. Normalmente, novas linguagens de programação são desenvolvidas e publicadas por grandes empresas que empregam muitos profissionais, e devido às regras de direitos de autor, é muito difícil nomear qualquer uma das pessoas envolvidas no projeto. O Python é uma exceção e, portanto, é claro que Guido van Rossum não desenvolveu e evoluiu ele próprio todos os componentes de Python. 
  
A rapidez com que o Python se espalhou pelo mundo é o resultado do trabalho contínuo de milhares (muitas vezes anônimos) de programadores, testadores, utilizadores (muitos deles não são especialistas em IT) e entusiastas, mas deve dizer-se que a primeira ideia (a semente da qual o Python brotou) chegou a uma cabeça - a de Guido.
 
Em 1999, Guido van Rossum definiu os seus objetivos para o Python, cujo foi influenciada por ABC que era uma linguagem pensada para iniciantes devido a sua facilidade de aprendizado e utilização, são eles: 
 
- Uma **linguagem fácil e intuitiva**, tão poderosa como a dos principais concorrentes;
- Código aberto, **open source**, para que todos possam contribuir;
- Código que seja tão **compreensível e inteligível** como o idioma inglês simples;
- **Adequado a tarefas diárias**, e produtiva, permitindo tempos de desenvolvimento curtos.

> Cerca de 20 anos mais tarde, é evidente que todas estas intenções foram cumpridas. Algumas fontes dizem que o Python é a linguagem de programação mais popular no mundo, enquanto outras afirmam que é a terceira ou a quinta.

Seja como for, continua a ocupar uma posição elevada no top dez do <a href="https://pypl.github.io/PYPL.html">PYPL PopularitY of Programming Language</a> e no <a href="https://www.tiobe.com/tiobe-index/">TIOBE Programming Community Index</a>.

O Python não é uma linguagem jovem. É **madura** e **confiável**. Não é uma *one-hit wonder*. É uma estrela brilhante no firmamento da programação, e o tempo gasto a aprender Python é um investimento muito bom.

Como é que os programadores, jovens e velhos, experientes e novatos, querem utilizá-lo? Como aconteceu que grandes empresas adotassem o Python e implementassem os seus principais produtos utilizando-o?

Há muitas razões - já enumerámos algumas delas, mas vamos enumerá-las novamente de uma forma mais prática:

- **é fácil de aprender** - o tempo necessário para aprender Python é menor do que para muitas outras linguagens; isto significa que é possível iniciar a programação em si mais rapidamente;
- **é fácil de ensinar** - a carga de trabalho de ensino é menor do que a necessária para outras linguagens; isto significa que o professor pode colocar mais ênfase em técnicas de programação gerais (independentes da linguagem), não desperdiçando energia em truques exóticos, estranhas exceções e regras incompreensíveis;
- é **fácil de usar** para escrever novo software - é muitas vezes possível escrever código mais rapidamente quando se usa Python;
- é **fácil de compreender** - é também frequentemente mais fácil e rápido de compreender o código de outra pessoa se for escrito em Python;
- é **fácil de obter, instalar e implementar** - o Python é gratuito, aberto e multiplataforma; nem todas as linguagens se podem gabar disso.

É claro que o Python também tem os seus inconvenientes (ninguém é perfeito hehe):

- **não tem um super-poder da velocidade** - o Python não oferece um desempenho excecional;
- em alguns casos pode ser resistente a algumas técnicas de teste mais simples - isto pode significar que **depurar (debuggar) o código Python pode ser mais difícil do que com outras linguagens**; felizmente, cometer erros é sempre mais difícil em Python.

Apesar da popularidade crescente de Python, ainda existem alguns nichos onde o Python está ausente, ou raramente é visto:

- **programação de baixo nível** (por vezes chamada programação "close to metal"): se quiser implementar um condutor ou motor gráfico extremamente eficaz, não utilizaria Python;
- **aplicações para dispositivos móveis**: existe pouca área de atuação para o Python nessa área, fortalecendo assim algumas das linguagens concorrentes.

Deve também ser afirmado que o Python não é a única solução do seu gênero disponível no mercado do TI. Tem muitos seguidores, mas há muitos que preferem outras linguagens e nem sequer consideram o Python para os seus projetos.
 
No início dos anos 1990 e desde então tem aumentado sua participação no mundo da programação. Permite uma programação fácil e clara para escalas pequenas e grandes, além de enfatizar a legibilidade eficiente do código, notadamente usando espaços em branco significativos.
 
Dentre as diversas linguagens de programação que existem, **Python** é considerada uma das principais. Por sua simplicidade de aprendizado, ela tem sido utilizada em diversos cursos universitários como a primeira linguagem com que os alunos têm contato ao programar. Atualmente, conta com ampla participação da comunidade, além de ter seu desenvolvimento aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation.

Recentemente, a _IEEE Computer Society_ classificou-a como a linguagem mais indicada para aprender em 2020. Isso se deve à sua eficiência no desenvolvimento de **machine learning**, **inteligência artificial**, **ciência**, **gestão** e **análise de dados**.

**Python** é uma linguagem de programação de alto nível, que permite ao programador utilizar instruções de forma intuitiva, tornando seu aprendizado mais simples do que o aprendizado de uma linguagem de baixo nível.

Nas linguagens de baixo nível, o programador precisa se expressar de forma muito mais próxima do que o dispositivo “entende”, levando naturalmente a um distanciamento da linguagem utilizada para comunicação entre duas pessoas.

A classificação das linguagens em paradigmas permite que entendamos qual é o melhor deles para solucionar determinado problema e, a partir daí, escolher a linguagem de programação (pertencente a esse paradigma) mais adequada, conforme características e especificidades do contexto em que se aplica o problema.

A linguagem Python foi escolhida como instrumento para o desenvolvimento desta disciplina, pois além de ser multiparadigma (possibilita escrever programas em diferentes paradigmas) e de uso geral, vem se destacando e sendo cada vez mais utilizada entre os novos desenvolvedores por vários motivos:

- Facilidade de aprendizado;
- Boa legibilidade de código;
- Boa facilidade de escrita;
- Produtividade e confiabilidade.
- Possui, ainda, comunidade de desenvolvedores crescente e vasta biblioteca, repleta de funções, aplicada a diversas áreas da ciência, assim como o crescente números de frameworks desenvolvidos para a linguagem.
 
## Características da Linguagem Python
A linguagem **Python** é uma linguagem de programação, com características interessantes:

  - É **interpretada** e **compilada**, ou seja, o interpretador Python executa o código fonte diretamente, traduzindo cada trecho para instruções de máquina;
  - É de **alto nível**, ou seja, o interpretador se vira com detalhes técnicos do computador. Assim, desenvolver um código mais simples do que em linguagem de baixo nível, nas quais o programador deve se preocupar com detalhes da máquina;
  - É de propósito geral, ou seja, podemos usar Python para desenvolver programas em diversas áreas. Ao contrário de linguagens de domínio específico, que são especializados e atendem somente a uma aplicação específica;
  - Tem **tipos dinâmicos**, ou seja, o interpretador faz a magia de descobrir o que é cada variável;
  - É **multiparadigma**, apesar de suportar perfeitamente o paradigma de programação estruturada, Python também suporta programação orientada a objetos, tem características do paradigma funcional, com o amplo uso de bibliotecas, assim como permite recursividade e uso de funções anônimas.
  - É **interativa**, permite que os usuários interajam com o interpretador Python diretamente para escrever os programas, utilizando o prompt interativo. Esse prompt fornece mensagens detalhadas para qualquer tipo de erro ou para qualquer comando específico em execução, suporta testes interativos e depuração de trechos de código.
  - É **híbrida** quanto ao método de implementação. Python usa uma abordagem mista para explorar as vantagens do interpretador e do compilador. Assim como Java, utiliza o conceito de máquina virtual (PVM - Python Virtual Machine), permitindo a geração de um código intermediário, mais fácil de ser interpretado, mas que não é vinculado definitivamente a nenhum sistema operacional.
  - É **portável**, tem a capacidade de rodar em uma grande variedade de plataformas de hardware com a mesma interface. Ele roda perfeitamente em quase todos os sistemas operacionais, como **Windows**, **Linux**, **UNIX**, e **macOS**, sem nenhuma alteração.
  - É **extensível**, permite que os programadores adicionem ou criem módulos e pacotes de baixo nível / alto nível ao interpretador Python. Esses módulos e pacotes de ferramentas permitem que os desenvolvedores tenham possibilidades amplas de colaboração, contribuindo para a popularidade da linguagem.
  - **Suporta bancos de dados**, por ser uma linguagem de programação de uso geral, Python suporta os principais sistemas de bancos de dados. Permite escrever código com integração com **MySQL**, **PostgreSQL**, **SQLite**, **ElephantSQL**, **MongoDB**, entre outros.
  - **Suporta interface com usuário**, permite escrever código de tal maneira que uma interface do usuário para um aplicativo possa ser facilmente criada, importando bibliotecas como **Tkinter**, **Flexx**, **CEF Python**, **Dabo**, **Pyforms** ou **PyGUI wxPython**, **PyQT**, **Kivy**.
  - Pode ser usado como **linguagem de script**. Permite fácil acesso a outros programas, podendo ser compilado para **bytecode** a fim de criar aplicativos grandes.
  - Permite **desenvolvimento de aplicações Web**. Devido à escalabilidade já citada, Python oferece uma variedade de opções para o desenvolvimento de aplicativos Web. A biblioteca padrão do Python incorpora muitos protocolos para o desenvolvimento da web, como **HTML**, **XML**, **JSON**, **processamento de e-mail**, além de fornecer base para **FTP**, **IMAP** e outros **protocolos da Internet**.
  - Permite criação de **aplicações comerciais**. É desenvolvido sob uma licença de código aberto aprovada pela **OSI**, tornando-o livremente utilizável e distribuível, mesmo para uso comercial.
 
### Resumindo as características do Python
- Orientada a objetos com uma semântica dinâmica;
- Possui licença compatível com Software livre;
- Linguagem de altíssimo nível (VHLL);
- Tipagem dinâmica e forte;
- Aumenta a produtividade do desenvolvedor;
- A implementação padrão e oficial de referência do Python que é mantida pela PSF (Python Software Foundation) e é escrita em linguagem C, e por isso, é também conhecida como CPython;
- Multiplataforma e multiparadigma (POO, funcional e procedural);
- Batteries Included: é uma biblioteca padrão rica e versátil que está imediatamente disponível, sem que o usuário baixe pacotes separados. Isso dá à linguagem Python uma vantagem inicial em muitos projetos.;
- Organizada;
- Comunidade gigante e ativa;
- Curva de aprendizado baixa;
- Muitas Bibliotecas.

Por essas e várias outras características, o Python se torna uma linguagem simples, bela, legível e amigável. É uma linguagem muito utilizada por diversas empresas como Wikipédia, Microsoft, Google, Yahoo!, CERN, NASA, Facebook, AMAZON, Instagram, Spotify, Bitorrent Inc, Django e Dropbox.

### Principais áreas de atuação com a linguagem Python
Vemo-lo todos os dias e em quase todo o lado. É utilizado extensivamente para implementar **serviços complexos da Internet** como motores de busca, armazenamento em nuvem e ferramentas, redes sociais, etc. Sempre que utiliza qualquer um destes serviços, está na realidade muito próximo de Python, embora não o conheça.

Muitas ferramentas em desenvolvimento são implementadas em Python. Cada vez mais aplicações de uso diário estão a ser escritas em Python. Muitos cientistas abandonaram ferramentas proprietárias dispendiosas e mudaram para o Python. Muitos testadores de projetos de TI começaram a utilizar o Python para realizar procedimentos de teste repetíveis. A lista é longa:

<li>IA - Inteligência Artificial</li>
<li>Machine Learning</li>
<li>Deep Learning</li>
<li>IoT - Internet das Coisas</li>
<li>Big Data</li>
<li>Data Analysis</li>
<li>Data Science</li>
<li>Computação 3D</li>
<li>Biotecnologia</li>
<li>Bioinformática</li>
<li>Web Development (Back-end)</li>
<li>Cybersecurity</li>
<li>Game Development</li>
<li>Mobile Development</li>
<li>Desktop Development</li>
<li>DevOps</li>
<li>Automação de Sistemas</li>
<li>Cloud Computing</li>
<li>Estudos científicos como: Engenharia, Geologia, Astronomia, Física, Química, Matemática e etc</li>

## Rivais do Python? ![Ruby](https://img.shields.io/badge/ruby-%23CC342D.svg?style=for-the-badge&logo=ruby&logoColor=white) ![Perl](https://img.shields.io/badge/Perl-39457E?style=for-the-badge&logo=Perl&logoColor=white)
O Python tem dois concorrentes diretos, com propriedades e predisposições comparáveis. Estes são:

- **Perl** - uma linguagem de scripting originalmente de autoria de Larry Wall;
- **Ruby** - uma linguagem de scripting originalmente escrita por Yukihiro Matsumoto.

A primeira é mais tradicional, mais conservadora do que Python, e assemelha-se a algumas das boas e antigas linguagens derivadas da clássica linguagem de programação C.

Em contraste, esta última é mais inovadora e mais cheia de ideias frescas do que Python. O próprio Python encontra-se algures entre estas duas criações.

A Internet está cheia de fóruns com infinitas discussões sobre a superioridade de um destes três sobre os outros, caso pretenda saber mais sobre cada um deles.

## Certificações em Python
![3b74900cebc980b0fa8bcf4bb86c85488d6987c8](https://user-images.githubusercontent.com/61624336/194156459-aa30790d-bcb5-4966-af03-d2fb3acaa607.png)

- https://pythoninstitute.org/pcep
- https://pythoninstitute.org/pcap

### Cursos que oferecem certificações
- https://pythoninstitute.org/

## Há mais de um Python
Existem dois tipos principais de Python, chamados **Python 2** e **Python 3**.

O **Python 2** é uma versão mais antiga do Python original. Desde então o seu desenvolvimento tem sido intencionalmente parado, embora isso não signifique que não hajam atualizações. Pelo contrário, as atualizações são emitidas regularmente, mas não se destinam a modificar a linguagem de forma significativa. Preferem corrigir quaisquer bugs recém-descobertos e falhas de segurança. O caminho de desenvolvimento de Python 2 já chegou a um beco sem saída, mas o Python 2 em si ainda está muito vivo, presente principalmente em sistemas operacionais Linux e macOS.

<div align="center"><img src="https://cdn.worldvectorlogo.com/logos/python-5.svg" height="177"></div><br \>

Em 2008, é lançada a versão 3.0, que resolveu muitos problemas de design da linguagem e melhorou a performance. Algumas mudanças foram muito profundas dessa forma a versão 3.x não é retrocompatível.

O **Python 3** é a versão mais recente (para ser mais preciso, a atual versão) da linguagem. Está a percorrer o seu próprio caminho de evolução, criando os seus próprios padrões e hábitos. Atualmente, estamos na versão <b><a href="https://www.python.org/downloads/">3.10.8</a></b> do Python.

Estas duas versões do Python não são compatíveis uma com a outra. Os **scripts** (Arquivos de texto que contém instruções que constituem um programa de Python) de Python 2 não serão executados num ambiente Python 3 e vice-versa, portanto, se quiser que o antigo código Python 2 seja executado por um interpretador Python 3, a única solução possível é reescrevê-lo, não do zero, claro, pois grandes partes do código podem permanecer intocadas, mas terá de rever todo o código para encontrar todas as incompatibilidades possíveis. Infelizmente, este processo não pode ser totalmente automatizado.

É demasiado difícil, demasiado demorado, demasiado caro e demasiado arriscado migrar uma velha aplicação Python 2 para uma nova plataforma. É possível que a reescrita do código lhe introduza novos bugs. É mais fácil e mais sensato deixar estes sistemas em paz e melhorar o intérprete existente, em vez de tentar trabalhar dentro do source code já em funcionamento.

O Python 3 não é apenas uma versão melhor do Python 2 - é uma linguagem completamente diferente, embora seja muito semelhante à sua predecessora. Quando se olha para eles à distância, parecem ser os mesmos, mas quando se olha de perto, no entanto, notam-se muitas diferenças.

Se estiver a modificar uma antiga solução Python existente, então é altamente provável que tenha sido codificada em Python 2. Esta é a razão pela qual o Python 2 ainda está a ser utilizado. Há demasiadas aplicações Python 2 existentes para o descartar completamente.

> 🐍 **Nota**: Se vai iniciar um novo projeto Python, deve usar Python 3.

É importante lembrar que pode haver diferenças menores ou maiores entre as versões posteriores do Python 3 (por exemplo, Python 3.6 introduziu chaves de dicionário ordenadas por defeito sob a implementação do CPython) - a boa notícia, porém, é que todas as versões mais recentes de Python 3 são retrocompatíveis com as versões anteriores de Python 3. Sempre que for significativo e importante, tentaremos realçar essas diferenças.

> Todas as amostras de código que irá encontrar aqui foram testadas com Python 3.4, Python 3.6, Python 3.7, e Python 3.8.

## Python aka CPython
<div align="center"><img src="https://user-images.githubusercontent.com/61624336/195659984-b7d1a71e-2c54-4c9d-89d3-70b5a5e65f89.svg" height="177"></div><br />

Além do Python 2 e Python 3, existe mais de uma versão de cada uma.

Em primeiro lugar, existem os Pythons que são mantidos pelas pessoas reunidas em torno da PSF (<a href="https://www.python.org/psf-landing/">Python Software Foundation</a>), uma comunidade que visa desenvolver, melhorar, expandir e popularizar o Python e o seu ambiente. O presidente da PSF é o próprio Guido von Rossum, e por esta razão, estes Pythons são chamados de canônicos. São também considerados **Pythons de referência**, pois qualquer outra implementação da linguagem deve seguir todas as normas estabelecidas pelo PSF.

<img src="https://user-images.githubusercontent.com/61624336/136308856-241076e0-15b9-475d-a561-016c75fd2731.png" height="177" align="right">

Guido van Rossum utilizou a **linguagem de programação C** para implementar a primeira versão da sua linguagem, e esta decisão ainda está em vigor. Todos os Pythons provenientes do PSF são escritos na linguagem C. Há muitas razões para esta abordagem e ela tem muitas consequências. Uma delas (provavelmente a mais importante) é que graças a ela, o Python pode ser facilmente portado e migrado para todas as plataformas com a capacidade de compilar e executar programas em linguagem C (praticamente todas as plataformas têm esta característica, o que abre muitas oportunidades de expansão para Python).

É por isso que a implementação da PSF é frequentemente referida como **CPython**. Este é o Python mais influente entre todos os Pythons do mundo.

O CPython é uma **implementação** da linguagem Python, um pacote com um compilador e um interpretador Python (Máquina Virtual Python - PVM), além de outras ferramentas para programar em Python.

## Cython
<div align="center"><img src="https://upload.wikimedia.org/wikipedia/en/c/ce/Cython-logo.svg" height="177"></div><br \>

Outro membro da família Python é o **Cython** que é  uma das várias soluções possíveis para a mais dolorosa das características de Python - **a falta de eficiência**. Grandes e complexos cálculos matemáticos podem ser facilmente codificados em Python (muito mais facilmente do que em C ou qualquer outra linguagem tradicional), mas a execução do código resultante pode ser extremamente demorada.

Como são conciliadas estas duas contradições? Uma solução é escrever as suas ideias matemáticas usando Python, e quando estiver absolutamente seguro de que o seu código está correto e produz resultados válidos, pode traduzi-lo para C. Certamente, o C correrá muito mais rápido do que Python puro.

É isto que o Cython pretende fazer - traduzir automaticamente o código Python (limpo e claro, mas não demasiado rápido) em código C (complicado e falador, mas ágil).

## Jython 
<div align="center">

<a href="https://www.jython.org"><img src="https://user-images.githubusercontent.com/61624336/169595807-6c1e4c7c-a063-46df-a9e9-fd013a2ce598.svg" height="177"></a>
  
</div><br />

Outra versão do Python é chamada **Jython**, o “J” é para “Java”. Imagine um Python escrito em Java em vez de C. Isto é útil, por exemplo, se desenvolver sistemas grandes e complexos escritos inteiramente em Java, e quiser acrescentar alguma flexibilidade Python a eles. O CPython tradicional pode ser difícil de integrar em tal ambiente, já que C e Java vivem em mundos completamente diferentes e não partilham muitas ideias comuns.

Jython pode comunicar com a infra-estrutura Java existente de forma mais eficaz. É por isso que alguns projetos o consideram utilizável e necessário.

> 🐍 **Nota**: A atual implementação do Jython segue as normas do Python 2. Até ao momento, não há Jython em conformidade com Python 3.

> 🐍 **Curiosidade**: Curioso saber que o código Python pode ser traduzido em <b>Bytecode Java</b> usando a implementação **Jython** para rodar aplicações Java e na JVM - Java Virtual Machine.

## PyPy e RPython
<div align="center">

<a href="https://www.pypy.org"><img src="https://www.pypy.org/images/pypy-logo.svg" height="177"></a>

</div><br />

Dê uma vista de olhos ao logotipo acima. É um rébus. Consegue resolvê-lo? É um logótipo do **PyPy** - *um Python dentro de um Python*. Por outras palavras, representa um ambiente Python escrito em linguagem Python, chamado **RPython** (Restricted Python). Na verdade, é um subconjunto de Python.

O source code de PyPy não é executado na forma de interpretação, mas sim traduzido para a linguagem de programação C e depois executado separadamente.

Isto é útil porque se quiser testar qualquer nova funcionalidade que possa ser (mas não tem de ser) introduzida na implementação do Python convencional, é mais fácil verificá-la com o PyPy do que com o CPython. É por isto que o PyPy é antes uma ferramenta para pessoas que desenvolvem Python, do que para o resto dos utilizadores.

Isto não torna o PyPy menos importante ou menos sério do que o CPython, é claro.

Além disso, o PyPy é compatível com a linguagem do Python 3.

Existem muitos mais Pythons diferentes no mundo. Encontrá-los-á se procurar, vamos nos concentrar no CPython.

# 🏗️ Sistema de implementação do Python
<div align="center"><a href="https://www.jython.org/"><img src="https://media.geeksforgeeks.org/wp-content/uploads/python_working.png"></a></div>

**Python** usa um sistema híbrido, uma combinação de interpretador e tradutor (compilador). O **compilador** converte o código-fonte Python em um código intermediário, que roda numa máquina virtual, a **PVM** (Python Virtual Machine).

O Python é uma linguagem interpretada. Isto significa que herda todas as vantagens e desvantagens descritas. Naturalmente, acrescenta algumas das suas características únicas a ambos os conjuntos.
Se quiser programar em Python, precisará do intérprete Python. Não será capaz de executar o seu código sem ele. Felizmente, o Python é gratuito. Esta é uma das suas vantagens mais importantes.
Devido a razões históricas, as linguagens concebidas para serem utilizadas na forma de interpretação são muitas vezes chamadas linguagens de scripting, enquanto os source programs codificados que as utilizam são chamados scripts.

## VirtualEnv em Python
O **virtualenv** do Python é utilizado para isola a versão do Python e das bibliotecas usadas em um determinado sistema. Caso você não utilize o virtualenv, todas as bibliotecas necessárias para seu sistema seriam instaladas no ambiente do sistema operacional.

# 🐍 Como obter o Python e como conseguir utilizá-lo
![cf12a9b584a5bc7ca191bbecbe0741151ae6ebfb](https://user-images.githubusercontent.com/61624336/195671940-1ad2730d-8a30-403c-b8ce-8b899af97969.png)

Existem várias maneiras de obter a sua própria cópia do Python 3, dependendo do sistema operativo que utilize.

> 🐧 Utilizadores de **Linux** provavelmente já têm o Python instalado - este é o cenário mais provável, já que a infraestrutura do Python é intensamente utilizada por muitos componentes do sistema operativo Linux. Por exemplo, alguns distribuidores podem acoplar as suas ferramentas específicas ao sistema e muitas destas ferramentas, como gestores de pacotes, são frequentemente escritas em Python. Algumas partes de ambientes gráficos disponíveis no mundo Linux também podem utilizar o Python.

Se for um utilizador Linux, abra o terminal/console e digite:

[![bash](https://img.shields.io/badge/-bash-4EAA25?style=social&logo=GNU-Bash&logoColor=000000)](#)

```sh
python3
```

no shell prompt, pressione Enter e aguarde. Se vir algo deste gênero:

<pre>
Python 3.4.5 (default, Jan 12 2017, 02:28:40)
[GCC 4.2.1 Compatible Clang 3.7.1 (tags/RELEASE_371/final)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
</pre>

<img src="https://user-images.githubusercontent.com/61624336/195667351-1b9ecde5-fc3b-4287-b69e-6bd829fe9c27.png" width="377" align="right">

Se o Python 3 estiver ausente, consulte a sua documentação do Linux para saber como utilizar o seu gestor de pacotes para descarregar e instalar um novo pacote - o que precisa chama-se python3, ou o seu nome começa com isso.

> 🪟🍎 Todos os utilizadores que não sejam Linux podem descarregar uma cópia em: https://www.python.org/downloads/.

> 🐍 **Nota**: Por padrão, a versão do Python 2 já se encontra instalado nas máquinas do sistema operacional Linux e macOS.

Como o browser diz ao site onde entrou o sistema operativo que utiliza, o único passo que tem de dar é clicar na versão Python apropriada que deseja.

Neste caso, selecione Python 3. O site oferece sempre a versão mais recente do mesmo. Se for um utilizador do Windows, inicie o arquivo `.exe` descarregado e siga todos os passos.

> 🪟 **Windows Env**: Deixe as configurações padrão que o instalador sugere por agora, com uma exceção - veja a caixa de verificação chamada `Add Python 3.x to PATH` e verifique-a. Isto tornará as coisas mais fáceis, pois vai adicionar o caminho do python3 instalado na sua máquina local para as variáveis de ambiente do seu sistema operacional Windows.

Se for um utilizador MacOS, uma versão do Python 2 pode já ter sido pré-instalada no seu computador, mas como vamos trabalhar com o Python 3, ainda assim terá de descarregar e instalar o arquivo `.pkg` relevante a partir do site Python.

Agora que tem o Python 3 instalado, é altura de verificar se funciona, e fazer o primeiro uso do mesmo. Este será um procedimento muito simples, mas deve ser o suficiente para o convencer de que o ambiente Python é completo e funcional.

Existem muitas formas de utilizar o Python, especialmente se vier a ser um programador Python. Para começar o seu trabalho, precisa das seguintes ferramentas:

- um **editor** que o irá apoiar na escrita do código (deve ter algumas características especiais, não disponíveis em ferramentas simples); este editor dedicado dar-lhe-á mais do que o equipamento padrão do sistema operativo;
- uma **console** na qual pode rodar o seu código recém-escrito e pará-lo à força quando ficar fora de controle;
- uma ferramenta chamada de **debugger**, capaz de rodar o seu código passo a passo e que lhe permite inspecioná-lo em cada momento da execução.

Para além dos seus muitos componentes úteis, a instalação padrão de Python 3 contém uma aplicação muito simples mas extremamente útil chamada **IDLE**.

Com o **IDLE** - Integrated Development and Learning Environment iniciado. Isto é o que deve ver:

![7d79de4a3439191bc815d1d0d51dd6e8bd08bcf0](https://user-images.githubusercontent.com/61624336/195676458-cce0c851-f6b2-4e47-b85e-ecde19d44357.png)

## Como escrever e executar o seu primeiro programa
É agora tempo de escrever e executar o seu primeiro programa de Python 3. Será muito simples, por agora.

O primeiro passo é criar um novo source file e preenchê-lo com código. Clique em `File` no menu do IDLE e escolha `New file`.

![9c47dcbd53615728044a921159aef565968d7f3c](https://user-images.githubusercontent.com/61624336/195677372-128a8986-dde7-4f69-983b-cd0bf0046f6a.png)

> Como pode ver, o IDLE abre uma nova janela para si. Pode utilizá-la para escrever e alterar o seu código.

Esta é a **janela do editor**. O seu único objetivo é ser um local de trabalho em que o seu source code é tratado. Não confundir a janela do editor com a janela shell. Desempenham funções diferentes.

A janela do editor está atualmente sem título, mas é uma boa prática começar a trabalhar nomeando o source file.

Clique em `File` (na nova janela), depois clique em `Save as...`, selecione uma pasta para o novo ficheiro (o ambiente de trabalho é um bom local para as suas primeiras tentativas de programação) e escolha um nome para o novo ficheiro.

![ed0d023d260245eecd1be0f4b0ff02fec660b9da](https://user-images.githubusercontent.com/61624336/195678750-3a44b5bd-0fd7-4a90-8c9b-bc7c35a482d3.png)

[![.py](https://img.shields.io/badge/-.py-fff?style=social&logo=Python&logoColor=3776AB)](#)

> 🐍 **Nota**: não defina nenhuma extensão para o nome do ficheiro que vai utilizar. O Python precisa que os seus ficheiros tenham a extensão `.py`, por isso deve confiar nas predefinições da janela de diálogo. A utilização da extensão padrão `.py` permite que o sistema operativo abra adequadamente estes ficheiros.

Agora coloque apenas uma linha na sua janela do editor recém-aberta e nomeada. A linha tem este aspeto:

[![.py](https://img.shields.io/badge/-snake.py-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
print("Hisssssss...")
```

> O comando `print()` , que é uma das diretivas mais fáceis em Python, imprime simplesmente uma linha para o ecrã.

Veja mais de perto as aspas. Estas são as formas mais simples de aspas (neutras, retas, mudas, etc.) tipicamente utilizadas nos source files. Não tente usar aspas tipográficas (curvas, curvilíneas, inteligentes, etc.), utilizadas por processadores de texto avançados, uma vez que o Python não as aceita.

![0830563fa18ea8138503c208eb9514af574d7a2c](https://user-images.githubusercontent.com/61624336/195683022-8105137e-d987-45f3-a003-407c320d1fa8.png)

Guarde o ficheiro `File > Save` e execute o programa `Run -> Run Module`.

Se tudo correr bem e não houver erros no código, a janela do console irá mostrar-lhe os efeitos causados pela execução do programa. Neste caso, o programa sibila. Tente executá-lo mais uma vez. E mais uma vez. Agora feche ambas as janelas e regresse ao ambiente de trabalho.

![0ced7f0e762ae8260831e994370b1ff2b8b7fd7b](https://user-images.githubusercontent.com/61624336/195683486-5c9343e2-37ab-48dd-a3af-32fe8d7c5905.png)

## Como estragar e corrigir o seu código
Agora reinicie o IDLE. Clique em `File > Open > aponte para o ficheiro que guardou anteriormente e deixe o IDLE lê-lo`.

Tente executá-lo novamente pressionando `F5` quando a janela do editor estiver ativa. Como pode ver, o IDLE é capaz de guardar o seu código e recuperá-lo quando precisar dele novamente.

O IDLE contém um recurso adicional e útil.

1. Primeiro, remova o parêntesis final.
2. Em seguida, insira o parêntesis novamente.

O seu código deve parecer-se com o que está aqui em baixo:

[![.py](https://img.shields.io/badge/-snake.py_(output)-fff?style=social&logo=Python&logoColor=3776AB)](#)

<pre>Hisssssss...</pre>

![ed47c4a8c77b4dd27800cb500f5f412c1fcb12fd](https://user-images.githubusercontent.com/61624336/195691376-2ca185ce-87f3-4b37-ab0d-304df28154d3.png)

Cada vez que colocar o parêntesis final no seu programa, o IDLE mostrará a parte do texto limitada com um par de parêntesis correspondentes. Isto ajuda-o a lembrar-se de os colocar em pares.

Retire novamente o parêntesis final. O código torna-se incorreto. Contém agora um erro de sintaxe. O IDLE não deve deixar que o execute.

Tente executar o programa novamente. O IDLE irá lembrá-lo de guardar o ficheiro modificado. Siga as instruções.

Observe cuidadosamente todas as janelas. Uma nova janela – diz que o intérprete encontrou um EOF (end-of-file) embora (na sua opinião) o código deva conter mais algum texto.

A janela do editor mostra claramente onde isto aconteceu.

![112b321a4d7620c67b0e037f8861fd71a9cb09df](https://user-images.githubusercontent.com/61624336/195692443-b541e9c2-702c-4e28-89c7-5ceb1b6d22ae.png)

Corrija o código agora. Deve ficar assim:

[![.py](https://img.shields.io/badge/-snake.py-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
print("Hisssssss...")
```

Execute-o para ver se “sibila” novamente.

Vamos estragar o código mais uma vez. Remova uma letra da palavra `print`. Execute o código pressionando `F5`. O que acontece agora?

![aa281b654b986dbe066685abaa0dcf8a3b842705](https://user-images.githubusercontent.com/61624336/195692660-b70902e1-f4c6-4990-a179-e6c6c8147312.png)

Deve ter notado que a mensagem de erro gerada para o erro anterior é bastante diferente da primeira.

![9e63a9fdc2ed8afae211381c57ccd02967eb4ebc](https://user-images.githubusercontent.com/61624336/195699490-9083ed72-8712-4793-ab8b-8092671ad63b.png)

Isto acontece porque a natureza do erro é diferente e o erro é descoberto numa fase diferente de interpretação.

A janela do editor não fornecerá qualquer informação útil sobre o erro, mas as janelas da console poderão.

A mensagem (a vermelho) mostra (nas linhas subsequentes):

- o **traceback** (que é o caminho que o código percorre através de diferentes partes do programa - pode ignorá-lo por agora, uma vez que está vazio num código tão simples);
- a **localização do erro** (o nome do ficheiro contendo o erro, o número da linha e o nome do módulo); 

> 🐍 **Nota**: o número pode ser enganador, uma vez que o Python normalmente mostra o local onde primeiro se notam os efeitos do erro, não necessariamente o erro em si.

- o **conteúdo da linha errada**; 

> 🐍 **Nota**: a janela do editor IDLE não mostra os números das linhas, mas mostra a localização atual do cursor no canto inferior direito; use-a para localizar a linha errada num source code longo;

- o **nome do erro** e uma breve explicação.

> Experimente criar novos ficheiros e executar o seu código. Tente fazer output de uma mensagem diferente para o ecrã, por exemplo `roar!`, `meow`, ou até mesmo talvez um `oink!`. Tente estragar e corrigir o seu código - veja o que acontece.

Ao retirar as aspas do argumento da `string` também é gerado um erro. Veja mais:

[![.py](https://img.shields.io/badge/-snake.py_input-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
print(Hisssssss...)
```
[![.py](https://img.shields.io/badge/-snake.py_output-fff?style=social&logo=Python&logoColor=3776AB)](#)

<pre>
Traceback (most recent call last):
  File "snake.py", line 1, in <module>
    print(Hisssssss...)
NameError: name 'Hisssssss...' is not defined
</pre>

Agora, ao retirar os parênteses da função com o argumento `string` também é gerado um erro. Veja mais:

[![.py](https://img.shields.io/badge/-snake.py_input-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
printHisssssss...
```
[![.py](https://img.shields.io/badge/-snake.py_output-fff?style=social&logo=Python&logoColor=3776AB)](#)

<pre>
Traceback (most recent call last):
  File "snake.py", line 1, in <module>
    printHisssssss...
NameError: name 'printHisssssss...' is not defined
</pre>

Agora, veja o que acontece ao colocar aspas duplas sem parênteses:

[![.py](https://img.shields.io/badge/-snake.py_input-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
print"Hisssssss..."
```
[![.py](https://img.shields.io/badge/-snake.py_output-fff?style=social&logo=Python&logoColor=3776AB)](#)

<pre>
  File "snake.py", line 1
    print"Hisssssss..."
               ^
SyntaxError: invalid syntax
</pre>

Agora, veja o que acontece ao colocar duas aspas distintas sem parênteses:

[![.py](https://img.shields.io/badge/-snake.py_input-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
print'Hisssssss..."
```
[![.py](https://img.shields.io/badge/-snake.py_output-fff?style=social&logo=Python&logoColor=3776AB)](#)

<pre>
 File "snake.py", line 1
    print'Hisssssss..."
               ^
SyntaxError: EOL while scanning string literal
</pre>

Agora, veja o que acontece ao colocar duas aspas simples ou duplas sem parênteses e com um sinal de igual:

[![.py](https://img.shields.io/badge/-snake.py_input-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
print='Hisssssss...'
```
[![.py](https://img.shields.io/badge/-snake.py_output-fff?style=social&logo=Python&logoColor=3776AB)](#)

<pre>
Success (1.82s)
</pre>

> Ele compila, mas não exibe resultado! Pois ele identificou como uma **variável** armazenando um valor, mas se exibirmos essa variável vai existir um erro de tipo.

# 🐍 `Hello, World!` - Linguagem Python
<div align="center"><img src="https://user-images.githubusercontent.com/61624336/196500926-929266b8-ee05-402c-91f0-4f3cbbbf0f85.svg" height="177"></div><br />

É tempo de começar a escrever algum código Python real e funcional. Vai ser muito simples por enquanto.

Como vamos mostrar-lhe alguns conceitos e termos fundamentais, estes snippets de código não serão sérios ou complexos.


[![.py](https://img.shields.io/badge/-helloWorld.py-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
print("Hello, World!")
```

Execute o código na janela do editor à direita. Se tudo correr bem aqui, verá a linha de texto na janela da console.

Em alternativa, lançe o IDLE, crie um novo source file Python, preencha-o com este código, nomeie o ficheiro e guarde-o. Agora execute-o. Se tudo correr bem, verá o texto contido dentro das aspas na janela da console IDLE. O código que executou deve parecer familiar. Viu algo muito semelhante quando o conduzimos através da criação do ambiente IDLE.

Agora vamos passar algum tempo a mostrar e a explicar-lhe o que está realmente a ver, e porque é que se parece com isto.

Como pode ver, o primeiro programa consiste nas seguintes partes:

- a palavra `print`;
- um parêntesis de abertura;
- umas aspas;
- uma linha de texto: `Hello, World!`;
- outras aspas;
- um parêntesis de fecho.

Cada um dos itens acima desempenha um papel muito importante no código.

## A função `print()`
Veja a linha de código abaixo:

[![.py](https://img.shields.io/badge/-helloWorld.py-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
print("Hello, World!")
```

A palavra `print` que se pode ver aqui é um **nome de função**. Isso não significa que, onde quer que a palavra apareça, é sempre um nome de função. O significado da palavra vem do contexto em que a palavra foi usada.

Provavelmente já encontrou o termo função muitas vezes antes, durante as aulas de matemática. Provavelmente também pode listar vários nomes de funções matemáticas, como seno ou log.

As funções Python, no entanto, são mais flexíveis e podem conter mais conteúdo do que as suas irmãs matemáticas.

Uma função (neste contexto) é uma parte separada do código do computador capaz de:

- **causar um qualquer efeito** (por exemplo, enviar texto para o terminal, criar um ficheiro, desenhar uma imagem, reproduzir um som, etc.); isto é algo completamente inédito no mundo da matemática;
- **avaliar um valor** (por exemplo, a raiz quadrada de um valor ou o comprimento de um dado texto) e **devolvê-lo como o resultado da função**; é isto que faz as funções Python serem os parentes dos conceitos matemáticos.

Além disso, muitas das funções Python podem fazer as duas coisas acima juntamente.

De onde vêm as funções?

- Podem vir **do próprio Python**; a função `print` é uma deste tipo; tal função é um valor acrescentado recebido juntamente com o Python e o seu ambiente (é **incorporada**); não é necessário fazer nada de especial (por exemplo, perguntar a alguém por qualquer coisa) se quiser fazer uso dela;
- podem ser provenientes de um ou mais dos add-ons de Python chamados **módulos**; alguns dos módulos vêm com Python, outros podem requerer instalação separada - seja qual for o caso, todos eles precisam de estar explicitamente ligados ao seu código (mostrar-lhe-emos como fazê-lo em breve);
- pode **escrevê-los você mesmo**, colocando tantas funções quantas quiser e precisar dentro do seu programa para o tornar mais simples, mais claro e mais elegante.

O nome da função deve ser **significativo** (o nome da função `print` é evidente por si mesmo).

Claro que, se vai fazer uso de qualquer função já existente, não tem influência no seu nome, mas quando começar a escrever as suas próprias funções, deve considerar cuidadosamente a sua escolha de nomes.

Como dissemos antes, uma função pode ter:

- um **efeito**;
- um **resultado**.

Há também uma terceira, muito importante, componente de função - o(s) **argumento(s)**.

As funções matemáticas normalmente aceitam um argumento, por exemplo, `sen(x)` toma um `x`, que é a medida de um ângulo.

As funções de Python, por outro lado, são mais versáteis. Dependendo das necessidades individuais, elas podem aceitar qualquer número de argumentos - tantos quantos forem necessários para desempenhar as suas tarefas. 

> 🐍 **Nota**: qualquer número inclui zero - algumas funções de Python não precisam de qualquer argumento.

[![.py](https://img.shields.io/badge/-helloWorld.py-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
print("Hello, World!")
```

Apesar do número de argumentos necessários/fornecidos, as funções Python exigem fortemente a presença de **um par de parêntesis** - de abertura e de fecho, respetivamente.

Se quiser entregar um ou mais **argumentos** a uma função, coloque-os **dentro dos parêntesis**. Se for utilizar uma função que não aceita qualquer argumento, ainda assim tem de ter os parêntesis.

> 🐍 **Nota**: para distinguir palavras comuns de nomes de funções, coloque **um par de parêntesis vazios** após os seus nomes, mesmo que a função correspondente queira um ou mais argumentos. Esta é uma convenção padrão.

A função de que estamos a falar aqui é `print()`. A função `print()` no nosso exemplo tem algum argumento? Claro que sim, mas o que são eles?

O único argumento entregue à função `print()` neste exemplo é uma `string`:

[![.py](https://img.shields.io/badge/-helloWorld.py-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
print("Hello, World!")
```

Como pode ver, **a string é delimitada com aspas** - de facto, as aspas fazem a string - cortam uma parte do código e atribuem-lhe um significado diferente.

Pode imaginar que as aspas dizem algo como: o texto entre nós não é código. Não se destina a ser executado, e deve tomá-lo como está.

Quase tudo o que colocar dentro das aspas será tomado literalmente, não como código, mas como **dados**. Tente jogar com esta string em particular - modificá-la, introduzir algum conteúdo novo, apagar algum do conteúdo existente.

Há mais do que uma maneira de especificar uma string dentro do código Python, mas por agora, esta é suficiente.

> Até agora, aprendeu sobre duas partes importantes do código: a função e a string. Falámos sobre elas em termos de sintaxe, mas agora é altura de os discutir em termos de semântica.

O nome da função (`print` neste caso) juntamente com os *parêntesis* e o(s) *argumento(s)*, formam a **invocação da função**.

Discutiremos isto com mais profundidade em breve, mas devemos dar-lhe umas luzes de momento.

[![.py](https://img.shields.io/badge/-helloWorld.py-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
print("Hello, World!")
```

O que acontece quando o Python encontra uma invocação como esta abaixo?

[![.py](https://img.shields.io/badge/-helloWorld.py-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
function_name(argument)
```

Vamos ver:

- Primeiro, o Python verifica se o nome especificado é **legal** (navega nos seus dados internos a fim de encontrar uma função existente com o mesmo nome; se esta pesquisa falhar, o Python aborta o código);
- segundo, o Python verifica se os requisitos da função para o número de argumentos **lhe permitem invocar** a função desta forma (por exemplo, se uma função específica exigir exatamente dois argumentos, qualquer invocação que apresente apenas um argumento será considerada errada, e abortará a execução do código);
- terceiro, o Python **deixa o seu código por um momento** e salta para a função que pretende invocar; claro, também leva o(s) seu(s) argumento(s) e passa-o(s) para a função;
- quarto, a função **executa o seu código**, causa o efeito desejado (se houver um), avalia o(s) resultado(s) desejado(s) (se existir(em)) e termina a sua tarefa;
- finalmente, o Python **regressa ao seu código** (ao local imediatamente após a invocação) e retoma a sua execução.

Três questões importantes têm de ser respondidas assim que possível:

1. Qual é o efeito que a função `print()` causa?

O efeito é muito útil e muito espetacular. A função:

- toma os seus argumentos (pode aceitar mais do que um argumento e pode também aceitar menos do que um argumento);
- converte-os numa forma legível para o ser humano, se necessário (como pode suspeitar, as strings não requerem esta ação, uma vez que a `string` já é legível);
- e envia os dados resultantes para o dispositivo de output (normalmente o console); por outras palavras, qualquer coisa que coloque na função `print()` aparecerá no ecrã.

Não admira, então, que a partir de agora utilize `print()` muito intensivamente para ver os resultados das suas operações e avaliações.

2. Que argumentos `print()` espera?

Quaisquer. Mostrar-lhe-emos em breve que `print()` é capaz de operar com virtualmente todos os tipos de dados oferecidos pelo Python. Strings, números, carateres, valores lógicos, objetos - qualquer um destes pode ser passado com sucesso para `print()`.

3. Que valor é devolvido pela função `print()` ?

Nenhum. O seu efeito é suficiente.

### Instruções Python
Já viu um programa de computador que contém uma invocação de função. Uma **invocação de função** é um dos muitos tipos possíveis de **instruções Python**.

É claro que qualquer programa complexo contém geralmente muito mais instruções do que uma. A questão é: como se acoplam mais do que uma instrução no código Python?

[![.py](https://img.shields.io/badge/-snake.py_input-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
print("The itsy bitsy spider climbed up the waterspout.")
print("Down came the rain and washed the spider out.")
```

[![.py](https://img.shields.io/badge/-snake.py_output-fff?style=social&logo=Python&logoColor=3776AB)](#)

<pre>
The itsy bitsy spider climbed up the waterspout.
Down came the rain and washed the spider out.
</pre>

A sintaxe de Python é bastante específica nesta área. Ao contrário da maioria das linguagens de programação, o Python requer que não haja mais do que uma instrução numa linha.

Uma linha pode estar vazia (ou seja, pode não conter qualquer instrução) mas não deve conter duas, três ou mais instruções. Isto é estritamente proibido.

> 🐍 **Nota**: o Python faz uma exceção a esta regra - permite que uma instrução se espalhe por mais do que uma linha (o que pode ser útil quando o seu código contém construções complexas).

### Newline
Mudámos um pouco o exemplo - acrescentámos uma invocação de função vazia `print()` . Chamamos-lhe vazia porque não apresentámos quaisquer argumentos para a função.

Pode vê-lo na janela do editor. Execute o código.

O que acontece?

Se tudo correr bem, deverá ver algo como isto:

[![.py](https://img.shields.io/badge/-snake.py_input-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")
```

[![.py](https://img.shields.io/badge/-snake.py_output-fff?style=social&logo=Python&logoColor=3776AB)](#)

<pre>
The itsy bitsy spider climbed up the waterspout.

Down came the rain and washed the spider out.
</pre>

Como pode ver, a invocação vazia `print()` não é tão vazia como se poderia esperar - produz uma linha vazia, ou (esta interpretação também é correta) o seu output é apenas uma **newline**.

Esta não é a única forma de produzir uma newline no console de output. Vamos agora mostrar-lhe outra forma.

### Caractere de escape
Modificámos novamente o código. Olhe com atenção.

Há duas mudanças muito subtis - inserimos um estranho par de carateres dentro da rima. Têm este aspeto: `\n`. Curiosamente, enquanto se pode ver dois carateres, o Python vê um.

A barra invertida `\` tem um significado muito especial quando usado dentro de strings - a isto chama-se o **caratere de escape**.

A palavra *escape* deve ser entendida especificamente - significa que a série de carateres na `string` escapa por um momento (um momento muito curto) para introduzir uma inclusão especial.

Por outras palavras, a barra invertida não significa nada em si, mas é apenas uma espécie de anúncio de que o próximo caratere após a barra invertida também tem um significado diferente.

A letra `n` colocada após a barra invertida vem da palavra **newline** (nova linha).

Tanto a barra invertida como o `n` formam um símbolo especial chamado **um caratere de newline**, que incita o console a iniciar uma nova linha de output.

Execute o código. O seu console deve agora ter este aspeto:

[![.py](https://img.shields.io/badge/-snake.py_input-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")
```

[![.py](https://img.shields.io/badge/-snake.py_output-fff?style=social&logo=Python&logoColor=3776AB)](#)

<pre>
The itsy bitsy spider
climbed up the waterspout.

Down came the rain
and washed the spider out.
</pre>

Como pode ver, duas newlines aparecem na canção de embalar, nos locais onde as `\n` foram usadas.

Esta convenção tem duas consequências importantes:

1. Se quiser colocar apenas uma barra invertida dentro de uma string, não se esqueça da sua natureza de escape - tem de a duplicar, por exemplo, uma tal invocação causará um erro:


[![.py](https://img.shields.io/badge/-snake.py_input-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
print("\")
```

enquanto esta não o fará:


[![.py](https://img.shields.io/badge/-snake.py_input-fff?style=social&logo=Python&logoColor=3776AB)](#)

```python
print("\\")
```

2. Nem todos os pares de escape (a barra invertida acoplada a outro caratere) significam algo.

Experimente o seu código no editor, execute-o e veja o que acontece.

# 📦 Gerenciandores de Pacote em Python (Package Manager)

## `pip` - Package Installer for Python
<div align="center"><img src="https://pypi.org/static/images/logo-small.95de8436.svg" height="177"></div><br \>

<img src="https://upload.wikimedia.org/wikipedia/commons/6/64/PyPI_logo.svg" height="177" align="right">

## `conda` - Anaconda
<div align="center">

<a href="https://www.anaconda.com/products/distribution"><img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/anaconda/anaconda-original-wordmark.svg" height="177"></a>
  
</div><br />


# 👹 Python-Ogre
<div align="center"><img src="https://upload.wikimedia.org/wikipedia/en/0/01/PythonOgreLogo.svg" height="177"></div><br \>

# 🦕 Django
<div align="center"><img src="https://cdn.worldvectorlogo.com/logos/django-community.svg" height="177"></div><br \>

# ⚗️ Flask
<div align="center"><img src="https://cdn.worldvectorlogo.com/logos/flask.svg" height="177"></div><br \>
