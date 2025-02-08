<!-- src/routes/categoria2.svelte -->
<script>
import Produto from '../../components/Produto.svelte';

const produtos = [
  {
    nome: "Tênis Casual",
    imagem: "/images/tenis.jpg",
    preco: "R$ 159,90",
    tamanhos: ["36", "37", "38", "39"],
    cores: ["Cinza", "Preto", "Branco"]
  },
  {
    nome: "Bolsa de Couro",
    imagem: "/images/bolsa.jpg",
    preco: "R$ 199,90",
    tamanhos: ["Único"],
    cores: ["Preto", "Marrom"]
  }
];
    // Não precisamos de lógica no momento
</script>
  
<main>
 
  
<div>
    <h1 style="color: #b76e79; font-family: 'Ballpark Weiner', cursive;">Aba de Peças Masculinas</h1>
    <button on:click={() => window.location.replace('/')} style="color:black">Voltar para a Página Inicial</button>
   
    <button on:click={() => window.location.href='/categoria1'} style="color:black">Peças Femininas</button>   
    <div class="produtos">
        {#each produtos as produto}
          <Produto {...produto} />
        {/each} 
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