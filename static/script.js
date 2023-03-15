function handleSubmit(event) {
    console.log('-------------event----------');
    event.preventDefault();

    const submitButton = document.querySelector("#submit-button");
    submitButton.setAttribute('disabled', true);

    const form = event.target;
    const url = '/predict';
    const formData = new FormData(form);


    fetch(url, {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            // handle the response data here
            const resultElement = document.querySelector("#prediction-value");
            if (resultElement) {
                resultElement.innerHTML = "$" + data.predicted_price;
            }
        })
        .catch(error => {
            // handle any errors here
            alert('Something went wrong');
            console.log('Error while submitting the form', error)
        })
        .finally(() => {
            submitButton.removeAttribute('disabled');
        })

}

const form = document.querySelector('#price-prediction-form');
form.addEventListener('submit', handleSubmit);
