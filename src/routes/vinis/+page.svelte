<script>
    // Lista de artistas
    let artistas = [
        { nome: "Artista 1", id: 1 },
        { nome: "Artista 2", id: 2 },
        { nome: "Artista 3", id: 3 }
    ];

    // Função para navegar para a página de álbuns
    const irParaAlbuns = (id) => {
        window.location.href = `/albuns/${id}`;
    };
</script>

<style>
    .artista {
        margin: 10px 0;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    button {
        margin-top: 5px;
        padding: 5px 10px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 3px;
        cursor: pointer;
    }

    button:hover {
        background-color: #0056b3;
    }
</style>

<h1>Artistas</h1>
<div>
    {#each artistas as artista}
        <div class="artista">
            <p>{artista.nome}</p>
            <button on:click={() => irParaAlbuns(artista.id)}>Ver Álbuns</button>
        </div>
    {/each}
</div>