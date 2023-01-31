function deleteImage(card) {
    fetch('/delete-card', {
        method: 'POST',
        body: JSON.stringify({ card: card}),
    }).then(() => {
        window.location.href = "/game";
    })
}