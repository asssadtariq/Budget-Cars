function change() {
    var minEle = document.getElementById('min-price');
    var maxEle = document.getElementById('max-price');

    if (minEle.value.length != 0 && parseInt(minEle.value) >= 0 ) {
        maxEle.value = parseInt(minEle.value) + 5000;
    }
    else if (parseInt(minEle.value) < 0) {
        minEle.value = 0;
    }
    else {
        maxEle.value = 0;
    }
}

function showText(target, message, msgText = "", indexCounter = 0) {
    if (indexCounter >= (message).length) {
        return;
    }

    console.log(target, target.innerText)
    target.value += msgText
    showText(target, message, msgText[indexCounter], indexCounter + 1);
}

$(document).ready(() => {
})

