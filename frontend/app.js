function classifyText() {
    var text = document.getElementById('textInput').value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://emote.default.svc.cluster.local:5050/classify", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            displayResults(response);
        }
    };

    var data = JSON.stringify({ "text": text, "labels": ["positive", "negative", "neutral"] });
    xhr.send(data);
}

function displayResults(data) {
    var resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
}

