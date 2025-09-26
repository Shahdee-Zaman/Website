async function getOutput(prompt) {
    const response = await fetch('/job_description', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: prompt })
    });
    const data = await response.json();
    changeTextArea(data);
}



function changeTextArea(output = false) {
    const user = document.getElementById('user_text');
    const button = document.getElementById('submission');
    if (!output) {
        user.disabled = false;
        user.value = '';
        button.value = 'Submit';
    }
    else if (!user.disabled) {
        user.disabled = true;
        user.value = output;
        button.value = 'New Entry'
    }
}

document.getElementById('job_description').addEventListener('submit', (event) => {
    event.preventDefault();
    const user = document.getElementById('user_text');
    const button = document.getElementById('submission');
    if (button.value == 'New Entry') changeTextArea(false);
    else {
        const text = user.value;
        getOutput(text);
    }
})
