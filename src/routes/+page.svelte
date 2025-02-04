<script>
    // Não precisamos de lógica no momento
</script>
  
<main>
  <h1 style="color: #b76e79; font-family: 'Ballpark Weiner', cursive;">D'ROSI</h1>
  <h2 style="color: #b76e79; font-family: 'Ballpark Weiner', cursive;">LINGERIE</h2>

  <p>Entre em contato para adquirir as peças: (67) 93505-8192</p>
  
  <div>
    <button on:click={() => window.location.href='/categoria1'} >Categoria 1</button>
    <button on:click={() => window.location.href='/categoria2'} >Categoria 2</button>    
  </div>
</main>
  
<style>
  main {
    text-align: center;
    padding: 20px;
    background-color: darkred;
    color: white; /* Ajuste a cor do texto */
    height: 100vh; /* Garante que o main tenha altura total da tela */
  }

  button {
    margin: 10px;
    padding: 10px;
    font-size: 16px;
    background-color: #b76e79;
    border-color: #FFD700;
  }
</style>

<!-- Adicionando o link da fonte Ballpark Weiner -->
<link href="https://fonts.googleapis.com/css2?family=Ballpark+Weiner&display=swap" rel="stylesheet">