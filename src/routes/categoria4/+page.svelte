<script>
	import Produto from '../../components/Produto.svelte';
	import { onMount } from 'svelte';

	onMount(() => {
		const btnTopo = document.getElementById('f4');
		btnTopo.onclick = function () {
			window.scrollTo({
				top: 0,
				behavior: 'smooth'
			});
		};
	});
    const produtos = [
		{
			nome: 'Pijama Canelado',
			imagem: '/images/p3.jpg',
			preco: 'R$ 230,00',
			tamanhos: ['GG'],
			cores: ['Bicolor'],
		},
		{
			nome: 'Pijama Canelado',
			imagem: '/images/p4.jpg',
			preco: 'R$ 230,00',
			tamanhos: ['G'],
			cores: ['Rosa Bebê'], 
		},
	];

	let selectedTamanho = '';
	let selectedCor = '';

	function filterProdutos() {
		return produtos.filter((produto) => {
			const tamanhoMatch = selectedTamanho ? produto.tamanhos.includes(selectedTamanho) : true;
			const corMatch = selectedCor ? produto.cores.includes(selectedCor) : true;
			return tamanhoMatch && corMatch;
		});
	}
</script>

<main>
	<h1 style="color: #b76e79; font-family: 'Ballpark Weiner', cursive;">Aba de Pijamas</h1>
	<button on:click={() => window.location.replace('/')} style="color:blacl"
		>Voltar para a Página Inicial</button
	>
	<button on:click={() => (window.location.href = '/categoria1')} style="color:black"
		>Peças Femininas</button
	>
	<button on:click={() => (window.location.href = '/categoria2')} style="color:black"
		>Peças Masculinas</button
	>
    <button on:click={() => (window.location.href = '/categoria3')} style="color:black"
		>Peças Avulsas</button
        >
	<div>
		<label for="tamanho" style="color: black;">Selecionar Tamanho:</label>
		<select id="tamanho" bind:value={selectedTamanho}>
			<option value="">Todos</option>
			<option value="M">M</option>
			<option value="G">G</option>
			<option value="GG">GG</option>
			<!-- Adicione mais opções conforme necessário -->
		</select>

		<label for="cor" style="color: black;">Selecionar Cor:</label>
		<select id="cor" bind:value={selectedCor}>
			<option value="">Todos</option>
			<option value="Verde">Verde</option>
			<option value="Bicolor">Bicolor</option>
			<option value="Sandia">Sandia</option>
			<option value="Lichia">Lichia</option>
			<!-- Adicione mais opções conforme necessário -->
		</select>
	</div>

	{#each filterProdutos() as produto}
		<Produto {...produto} />
	{:else}
		<center
			><br /><br />
			<p style="color: black; font-size: 20px;">Nenhum produto encontrado</p></center
		>
	{/each}
</main>

<button id="f4">topo</button>

<!-- Adicionando o link da fonte Ballpark Weiner -->
<link
	href="https://fonts.googleapis.com/css2?family=Ballpark+Weiner&display=swap"
	rel="stylesheet"
/>

<svelte:head>
	<style>
		body {
			background-color: darkred;
		}
	</style>
</svelte:head>

<style>
	button {
		border: 2px solid #ffd700;
		margin: 10px;
		padding: 10px;
		font-size: 16px;
		background-color: #b76e79;
		cursor: pointer;
		transition: all 0.3s ease;
		border-radius: 8px; /* Bordas arredondadas */
		box-shadow: 4px 4px 6px rgba(0, 0, 0, 0.3); /* Efeito 3D */
		transform: translateY(-2px); /* Eleva o botão levemente */
	}

	button:hover {
		transform: scale(1.1) translateY(-4px); /* Aumenta e eleva mais o botão */
		background-color: #b76e79; /* Muda a cor de fundo */
		border: 2px solid #ffd700;
		margin: 10px;
		padding: 10px;
		font-size: 16px;
		box-shadow: 6px 6px 8px rgba(0, 0, 0, 0.4); /* Intensifica o efeito 3D */
	}

	button:active {
		transform: scale(0.95) translateY(2px); /* Diminui e "pressiona" o botão */
		background-color: #b76e79; /* Muda a cor de fundo para um tom mais escuro */
		border: 2px solid #ffd700;
		margin: 10px;
		padding: 10px;
		font-size: 16px;
		border-color: #ffd700;
		box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2); /* Reduz o efeito 3D */
	}
	select {
		border: 2px solid #ffd700;
		margin: 10px;
		padding: 10px;
		font-size: 16px;
		background-color: #b76e79;
		color: black;
		cursor: pointer;
		transition: all 0.3s ease;
		border-radius: 8px; /* Bordas arredondadas */
		box-shadow: 4px 4px 6px rgba(0, 0, 0, 0.3); /* Efeito 3D */
		transform: translateY(-2px); /* Eleva o botão levemente */
	}

	select:hover {
		transform: scale(1.1) translateY(-4px); /* Aumenta e eleva mais o botão */
		background-color: #b76e79; /* Muda a cor de fundo */
		box-shadow: 6px 6px 8px rgba(0, 0, 0, 0.4); /* Intensifica o efeito 3D */
	}

	select:active {
		transform: scale(0.95) translateY(2px); /* Diminui e "pressiona" o botão */
		background-color: #b76e79; /* Muda a cor de fundo para um tom mais escuro */
		box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2); /* Reduz o efeito 3D */
	}
</style>