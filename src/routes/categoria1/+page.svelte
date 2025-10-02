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
			nome: 'Conjunto renda bicolor',
			imagem: '/images/f2.jpg',
			preco: 'R$ 177,00',
			tamanhos: ['M'],
			cores: ['Vinho'],
		},
		{
			nome: 'Conjunto de cropped',
			imagem: '/images/f3.jpg',
			preco: 'R$ 188,00',
			tamanhos: ['M'],
			cores: ['Vermelho'],
		},
		{
			nome: 'Conjunto com laços',
			imagem: '/images/f5.jpg',
			preco: 'R$ 175,00',
			tamanhos: ['G'],
			cores: ['Preto'],
		},
		{
			nome: 'Conjunto',
			imagem: '/images/f6.jpg',
			preco: 'R$ 178,00',
			tamanhos: ['G'],
			cores: ['Preto'],
		},
		{
			nome: 'Conjunto com bojo soft',
			imagem: '/images/f9.jpg',
			preco: 'R$ 176,00',
			tamanhos: ['G'],
			cores: ['Lavanda'],
		},
		{
			nome: 'Conjunto básico',
			imagem: '/images/f10.jpg',
			preco: 'R$ 180,00',
			tamanhos: ['G'],
			cores: ['Nude'],
		},
		{
			nome: 'Conjunto básico',
			imagem: '/images/f11.jpg',
			preco: 'R$ 180,00',
			tamanhos: ['G'],
			cores: ['Odalisca'],
		},
		{
			nome: 'Conjunto Reforçado',
			imagem: '/images/f13.jpg',
			preco: 'R$ 194,00',
			tamanhos: ['G'],
			cores: ['Nude'],
		},
        {
			nome: 'Conjunto de Renda',
			imagem: '/images/f17.jpg',
			preco: 'R$ 178,00',
			tamanhos: ['GG'],
			cores: ['Divino'],
		},
		{
			nome: 'Conjunto sem bojo com detalhes de rolote',
			imagem: '/images/f21.jpg',
			preco: 'R$ 178,00',
			tamanhos: ['G'],
			cores: ['Preto'],
		},
		{
			nome: 'Conjunto tomara que caia com a lateral dupla e reforçada',
			imagem: '/images/f25.jpg',
			preco: 'R$ 176,00',
			tamanhos: ['M'],
			cores: ['Preto'],
		}
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
