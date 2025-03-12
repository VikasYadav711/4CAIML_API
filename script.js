function fetchAPIdata(text, id) {
    let apiUrl = '';//exampl url`http://103.115.194.42/sentnew?text=${encodeURIComponent(text)}`;

    fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const formattedData = JSON.stringify(data, null, 2);
        document.getElementById(`api-result-tab-pane-p-${id}`).innerHTML = `<pre>${formattedData}</pre>`;
    })
    .catch(err => {
        console.error("API error:", err);
        document.getElementById(`api-result-tab-pane-p-${id}`).innerHTML = `<pre style="color: red;">Error fetching data</pre>`;
    });
}
