<script>
    // Lista de álbuns com suas músicas, informações adicionais e imagens
    let albuns = [
        { 
            artista: "Artista 1",
            titulo: "Título 1",
            ano: 2021,
            numeroDisco: "001",
            gravadora: "Gravadora 1",
            acervoSN: "Sim",
            captura: "Digital",
            musicas: ["Musica 1", "Musica 2", "Musica 3"],
            imagem: "/path/to/image1.jpg" // Adicione o caminho da imagem
        },
        { 
            artista: "Artista 2",
            titulo: "Título 2",
            ano: 2020,
            numeroDisco: "002",
            gravadora: "Gravadora 2",
            acervoSN: "Não",
            captura: "Analógica",
            musicas: ["Musica A", "Musica B", "Musica C"],
            imagem: "/path/to/image2.jpg" // Adicione o caminho da imagem
        },
        { 
            artista: "Artista 3",
            titulo: "Título 3",
            ano: 2019,
            numeroDisco: "003",
            gravadora: "Gravadora 3",
            acervoSN: "Sim",
            captura: "Digital",
            musicas: ["Musica X", "Musica Y", "Musica Z"],
            imagem: "/path/to/image3.jpg" // Adicione o caminho da imagem
        }
    ];

    let activeAlbum = null;

    function toggleAlbum(index) {
        activeAlbum = activeAlbum === index ? null : index;
    }
</script>

<style>
    .album {
        margin: 1rem 0;
        padding: 1rem;
        background: #f0f0f0;
        border-radius: 8px;
        cursor: pointer;
    }

    .album img {
        max-width: 100%;
        height: auto;
        border-radius: 8px;
        margin-bottom: 1rem;
    }

    .musicas-popup {
        position: absolute;
        background: white;
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        z-index: 1000;
    }
</style>

<div>
    <h1>Álbuns</h1>
    {#each albuns as album, index}
        <div class="album" on:click={() => toggleAlbum(index)}>
            <img src={album.imagem} alt={`Imagem do álbum`} />
            <p><strong>Artista:</strong> {album.artista}</p>
            <p><strong>Título:</strong> {album.titulo}</p>
            <p><strong>Ano:</strong> {album.ano}</p>
            <p><strong>Nº. disco:</strong> {album.numeroDisco}</p>
            <p><strong>Gravadora:</strong> {album.gravadora}</p>
            <p><strong>Acervo S/N:</strong> {album.acervoSN}</p>
            <p><strong>Captura:</strong> {album.captura}</p>
        </div>
        {#if activeAlbum === index}
            <div class="musicas-popup">
                <h3>Músicas:</h3>
                <ul>
                    {#each album.musicas as musica}
                        <li>{musica}</li>
                    {/each}
                </ul>
            </div>
        {/if}
    {/each}
</div>
