function handleSubmit(event) {
    console.log('-------------event----------');
    // prevent the form from submitting normally
    event.preventDefault();

    // Disable the button until the promise is settled.
    const submitButton = document.querySelector("#submit-button");
    submitButton.setAttribute('disabled', true);

    // submit the form using AJAX
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