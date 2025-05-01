<script>
	export let nome = '';
	export let imagem = '';
	export let estoque = '';
	export let preco = 0;
	export let tamanhos = [];
	export let cores = [];
</script>

<div class="produto">
	<img src={imagem} alt={nome} />
	<div class="produto-info">
		<h2>{nome}</h2>
		<p><strong>Estoque:</strong> {estoque}</p>
		<p><strong>Preço:</strong> {preco}</p>
		<p><strong>Tamanhos:</strong> {tamanhos.join(', ')}</p>
		<p><strong>Cores:</strong> {cores.join(', ')}</p>
	</div>
</div>

<style>
	.produto {
		display: flex;
		flex-direction: column;
		align-items: center;
		background-color: #b76e79; /* Muda a cor de fundo */
		border: 2px solid #ffd700;
		border-radius: 8px solid #ffd700;
		box-shadow: 0 4px 6px rgba(0, 0, 0, 900);
		border-radius: 12px;
		padding: 20px;
		margin: 10px;
		width: 300px;
		transition: transform 0.2s, box-shadow 0.2s;
	}

	.produto:hover {
		transform: translateY(-5px);
		box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
	}
    .produto:active {
		transform: translateY(5px);
		box-shadow: 0 2px 3px rgba(0, 0, 0, 0.4);
	}
	.produto:focus {
		outline: none;
		box-shadow: 0 0 0 4px rgba(255, 215, 0, 0.5);
	}
	img {
		width: 100%;
		height: auto;
		border-radius: 8px;
		margin-bottom: 15px;
		border: 2px solid #ffd700;
		border-radius: 8px solid #ffd700;
	}

	.produto-info {
		text-align: center;
	}

	h2 {
		font-size: 1.5rem;
		margin-bottom: 10px;
		color: black;
	}

	p {
		margin: 5px 0;
		color: black;
	}

	p strong {
		color: black;
	}
</style>
