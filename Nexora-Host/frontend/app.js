const API_URL = "http://localhost:5000";


async function checkServer() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();

        console.log("Nexora Host:", data);

    } catch (error) {
        console.log("Backend недоступен");
    }
}


checkServer();
