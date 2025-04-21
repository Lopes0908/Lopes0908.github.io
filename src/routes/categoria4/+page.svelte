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
			imagem: '/images/p1.jpg',
			estoque: 'Em estoque',
			preco: 'R$ 230,00',
			tamanhos: ['M'],
			cores: ['Verde'],
			estoque: 'Esgotado',
		},
		{
			nome: 'Pijama Canelado',
			imagem: '/images/p2.jpg',
			preco: 'R$ 230,00',
			tamanhos: ['G'],
			cores: ['Bicolor'],
			estoque: 'Esgotado',
		},
		{
			nome: 'Pijama Canelado',
			imagem: '/images/p3.jpg',
			preco: 'R$ 230,00',
			tamanhos: ['GG'],
			cores: ['Bicolor'],
			estoque: 'Disonível',
		},
		{
			nome: 'Camisola de liganetie',
			imagem: '/images/c1.jpg',
			preco: 'R$ 180,00',
			tamanhos: ['G'],
			cores: ['Sandia'],
			estoque: 'Esgotado',
		},
		{
			nome: 'Camisola de liganetie',
			imagem: '/images/c2.jpg',
			preco: 'R$ 180,00',
			tamanhos: ['M'],
			cores: ['Lichia'],
			estoque: 'Esgotado',
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
	button:hover {
		transform: scale(1.1); /* Aumenta o botão */
		background-color: #b76e79; /* Muda a cor de fundo */
		border: 2px solid #ffd700;
		margin: 10px;
		padding: 10px;
		font-size: 16px;
	}
	button:active {
		transform: scale(0.95); /* Diminui o botão */
		background-color: #b76e79; /* Muda a cor de fundo para um tom mais escuro */
		border: 2px solid #ffd700;
		margin: 10px;
		padding: 10px;
		font-size: 16px;
		border-color: #ffd700;
	}
	main {
		padding: 20px;
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
		border: 2px solid #ffd700;
		margin: 10px;
		padding: 10px;
		font-size: 16px;
		background-color: #b76e79;
		cursor: pointer;
		transition: all 0.3s ease;
		border-radius: 8px; /* Bordas arredondadas */
	}
	select {
		margin: 10px;
		padding: 10px;
		font-size: 16px;
		border-radius: 8px;
		border: 2px solid #ffd700;
	}
	select {
		margin: 10px;
		padding: 10px;
		font-size: 16px;
		border-radius: 8px solid #ffd700;
		border: 2px solid #ffd700;
		background-color: #b76e79;
		color: black;
		cursor: pointer;
		transition: all 0.3s ease;
	}
	select:hover {
		transform: scale(1.1);
		border-color: #ffd700;
		background-color: #b76e79;
	}
	select:active {
		transform: scale(0.95);
		border-color: #ffd700;
		background-color: #b76e79;
	}
	option:value {
		background-color: #b76e79;
		color: black;
		border-radius: 8px solid #ffd700;
		cursor: pointer;
		transition: all 0.3s ease;
	}
</style>