<script lang="ts">
    import { onMount } from 'svelte';
    let nome = '';
    let raca = '';
    let classe = '';
    let personagens: { nome: string; raca: string; classe: string }[] = [];
    let mostrarLista = false;

    // Carregar personagens do localStorage ao iniciar
    onMount(() => {
        const dados = localStorage.getItem('personagens');
        if (dados) {
            personagens = JSON.parse(dados);
        }
    });

    function cadastrar() {
        if (nome && raca && classe) {
            personagens = [...personagens, { nome, raca, classe }];
            localStorage.setItem('personagens', JSON.stringify(personagens));
            nome = '';
            raca = '';
            classe = '';
            alert('Personagem cadastrado com sucesso!');
        }
    }

    function mostrarPersonagens() {
        mostrarLista = true;
    }

    function voltarCadastro() {
        mostrarLista = false;
    }
</script>

{#if !mostrarLista}
    <h1>Cadastrar Personagem</h1>
    <form on:submit|preventDefault={cadastrar}>
        <label>
            Nome:
            <input bind:value={nome} required />
        </label>
        <br />
        <label>
            Raça:
            <input bind:value={raca} required />
        </label>
        <br />
        <label>
            Classe:
            <input bind:value={classe} required />
        </label>
        <br />
        <button type="submit">Cadastrar</button>
    </form>
    <button on:click={mostrarPersonagens} style="margin-top: 1em;">Ver Personagens</button>
{:else}
    <h1>Personagens Cadastrados</h1>
    {#if personagens.length === 0}
        <p>Nenhum personagem cadastrado.</p>
    {:else}
        <ul>
            {#each personagens as p}
                <li><strong>{p.nome}</strong> - {p.raca} - {p.classe}</li>
            {/each}
        </ul>
    {/if}
    <button on:click={voltarCadastro} style="margin-top: 1em;">Voltar ao Cadastro</button>
{/if}

<style>
    form {
        margin-bottom: 1em;
    }
    label {
        display: block;
        margin-bottom: 0.5em;
    }
    input {
        margin-left: 0.5em;
    }
</style>