<!-- src/routes/categoria2.svelte -->
<script>
import Produto from '../../components/Produto.svelte';

const produtos = [
  {
    nome: "Cueca samba canção de algodão egípcio",
    imagem: "/images/m1.jpg",
    preco: "R$ 138,00",
    tamanhos: ["Consultar com o fornecedor"],
    cores: ["Consultar com o fornecedor"]
  },
  {
    nome: "cueca sem costura de microfibra",
    imagem: "/images/m2.jpg",
    preco: "R$ 80,00",
    tamanhos: ["consultar com o fornecedor"],
    cores: ["consultar com o fornecedor"]
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
    height: auto; /* Garante que o main tenha altura total da tela */
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