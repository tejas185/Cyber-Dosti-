document.getElementById('crackButton').addEventListener('click', function() {
    const username = document.getElementById('username').value;
    const passwordList = [
        '1234', 'password', 'admin', 'letmein', 'welcome', 
        'password1', 'qwerty', 'abc123', 'iloveyou', '111111', 
        'sunshine', '123123', 'admin123', 'password123', '654321', 
        'superman', 'batman', 'dragon', 'master', 'trustno1'
    ];

    let resultDiv = document.getElementById('result');
    resultDiv.textContent = 'Cracking password...';

    setTimeout(() => {
        for (let password of passwordList) {
            password = password.trim();
            // Simulate checking the password (replace with real check if needed)
            if (checkPassword(username, password)) {
                resultDiv.textContent = `Password found: ${password}`;
                return;
            }
        }
        resultDiv.textContent = 'Password not found in the given list.';
    }, 100);
});

function checkPassword(username, password) {
    // Simulate a password check
    // Replace with real password check logic
    const correctPassword = 'password123'; // Example correct password
    return password === correctPassword;
}
