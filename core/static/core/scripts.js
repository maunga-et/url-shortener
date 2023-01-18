
function handleRequest() {
    let url = document.querySelector('#url').value

    if (url === "") {
        document.querySelector('#notification').classList.remove('d-none');
        document.querySelector('#notification').classList.add('alert-danger');
        document.querySelector('#notification').innerHTML = 'The URL cannot be empty.';
    } else {
        var requestObject = new XMLHttpRequest();
        requestObject.onreadystatechange = () => {
            if (requestObject.readyState === XMLHttpRequest.DONE) {
                if (requestObject.status === 200) {
                    document.querySelector('.btn-text').classList.remove('d-none');
                    document.querySelector('button').classList.remove('disabled');
                    document.querySelector('.spinner-span').classList.remove('spinner-border');

                    document.querySelector('#notification').classList.remove('d-none');
                    document.querySelector('#notification').classList.remove('alert-danger');
                    document.querySelector('#notification').classList.add('alert-success');
                    cleaned_data = JSON.parse(requestObject.responseText);
                    document.querySelector('#notification').innerHTML = `https://tinly.com/${cleaned_data['data']}`;
                    
                } else {
                    document.querySelector('.btn-text').classList.remove('d-none');
                    document.querySelector('button').classList.remove('disabled');
                    document.querySelector('.spinner-span').classList.remove('spinner-border');
                    document.querySelector('#notification').classList.remove('d-none');
                    document.querySelector('#notification').classList.add('alert-danger');
                    document.querySelector('#notification').innerHTML = requestObject.status;
                } 
            } else {
                document.querySelector('button').classList.add('disabled');
                document.querySelector('.btn-text').classList.add('d-none');
                document.querySelector('.spinner-span').classList.add('spinner-border');
            }
        }
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== ''){
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        requestObject.open('POST', 'http://localhost:8000/api/shorten-url');
        requestObject.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        requestObject.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        requestObject.send(`url=${encodeURIComponent(url)}`);
    }
}
form = document.querySelector('form');
form.addEventListener(
    'submit',
    (e) => {
        e.preventDefault();
        e.stopPropagation();
        handleRequest();
    }
)