const predictButton = document.querySelector("#predict-button");
const imageInput = document.querySelector("#image-upload");

predictButton.onclick = () => {
    if (imageInput.value) {
        predictButton.classList.add('disabled');
    }
}

