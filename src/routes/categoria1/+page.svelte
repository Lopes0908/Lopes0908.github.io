<script>

    // Não precisamos de lógica no momento
</script>
  
<main>
 
  
<div>
    <button on:click={() => window.location.replace('/')} style="color:black">Voltar para a Página Inicial</button>
   
    <button on:click={() => window.location.href='/categoria2'} style="color:black">Peças Masculinas</button>    
  </div>
</main>
  
<style>
   button:hover {
        transform: scale(1.1); /* Aumenta o botão */
        background-color: #b76e79; /* Muda a cor de fundo */
    }
    button:active {
        transform: scale(0.95); /* Diminui o botão */
        background-color: #b76e79; /* Muda a cor de fundo para um tom mais escuro */
    }
  main {
    padding: 20px;
    background-color: darkred;
    color: white; /* Ajuste a cor do texto */
    height: 100vh; /* Garante que o main tenha altura total da tela */
  }
  @media (max-width: 600px) {
        button {
            font-size: 16px; /* Diminui o tamanho da fonte em telas pequenas */
            padding: 10px 20px; /* Ajusta o padding em dispositivos móveis */
        }
    }
  button {
    border: 2px solid black;
    margin: 10px;
    padding: 10px;
    font-size: 16px;
    background-color: #b76e79;
    border-color: #FFD700;
    cursor: pointer;
    transition: all 0.3s ease;
    border-radius: 8px; /* Bordas arredondadas */
  }
</style>

<!-- Adicionando o link da fonte Ballpark Weiner -->
<link href="https://fonts.googleapis.com/css2?family=Ballpark+Weiner&display=swap" rel="stylesheet">