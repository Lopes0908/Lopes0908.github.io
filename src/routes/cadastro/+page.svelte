<script lang="ts">
    import { onMount } from 'svelte';
    let nome = '';
    let raca = '';
    let classe = '';
    let foto: string | null = null;
    let personagens: { nome: string; raca: string; classe: string; foto: string | null }[] = [];
    let mostrarLista = false;
    let urlCompartilhamento: string | null = null;

    // Carregar personagens do localStorage ou da URL ao iniciar
    onMount(() => {
        const params = new URLSearchParams(window.location.search);
        const dadosUrl = params.get('dados');
        if (dadosUrl) {
            try {
                personagens = JSON.parse(decodeURIComponent(atob(dadosUrl)));
                mostrarLista = true;
            } catch (e) {
                alert('Erro ao carregar personagens compartilhados.');
            }
        } else {
            const dados = localStorage.getItem('personagens');
            if (dados) {
                personagens = JSON.parse(dados);
            }
        }
    });

    function handleFotoChange(event: Event) {
        const file = (event.target as HTMLInputElement).files?.[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                foto = e.target?.result as string;
            };
            reader.readAsDataURL(file);
        } else {
            foto = null;
        }
    }

    function cadastrar() {
        if (nome && raca && classe) {
            personagens = [...personagens, { nome, raca, classe, foto }];
            localStorage.setItem('personagens', JSON.stringify(personagens));
            nome = '';
            raca = '';
            classe = '';
            foto = null;
            alert('Personagem cadastrado com sucesso!');
        }
    }

    function mostrarPersonagens() {
        mostrarLista = true;
    }

    function voltarCadastro() {
        mostrarLista = false;
    }

    function deletarPersonagem(index: number) {
        personagens = personagens.filter((_, i) => i !== index);
        localStorage.setItem('personagens', JSON.stringify(personagens));
    }

    function gerarUrlCompartilhamento() {
        const dados = encodeURIComponent(btoa(JSON.stringify(personagens)));
        urlCompartilhamento = `${window.location.origin}${window.location.pathname}?dados=${dados}`;
    }

    function copiarUrl(url: string) {
        navigator.clipboard.writeText(url);
        alert('URL copiada!');
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
        <label>
            Foto de Perfil:
            <input type="file" accept="image/*" on:change={handleFotoChange} />
        </label>
        {#if foto}
            <div style="margin-top:0.5em;">
                <img src={foto} alt="Prévia da foto" style="max-width: 100px; max-height: 100px; border-radius: 8px;" />
            </div>
        {/if}
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
            {#each personagens as p, i}
                <li>
                    {#if p.foto}
                        <img src={p.foto} alt="Foto de perfil" style="width:40px; height:40px; object-fit:cover; border-radius:50%; vertical-align:middle; margin-right:0.5em;" />
                    {/if}
                    <strong>{p.nome}</strong> - {p.raca} - {p.classe}
                    <button on:click={() => deletarPersonagem(i)} style="margin-left: 1em;">Deletar</button>
                </li>
            {/each}
        </ul>
    {/if}
    <button on:click={voltarCadastro} style="margin-top: 1em;">Voltar ao Cadastro</button>
{/if}

{#if personagens.length > 0}
    <button on:click={gerarUrlCompartilhamento} style="margin-top: 1em;">Gerar URL de Compartilhamento</button>
{/if}
{#if urlCompartilhamento}
    <div style="margin-top: 0.5em;">
        <input type="text" readonly value={urlCompartilhamento} style="width: 80%;" />
        <button on:click={() => copiarUrl(urlCompartilhamento)}>Copiar</button>
    </div>
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
    ul {
        padding-left: 1em;
    }
    li {
        margin-bottom: 0.5em;
    }
    button {
        cursor: pointer;
    }
</style>
