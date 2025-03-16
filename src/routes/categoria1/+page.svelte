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
			nome: 'Conjunto',
			imagem: '/images/f1.jpg',
			preco: 'R$ 192,00',
			tamanhos: ['P'],
			cores: ['Preto'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto renda bicolor',
			imagem: '/images/f2.jpg',
			preco: 'R$ 177,00',
			tamanhos: ['M'],
			cores: ['Vinho'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto de cropped',
			imagem: '/images/f3.jpg',
			preco: 'R$ 188,00',
			tamanhos: ['M'],
			cores: ['Vermelho'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto rendado',
			imagem: '/images/f4.jpg',
			preco: 'R$ 170,00',
			tamanhos: ['M'],
			cores: ['Nude'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto com laços',
			imagem: '/images/f5.jpg',
			preco: 'R$ 175,00',
			tamanhos: ['G'],
			cores: ['Preto'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto',
			imagem: '/images/f6.jpg',
			preco: 'R$ 178,00',
			tamanhos: ['G'],
			cores: ['Preto'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto com laços',
			imagem: '/images/f7.jpg',
			preco: 'R$ 175,00',
			tamanhos: ['M'],
			cores: ['Divino'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto',
			imagem: '/images/f8.jpg',
			preco: 'R$ 230,00',
			tamanhos: ['G'],
			cores: ['Bicolor'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto com bojo soft',
			imagem: '/images/f9.jpg',
			preco: 'R$ 176,00',
			tamanhos: ['G'],
			cores: ['Lavanda'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto básico',
			imagem: '/images/f10.jpg',
			preco: 'R$ 180,00',
			tamanhos: ['G', 'GG'],
			cores: ['Nude'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto básico',
			imagem: '/images/f11.jpg',
			preco: 'R$ 180,00',
			tamanhos: ['G', 'GG', 'M'],
			cores: ['Odalisca'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto básico',
			imagem: '/images/f12.jpg',
			preco: 'R$ 180,00',
			tamanhos: ['GG','M'],
			cores: ['Verde claro'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto Reforçado',
			imagem: '/images/f13.jpg',
			preco: 'R$ 194,00',
			tamanhos: ['G','GG'],
			cores: ['Nude'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto Reforçado',
			imagem: '/images/f14.jpg',
			preco: 'R$ 194,00',
			tamanhos: ['G'],
			cores: ['Preto'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto de renda',
			imagem: '/images/f15.jpg',
			preco: 'R$ 178,00',
			tamanhos: ['G'],
			cores: ['Nude'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto de Renda',
			imagem: '/images/f16.jpg',
			preco: 'R$ 178,00',
			tamanhos: ['M'],
			cores: ['Verde claro'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto de Renda',
			imagem: '/images/f17.jpg',
			preco: 'R$ 178,00',
			tamanhos: ['GG'],
			cores: ['Divino'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto de bojo confort',
			imagem: '/images/f18.jpg',
			preco: 'R$ 160,00',
			tamanhos: ['M'],
			cores: ['Azul claro'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto de bojo confort',
			imagem: '/images/f19.jpg',
			preco: 'R$ 160,00',
			tamanhos: ['M'],
			cores: ['Rosa'],
			estoque: 'Disonível',
		},
		{
			nome: 'Conjunto de bojo confort',
			imagem: '/images/f20.jpg',
			preco: 'R$ 160,00',
			tamanhos: ['M'],
			cores: ['Divino'],
			estoque: 'Disonível',
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
	<h1 style="color: #b76e79; font-family: 'Ballpark Weiner', cursive;">Aba de Peças Femininas</h1>
	<button on:click={() => window.location.replace('/')} style="color:black"
		>Voltar para a Página Inicial</button
	>
	<button on:click={() => (window.location.href = '/categoria2')} style="color:black"
		>Peças Masculinas</button
	>
	<button on:click={() => (window.location.href = '/categoria3')} style="color:black"
		>Peças Avulsas</button
	>
	<button on:click={() => (window.location.href = '/categoria4')} style="color:black"
		>Pijamas e Camisolas</button
		>
	<div>
		<label for="tamanho" style="color: black;">Selecionar Tamanho:</label>
		<select id="tamanho" bind:value={selectedTamanho}>
			<option value="">Todos</option>
			<option value="M">M</option>
			<option value="P">P</option>
			<option value="G">G</option>
			<option value="GG">GG</option>
			<!-- Adicione mais opções conforme necessário -->
		</select>

		<label for="cor" style="color: black;">Selecionar Cor:</label>
		<select id="cor" bind:value={selectedCor}>
			<option value="">Todas</option>
			<option value="Nude">Nude</option>
			<option value="Bicolor">Bicolor</option>
			<option value="Vermelho">Vermelho</option>
			<option value="Preto">Preto</option>
			<option value="Vinho">Vinho</option>
			<option value="Divino">Divino</option>
			<option value="Lavanda">Lavanda</option>
			<option value="Odalisca">Odalisca</option>
			<option value="Verde claro">Verde claro</option>
			<option value="Azul claro">Azul claro</option>
			<option value="Azul marinho">Azul marinho</option>
			<option value="Romance">Romance</option>
			<option value="Preto">Preto</option>
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