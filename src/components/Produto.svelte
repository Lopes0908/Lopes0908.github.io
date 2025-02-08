<script>
      export let nome = '';
      export let imagem = '';
    export let preco = 0;
      export let tamanhos = [];
      export let cores = [];
  </script>

<div class="produto">
    <img src={imagem} alt={nome} />
    <h2>{nome}</h2>
    <p>Preço: {preco}</p>
    <p>Tamanhos: {tamanhos.join(", ")}</p>
    <p>Cores: {cores.join(", ")}</p>
  </div>
  <style>
    .produto {
      border: 2px solid black;
      padding: 10px;
      margin: 10px;
      border-color: #FFD700;
      border-radius: 8px; /* Bordas arredondadas */
      text-align: center;
    }
  
    img {
      max-width: 100%;
      height: auto;
    }
  
    h2 {
      font-size: 1.5rem;
      margin-top: 10px;
    }
  
    p {
      margin: 5px 0;
    }
  </style>